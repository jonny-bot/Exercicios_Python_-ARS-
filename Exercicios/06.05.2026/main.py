import os
import subprocess
from tqdm import tqdm


def export_requirements(filename="requirements.txt"):
    """Exporta as bibliotecas instaladas para um arquivo."""
    try:

        with open(filename, "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)
        print(f"✅ Bibliotecas exportadas para {filename}")

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao exportar bibliotecas:", e)

    except Exception as e:
        print("❌ Erro inesperado ao criar o arquivo:", e)


def install_requirements(filename="requirements.txt"):
    """Instala/atualiza bibliotecas a partir do arquivo com barra de progresso."""
    try:

        if os.path.exists(filename):
            # Lê todas as bibliotecas do arquivo

            with open(filename, "r") as f:
                libs = [line.strip() for line in f if line.strip()]

            print("📦 Instalando bibliotecas...\n")
            for lib in tqdm(libs, desc="Progresso", unit="pacote"):
                try:

                    subprocess.run(["pip", "install", lib], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                except subprocess.CalledProcessError:
                    print(f"\n⚠️ Falha ao instalar {lib}")

            print("\n✅ Instalação concluída!")

        else:
            print(f"⚠️ Arquivo {filename} não encontrado.")

    except Exception as e:
        print("❌ Erro inesperado:", e)

if __name__ == "__main__":
    try:
        export_requirements()

        install_requirements()
        
    except Exception as e:
        print("❌ Ocorreu um erro geral no programa:", e)
