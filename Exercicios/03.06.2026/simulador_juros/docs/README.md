# Estrutura do Projeto

Este projeto foi reorganizado para ficar mais modular e fácil de manter.

- `app/`
  - `tela_login.py` — tela de login e início da aplicação
  - `menu_principal.py` — menu principal que navega entre simuladores
  - `tema.py` — gerenciamento de tema (light/dark)
  - `telas/` — telas específicas de UI
    - `controle_gastos.py`
    - `numero_magico.py`
    - `ui_juros_compostos.py`
    - `ui_juros_simples.py`
    - `ui_primeiro_milhao.py`

- `core/`
  - `funcoes.py` — lógica de exportação, cálculo e utilitários
  - `graficos.py` — criação de gráficos para as telas

- `data/`
  - `usuarios.db` — banco de dados local de usuários
  - `dados_exportados/` — arquivos de exemplo exportados

- `tests/`
  - scripts de validação e testes rápidos do projeto

- `docs/`
  - documentação do projeto e estrutura de pastas
