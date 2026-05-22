from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from menu_principal import MenuPrincipal
from tema import aplicar_tema

class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tela de Login")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # Layout superior (switch de tema)
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(8)

        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon("sun_icon.png").pixmap(24, 24))
        top_layout.addWidget(self.icon_label, alignment=Qt.AlignVCenter)

        self.btn_tema = QPushButton()
        self.btn_tema.setFixedSize(70, 34)
        self.btn_tema.setCursor(Qt.PointingHandCursor)
        self.btn_tema.setCheckable(True)
        self.btn_tema.setStyleSheet("""
            QPushButton {
                background-color: #E5E7EB;
                border-radius: 17px;
                border: 2px solid #9CA3AF;
            }
        """)
        self.btn_tema.clicked.connect(self.toggle_theme)
        top_layout.addWidget(self.btn_tema, alignment=Qt.AlignVCenter)

        # Bolinha dentro do botão
        self.bolinha = QLabel(self.btn_tema)
        self.bolinha.setStyleSheet("background-color: #2563EB; border-radius: 12px;")
        self.bolinha.setGeometry(4, 4, 26, 26)

        layout.addLayout(top_layout)
        layout.setAlignment(top_layout, Qt.AlignRight)

        titulo = QLabel("LOGIN")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Campo Login
        self.input_login = QLineEdit()
        self.input_login.setPlaceholderText("Digite seu login")
        self.input_login.setFixedHeight(40)
        layout.addWidget(self.input_login)

        # Campo Senha
        self.input_senha = QLineEdit()
        self.input_senha.setPlaceholderText("Digite sua senha")
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.input_senha.setFixedHeight(40)
        layout.addWidget(self.input_senha)

        # Botão Entrar
        btn_entrar = QPushButton("ENTRAR")
        btn_entrar.setFixedHeight(40)
        btn_entrar.clicked.connect(self.validar_login)
        layout.addWidget(btn_entrar)

        # Botão Sair
        btn_sair = QPushButton("SAIR")
        btn_sair.setFixedHeight(40)
        btn_sair.clicked.connect(QApplication.quit)
        layout.addWidget(btn_sair)

        self.apply_theme()

    def apply_theme(self):
        aplicar_tema(self, self.dark_mode)

        if self.dark_mode:
            self.icon_label.setPixmap(QIcon("moon_icon.png").pixmap(24, 24))
            self.bolinha.setStyleSheet("background-color: #FACC15; border-radius: 12px;")
            self.setStyleSheet("""
                QWidget { background-color: #1F2937; color: #F9FAFB; }
                QLineEdit {
                    background-color: #374151; color: #F9FAFB;
                    border: 2px solid #9CA3AF; border-radius: 8px; padding: 8px;
                }
                QPushButton {
                    background-color: #2563EB; color: #fff;
                    font-weight: bold; border-radius: 8px; height: 40px;
                }
                QPushButton:hover { background-color: #1E40AF; }
            """)
        else:
            self.icon_label.setPixmap(QIcon("sun_icon.png").pixmap(24, 24))
            self.bolinha.setStyleSheet("background-color: #2563EB; border-radius: 12px;")
            self.setStyleSheet("""
                QWidget { background-color: #F3F4F6; color: #111827; }
                QLineEdit {
                    background-color: #fff; color: #111827;
                    border: 2px solid #9CA3AF; border-radius: 8px; padding: 8px;
                }
                QPushButton {
                    background-color: #2563EB; color: #fff;
                    font-weight: bold; border-radius: 8px; height: 40px;
                }
                QPushButton:hover { background-color: #1E40AF; }
            """)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

        self.anim = QPropertyAnimation(self.bolinha, b"geometry")
        self.anim.setDuration(300)
        if self.dark_mode:
            self.anim.setStartValue(QRect(4, 4, 26, 26))
            self.anim.setEndValue(QRect(40, 4, 26, 26))
        else:
            self.anim.setStartValue(QRect(40, 4, 26, 26))
            self.anim.setEndValue(QRect(4, 4, 26, 26))
        self.anim.start()

    def validar_login(self):
        login = self.input_login.text()
        senha = self.input_senha.text()

        if login == "Joao" and senha == "ars@3103":
            # passa o estado do tema escolhido para o MenuPrincipal
            self.menu = MenuPrincipal(voltar_callback=self.show_login, dark_mode=self.dark_mode)
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Acesso negado. Usuário ou senha inválidos.")

    def show_login(self):
        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())
