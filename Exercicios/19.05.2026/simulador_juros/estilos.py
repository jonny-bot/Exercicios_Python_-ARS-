# estilos.py - Consolidação de estilos CSS para toda a aplicação

from config import CORES
from PyQt5.QtCore import Qt

# Estilos de botões
BOTAO_PRIMARIO = f"""
    background: {CORES['primaria']};
    color: #fff;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
    border: none;
"""

BOTAO_SUCESSO = f"""
    background: {CORES['sucesso']};
    color: #fff;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
    border: none;
"""

BOTAO_SECUNDARIO = f"""
    background: {CORES['cinza']};
    color: #fff;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
    border: none;
"""

BOTAO_OUTLINE = f"""
    background: #fff;
    color: {CORES['texto']};
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
    border: 1px solid {CORES['borda']};
"""

BOTAO_PERIGO = f"""
    background: {CORES['erro']};
    color: #fff;
    padding: 10px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
    border: none;
"""

# Estilos para campos de entrada
CAMPO_TEXTO = f"""
    padding: 6px;
    border: 1px solid {CORES['borda']};
    border-radius: 6px;
    background: #FFFFFF;
    color: {CORES['texto']};
"""

# Estilos para labels
LABEL_TITULO = f"""
    color: {CORES['texto']};
    font-weight: bold;
    margin-bottom: 5px;
"""

# Factory functions para criar botões estilizados
def get_estilo_botao(tipo="primario"):
    """Retorna o estilo CSS para um tipo de botão"""
    estilos = {
        "primario": BOTAO_PRIMARIO,
        "sucesso": BOTAO_SUCESSO,
        "secundario": BOTAO_SECUNDARIO,
        "outline": BOTAO_OUTLINE,
        "perigo": BOTAO_PERIGO
    }
    return estilos.get(tipo, BOTAO_PRIMARIO)

def criar_botao_estilizado(texto, tipo="primario"):
    """Factory para criar um QPushButton com estilo já aplicado"""
    from PyQt5.QtWidgets import QPushButton
    botao = QPushButton(texto)
    botao.setStyleSheet(get_estilo_botao(tipo))
    botao.setCursor(Qt.PointingHandCursor)
    return botao
