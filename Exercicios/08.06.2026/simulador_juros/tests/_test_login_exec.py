import os
import sys
from PyQt5.QtWidgets import QApplication
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.tela_login import TelaLogin

app = QApplication([])
login = TelaLogin()
login.input_login.setText('Joao')
login.input_senha.setText('ars@3103')
login.validar_login()
print('login callback executed')
