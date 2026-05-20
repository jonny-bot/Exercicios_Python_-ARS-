# config.py - Configurações centralizadas do projeto

# Cores padrão do projeto
CORES = {
    "primaria": "#2563EB",
    "sucesso": "#059669",
    "roxo": "#7C3AED",
    "cinza": "#6B7280",
    "cinza_claro": "#9CA3AF",
    "fundo": "#F9FAFB",
    "texto": "#111827",
    "borda": "#D1D5DB",
    "erro": "#DC2626"
}

# Fontes padrão
FONTS = {
    "titulo_grande": ("Segoe UI", 20, True),
    "titulo": ("Segoe UI", 16, True),
    "botao": ("Segoe UI", 14, False),
    "padrao": ("Segoe UI", 12, False),
    "pequeno": ("Segoe UI", 10, False)
}

# Geometria das janelas
GEOMETRIA = {
    "menu": (200, 100, 500, 400),
    "janela_grande": (200, 100, 1200, 800),
    "janela_media": (200, 100, 1100, 750)
}

# Constantes da aplicação
APP_TITLE = "Simuladores Financeiros"
IR_PADRAO = 0.15
LIMITE_MESES_SIMULACAO = 2400
META_PRIMEIRO_MILHAO = 1_000_000
