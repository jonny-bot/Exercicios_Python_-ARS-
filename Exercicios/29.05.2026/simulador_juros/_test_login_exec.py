from PyQt5.QtWidgets import QApplication
from tela_login import TelaLogin

app = QApplication([])
login = TelaLogin()
login.input_login.setText('Joao')
login.input_senha.setText('ars@3103')
login.validar_login()
print('login callback executed')
