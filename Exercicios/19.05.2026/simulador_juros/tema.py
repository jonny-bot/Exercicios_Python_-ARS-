# tema.py - Aplicação de temas consistentes

from PyQt5.QtGui import QFont, QColor, QPalette
from config import CORES, FONTS

def aplicar_tema_claro(widget):
    """Aplica tema claro padrão a um widget"""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(CORES["fundo"]))
    palette.setColor(QPalette.WindowText, QColor(CORES["texto"]))
    widget.setPalette(palette)
    
    fonte = QFont(FONTS["padrao"][0], FONTS["padrao"][1])
    widget.setFont(fonte)

def get_fonte(tipo="padrao"):
    """Retorna uma fonte QFont baseada no tipo especificado"""
    spec = FONTS.get(tipo, FONTS["padrao"])
    fonte = QFont(spec[0], spec[1])
    if len(spec) > 2 and spec[2]:
        fonte.setBold(True)
    return fonte

def get_cor(nome):
    """Retorna uma cor RGB em formato string"""
    return CORES.get(nome, CORES["fundo"])
