from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from menu_principal import MenuPrincipal
from tema import aplicar_tema


class TelaLogin(QWidget):
    BTN_WIDTH = 200
    BTN_HEIGHT = 40
    INPUT_WIDTH = 250
    INPUT_HEIGHT = 40

    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tela de Login")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # Layout superior (switch de tema)
        layout.addLayout(self._build_top_layout())
        layout.addWidget(self._build_title())

        # Campos de login e senha centralizados
        self.input_login = self._build_input("Digite seu login", False)
        layout.addLayout(self._center_widget(self.input_login))

        self.input_senha = self._build_input("Digite sua senha", True)
        layout.addLayout(self._center_widget(self.input_senha))

        # Botões centralizados
        layout.addLayout(self._build_button_row())

        self.apply_theme()

    def _build_top_layout(self):
        top_layout = QHBoxLayout()
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon(".png/sun_icon.png").pixmap(24, 24))

        self.btn_tema = QPushButton()
        self.btn_tema.setFixedSize(70, 34)
        self.btn_tema.setCursor(Qt.PointingHandCursor)
        self.btn_tema.setCheckable(True)
        self.btn_tema.clicked.connect(self.toggle_theme)

        self.bolinha = QLabel(self.btn_tema)
        self.bolinha.setGeometry(4, 4, 26, 26)

        top_layout.addWidget(self.icon_label, alignment=Qt.AlignVCenter)
        top_layout.addWidget(self.btn_tema, alignment=Qt.AlignVCenter)
        top_layout.setAlignment(Qt.AlignRight)
        return top_layout

    def _build_title(self):
        titulo = QLabel("LOGIN")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        return titulo

    def _build_input(self, placeholder, is_password):
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedSize(self.INPUT_WIDTH, self.INPUT_HEIGHT)
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
        return input_field

    def _build_button_row(self):
        row = QHBoxLayout()
        row.setAlignment(Qt.AlignCenter)

        btn_entrar = self._build_button("ENTRAR", self.validar_login, default=True)
        btn_sair = self._build_button("SAIR", QApplication.quit)

        row.addWidget(btn_entrar)
        row.addSpacing(20)
        row.addWidget(btn_sair)

        return row

    def _build_button(self, text, callback, default=False):
        btn = QPushButton(text)
        btn.setFixedSize(self.BTN_WIDTH, self.BTN_HEIGHT)
        btn.clicked.connect(callback)
        if default:
            btn.setDefault(True)
        return btn

    def _center_widget(self, widget):
        """Envolve um widget em um layout horizontal centralizado."""
        row = QHBoxLayout()
        row.addWidget(widget, alignment=Qt.AlignCenter)
        return row

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.validar_login()

    def apply_theme(self):
        aplicar_tema(self, self.dark_mode)

        if self.dark_mode:
            self.icon_label.setPixmap(QIcon(".png/moon_icon.png").pixmap(24, 24))
            self.bolinha.setStyleSheet("background-color: #FACC15; border-radius: 12px;")
            self.setStyleSheet("""
                QWidget { background-color: #1F2937; color: #F9FAFB; }
                QLineEdit {
                    background-color: #374151; color: #F9FAFB;
                    border: 2px solid #9CA3AF; border-radius: 8px; padding: 8px;
                }
                QPushButton {
                    background-color: #2563EB; color: #fff;
                    font-weight: bold; border-radius: 8px;
                }
                QPushButton:hover { background-color: #1E40AF; }
            """)
        else:
            self.icon_label.setPixmap(QIcon(".png/sun_icon.png").pixmap(24, 24))
            self.bolinha.setStyleSheet("background-color: #2563EB; border-radius: 12px;")
            self.setStyleSheet("""
                QWidget { background-color: #F3F4F6; color: #111827; }
                QLineEdit {
                    background-color: #fff; color: #111827;
                    border: 2px solid #9CA3AF; border-radius: 8px; padding: 8px;
                }
                QPushButton {
                    background-color: #2563EB; color: #fff;
                    font-weight: bold; border-radius: 8px;
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
            self.menu = MenuPrincipal(voltar_callback=self.show_login, dark_mode=self.dark_mode)
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Erro de Login",
                "Usuário ou senha inválidos.\nPor favor, tente novamente."
            )

    def show_login(self):
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())
