import os
import sys
import re
import sqlite3
import hashlib
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from .menu_principal import MenuPrincipal
from .tema import aplicar_tema

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_NAME = os.path.join(BASE_DIR, "data", "usuarios.db")
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".png"))


def _hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def init_db():
    """Cria o banco de dados e tabela de usuários se não existir."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    # Migra senhas antigas em texto simples para hash seguro
    cursor.execute("SELECT id, senha FROM usuarios")
    for user_id, senha in cursor.fetchall():
        if not re.fullmatch(r"[0-9a-f]{64}", senha or ""):
            cursor.execute(
                "UPDATE usuarios SET senha=? WHERE id=?",
                (_hash_password(senha), user_id)
            )

    # Usuário padrão para testes
    cursor.execute("INSERT OR IGNORE INTO usuarios (login, senha) VALUES (?, ?)", ("joao", _hash_password("ars@3103")))
    conn.commit()
    conn.close()


class TelaLogin(QWidget):
    BTN_SIZE = (200, 40)
    INPUT_SIZE = (250, 40)

    ICONS = {
        "light": os.path.join(ASSETS_DIR, "sun_icon.png"),
        "dark": os.path.join(ASSETS_DIR, "moon_icon.png")
    }

    STYLES = {
        "dark": """
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
        """,
        "light": """
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
        """
    }

    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.anim = QPropertyAnimation()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tela de Login")
        self.resize(400, 350)

        layout = QVBoxLayout(self)
        layout.addLayout(self._build_top_layout())
        layout.addWidget(self._build_title())

        # Inputs
        self.input_login = self._build_input("Digite seu login", False)
        layout.addLayout(self._center_widget(self.input_login))

        self.input_senha = self._build_input("Digite sua senha", True)
        layout.addLayout(self._center_widget(self.input_senha))

        # Botões
        layout.addLayout(self._build_button_row())

        self.apply_theme()

    def _build_top_layout(self):
        top_layout = QHBoxLayout()
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon(self.ICONS["light"]).pixmap(24, 24))

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
        input_field.setFixedSize(*self.INPUT_SIZE)
        if is_password:
            input_field.setEchoMode(QLineEdit.Password)
        return input_field

    def _build_button_row(self):
        row = QHBoxLayout()
        row.setAlignment(Qt.AlignCenter)

        btn_entrar = self._build_button("ENTRAR", self.validar_login, default=True)
        btn_cadastrar = self._build_button("CADASTRAR", self.cadastrar_usuario)
        btn_sair = self._build_button("SAIR", QApplication.quit)

        row.addWidget(btn_entrar)
        row.addSpacing(10)
        row.addWidget(btn_cadastrar)
        row.addSpacing(10)
        row.addWidget(btn_sair)
        return row

    def _build_button(self, text, callback, default=False):
        btn = QPushButton(text)
        btn.setFixedSize(*self.BTN_SIZE)
        btn.clicked.connect(callback)
        if default:
            btn.setDefault(True)
        return btn

    def _center_widget(self, widget):
        row = QHBoxLayout()
        row.addWidget(widget, alignment=Qt.AlignCenter)
        return row

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.validar_login()

    def apply_theme(self):
        aplicar_tema(self, self.dark_mode)
        theme = "dark" if self.dark_mode else "light"

        self.icon_label.setPixmap(QIcon(self.ICONS[theme]).pixmap(24, 24))
        self.bolinha.setStyleSheet(
            "background-color: #FACC15; border-radius: 12px;" if self.dark_mode
            else "background-color: #9CA3AF; border-radius: 12px;"
        )
        self.setStyleSheet(self.STYLES[theme])

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

        self.anim = QPropertyAnimation(self.bolinha, b"geometry")
        self.anim.setDuration(300)
        start, end = (QRect(4, 4, 26, 26), QRect(40, 4, 26, 26)) if self.dark_mode else (QRect(40, 4, 26, 26), QRect(4, 4, 26, 26))
        self.anim.setStartValue(start)
        self.anim.setEndValue(end)
        self.anim.start()

    def validar_login(self):
        login = self.input_login.text().strip()
        senha = self.input_senha.text().strip()

        if not login or not senha:
            QMessageBox.warning(self, "Erro de Login", "Preencha login e senha para continuar.")
            return

        senha_hash = _hash_password(senha)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha=?", (login, senha_hash))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            try:
                self.menu = MenuPrincipal(voltar_callback=self.show_login, dark_mode=self.dark_mode)
                self.menu.showMaximized()
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Erro ao Abrir Menu", f"Ocorreu um erro ao abrir o menu:\n{e}")
        else:
            QMessageBox.warning(self, "Erro de Login", "Usuário ou senha inválidos.\nPor favor, tente novamente.")

    def cadastrar_usuario(self):
        login = self.input_login.text().strip()
        senha = self.input_senha.text().strip()

        if not login or not senha:
            QMessageBox.warning(self, "Cadastro Inválido", "Preencha login e senha para cadastrar.")
            return

        senha_hash = _hash_password(senha)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha_hash))
            conn.commit()
            QMessageBox.information(self, "Cadastro Realizado", "Usuário cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Erro de Cadastro", "Este login já existe. Escolha outro.")
        finally:
            conn.close()

    def show_login(self):
        self.show()
