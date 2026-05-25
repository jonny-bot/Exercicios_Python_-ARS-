import subprocess
import json
import datetime
from tqdm import tqdm  # biblioteca para barra de progresso

def run_command(command):
    """Executa um comando no shell e retorna código, saída e erro."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def get_installed_packages():
    """Retorna pacotes já instalados (pip freeze)."""
    code, out, err = run_command("pip freeze")
    if code == 0:
        return {line.split("==")[0].lower(): line.split("==")[1] for line in out.splitlines() if "==" in line}
    return {}

def read_requirements(requirements_file):
    """Lê requirements.txt tentando diferentes codificações e limpando caracteres inválidos."""
    encodings = ["utf-8", "utf-16", "latin-1"]
    for enc in encodings:
        try:
            with open(requirements_file, "r", encoding=enc) as f:
                lines = f.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("Não foi possível decodificar o arquivo requirements.txt")

    requirements = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.replace("\x00", "")
        requirements.append(line)
    return requirements

def install_requirements(requirements_file="requirements.txt"):
    installed = get_installed_packages()
    log = {
        "process_summary": {
            "total_packages": 0,
            "already_ok": 0,
            "installed_successfully": 0,
            "updated_successfully": 0,
            "manual_corrections": 0,
            "persistent_errors": 0
        },
        "packages": [],
        "validation": {},
        "timestamp": datetime.datetime.now().isoformat(),
        "final_status": "in_progress"
    }

    failed_packages = []

    # 1. Ler requirements.txt
    requirements = read_requirements(requirements_file)
    log["process_summary"]["total_packages"] = len(requirements)

    # 2. Instalação pacote a pacote com barra + log textual
    for req in tqdm(requirements, desc="Instalando pacotes", unit="pacote"):
        if "==" in req:
            pkg, version = req.split("==", 1)
        else:
            pkg, version = req, None

        pkg_lower = pkg.lower()

        if version and pkg_lower in installed and installed[pkg_lower] == version:
            log["process_summary"]["already_ok"] += 1
            log["packages"].append({
                "name": pkg,
                "target_version": version,
                "final_version": version,
                "status": "already_ok"
            })
            print(f"[OK] {pkg} já estava na versão correta ({version})")
            continue

        print(f"[...] Instalando {req}...")
        code, out, err = run_command(f"pip install {req}")
        if code == 0:
            status = "installed_successfully" if pkg_lower not in installed else "updated_successfully"
            log["process_summary"][status] += 1
            log["packages"].append({
                "name": pkg,
                "target_version": version,
                "final_version": version if version else "latest",
                "status": status
            })
            print(f"[SUCESSO] {pkg} instalado/atualizado")
        else:
            failed_packages.append(req)
            log["packages"].append({
                "name": pkg,
                "target_version": version,
                "final_version": None,
                "status": "failed_initial",
                "notes": err
            })
            print(f"[ERRO] Falha ao instalar {pkg}: {err}")

    # 3. Tentativa manual com barra + log textual
    for req in tqdm(failed_packages, desc="Tentando correções manuais", unit="pacote"):
        pkg = req.split("==")[0] if "==" in req else req
        print(f"[...] Tentando corrigir {req}...")
        code, out, err = run_command(f"pip install {req}")
        if code == 0:
            log["process_summary"]["manual_corrections"] += 1
            log["packages"].append({
                "name": pkg,
                "final_version": "corrigida",
                "status": "manual_correction"
            })
            print(f"[CORRIGIDO] {pkg} instalado manualmente")
        else:
            log["process_summary"]["persistent_errors"] += 1
            log["packages"].append({
                "name": pkg,
                "final_version": None,
                "status": "persistent_error",
                "notes": err
            })
            print(f"[FALHA] {pkg} não pôde ser instalado: {err}")

    # 4. Validação final
    code, out, err = run_command("pip check")
    log["validation"]["pip_check"] = out if code == 0 else err

    # 5. Status final
    if log["process_summary"]["persistent_errors"] > 0:
        log["final_status"] = "completed_with_warnings"
    else:
        log["final_status"] = "completed_successfully"

    # 6. Exporta relatório JSON
    with open("install_report.json", "w", encoding="utf-8") as f:
        json.dump(log, f, indent=4, ensure_ascii=False)

    return log


if __name__ == "__main__":
    report = install_requirements("requirements.txt")
    print(json.dumps(report, indent=4, ensure_ascii=False))
