# validadores.py - Validadores reutilizáveis para campos de entrada

from PyQt5.QtGui import QDoubleValidator, QIntValidator

class ValidadorMonetario(QDoubleValidator):
    """Validador para valores monetários"""
    def __init__(self):
        super().__init__(0, 999999999, 2)
        self.setNotation(QDoubleValidator.StandardNotation)

class ValidadorTaxa(QDoubleValidator):
    """Validador para taxas percentuais (0-100)"""
    def __init__(self):
        super().__init__(0, 100, 4)
        self.setNotation(QDoubleValidator.StandardNotation)

class ValidadorMeses(QIntValidator):
    """Validador para período em meses"""
    def __init__(self):
        super().__init__(1, 2400)

class ValidadorAnos(QIntValidator):
    """Validador para período em anos"""
    def __init__(self):
        super().__init__(1, 200)

def criar_campo_monetario(placeholder=""):
    """Factory para criar um QLineEdit monetário pronto"""
    from PyQt5.QtWidgets import QLineEdit
    campo = QLineEdit()
    campo.setValidator(ValidadorMonetario())
    campo.setPlaceholderText(placeholder)
    campo.setMinimumHeight(34)
    return campo

def criar_campo_taxa(placeholder=""):
    """Factory para criar um QLineEdit de taxa pronto"""
    from PyQt5.QtWidgets import QLineEdit
    campo = QLineEdit()
    campo.setValidator(ValidadorTaxa())
    campo.setPlaceholderText(placeholder)
    campo.setMinimumHeight(34)
    return campo
