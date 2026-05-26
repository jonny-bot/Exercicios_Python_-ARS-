from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui_juros_compostos import SimuladorJuros
from ui_primeiro_milhao import CalculadoraPrimeiroMilhao
from ui_juros_simples import CalculadoraJurosSimples
from controle_gastos import ControleGastos   # <-- Importa sua nova tela


class MenuPrincipal(QWidget):
    BTN_WIDTH = 180
    BTN_HEIGHT = 55
    BTN_STYLE = """
        QPushButton {{
            background:{cor};
            color:#fff;
            font-size:15px;
            font-weight:500;
            border-radius:8px;
            padding:10px;
        }}
        QPushButton:hover {{
            background-color:#333;
        }}
    """

    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.dark_mode = dark_mode
        self.voltar_callback = voltar_callback
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Menu Principal - Simuladores Financeiros")
        self.resize(800, 600)

        layout = QVBoxLayout(self)
        self.stack = QStackedWidget()

        # Página inicial (menu)
        menu_page = QWidget()
        menu_layout = QVBoxLayout(menu_page)

        titulo = QLabel("CENTRAL DE SIMULADORES")
        titulo.setFont(QFont("Segoe UI", 24, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        menu_layout.addWidget(titulo, alignment=Qt.AlignCenter)

        # Botões principais
        menu_layout.addWidget(self._build_button("📝 Gastos Mensais", "#1E90FF",
                                                 lambda: self.stack.setCurrentWidget(self.gastos)),
                              alignment=Qt.AlignCenter)

        menu_layout.addWidget(self._build_button("📈 Juros Compostos", "#2563EB",
                                                 lambda: self.stack.setCurrentWidget(self.simulador)),
                              alignment=Qt.AlignCenter)

        menu_layout.addWidget(self._build_button("💰 Primeiro Milhão", "#059669",
                                                 lambda: self.stack.setCurrentWidget(self.milhao)),
                              alignment=Qt.AlignCenter)

        menu_layout.addWidget(self._build_button("📊 Juros Simples", "#7C3AED",
                                                 lambda: self.stack.setCurrentWidget(self.simples)),
                              alignment=Qt.AlignCenter)

        # Botão Logout
        menu_layout.addWidget(self._build_button("LOGOUT", "#F59E0B", self.voltar_login),
                              alignment=Qt.AlignCenter)

        self.stack.addWidget(menu_page)

        # Instancia telas com suporte ao tema
        self.gastos = ControleGastos(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.simulador = SimuladorJuros(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.milhao = CalculadoraPrimeiroMilhao(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.simples = CalculadoraJurosSimples(voltar_callback=self.show_menu, dark_mode=self.dark_mode)

        self.stack.addWidget(self.gastos)
        self.stack.addWidget(self.simulador)
        self.stack.addWidget(self.milhao)
        self.stack.addWidget(self.simples)

        layout.addWidget(self.stack)
        self.apply_theme()

    def _build_button(self, text, color, callback):
        btn = QPushButton(text)
        btn.setFixedSize(self.BTN_WIDTH, self.BTN_HEIGHT)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(self.BTN_STYLE.format(cor=color))
        btn.clicked.connect(callback)
        return btn

    def apply_theme(self):
        theme_light = """
            QWidget { background-color: #F3F4F6; color: #111827; }
            QLabel { color: #111827; }
        """
        theme_dark = """
            QWidget { background-color: #1F2937; color: #F9FAFB; }
            QLabel { color: #F9FAFB; }
        """
        self.setStyleSheet(theme_dark if self.dark_mode else theme_light)

        # Atualiza também as telas internas
        self.gastos.apply_theme()
        self.simulador.atualizar_tema(self.dark_mode)
        self.milhao.atualizar_tema(self.dark_mode)
        self.simples.atualizar_tema(self.dark_mode)

    def show_menu(self):
        self.stack.setCurrentIndex(0)

    def voltar_login(self):
        self.close()
        if self.voltar_callback:
            self.voltar_callback()
