from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from .telas.ui_juros_compostos import SimuladorJuros
from .telas.ui_primeiro_milhao import CalculadoraPrimeiroMilhao
from .telas.ui_juros_simples import CalculadoraJurosSimples
from .telas.controle_gastos import ControleGastos
from .telas.numero_magico import NumeroMagico
from .telas.metas_financeiras import MetasFinanceiras


class MenuPrincipal(QWidget):
    BTN_SIZE = (180, 55)
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

    THEMES = {
        "light": """
            QWidget { background-color: #F3F4F6; color: #111827; }
            QLabel { color: #111827; }
        """,
        "dark": """
            QWidget { background-color: #1F2937; color: #F9FAFB; }
            QLabel { color: #F9FAFB; }
        """
    }

    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.dark_mode = dark_mode
        self.voltar_callback = voltar_callback
        self.stack = QStackedWidget()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Menu Principal - Simuladores Financeiros")
        layout = QVBoxLayout(self)

        # Página inicial (menu principal)
        menu_page = QWidget()
        menu_layout = QVBoxLayout(menu_page)

        # Títulos
        menu_layout.addWidget(self._build_label("CENTRAL DE SIMULADORES", 24, QFont.Bold))
        menu_layout.addWidget(self._build_label("Pessoal", 16))
        menu_layout.addLayout(self._build_section([
            ("📝 Gastos Mensais", "#1E90FF", lambda: self._switch_page(self.gastos)),
            ("🔢 Número Mágico", "#512DE6", lambda: self._switch_page(self.numero_magico)),
            ("🎯 Metas Financeiras", "#F97316", lambda: self._switch_page(self.metas))
        ]))

        menu_layout.addWidget(self._build_label("Calculadoras", 16))
        menu_layout.addLayout(self._build_section([
            ("📈 Juros Compostos", "#2563EB", lambda: self._switch_page(self.simulador)),
            ("💰 Primeiro Milhão", "#059669", lambda: self._switch_page(self.milhao)),
            ("📊 Juros Simples", "#7C3AED", lambda: self._switch_page(self.simples))
        ]))

        menu_layout.addWidget(self._build_button("LOGOUT", "#F59E0B", self.voltar_login),
                              alignment=Qt.AlignCenter)

        # Adiciona menu_page primeiro
        self.stack.addWidget(menu_page)
        layout.addWidget(self.stack)

        # 🔑 Força abrir direto no menu inicial
        self.stack.setCurrentIndex(0)

        # Telas internas
        self.gastos = ControleGastos(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.numero_magico = NumeroMagico(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.metas = MetasFinanceiras(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.simulador = SimuladorJuros(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.milhao = CalculadoraPrimeiroMilhao(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.simples = CalculadoraJurosSimples(voltar_callback=self.show_menu, dark_mode=self.dark_mode)

        for tela in [self.gastos, self.numero_magico, self.metas, self.simulador, self.milhao, self.simples]:
            self.stack.addWidget(tela)

        self.apply_theme()
        self.showMaximized()

    def _build_label(self, text, size, weight=QFont.Normal):
        label = QLabel(text)
        label.setFont(QFont("Segoe UI", size, weight))
        label.setAlignment(Qt.AlignCenter)
        return label

    def _build_section(self, buttons):
        layout = QHBoxLayout()
        for text, color, callback in buttons:
            layout.addWidget(self._build_button(text, color, callback))
        return layout

    def _build_button(self, text, color, callback):
        btn = QPushButton(text)
        btn.setFixedSize(*self.BTN_SIZE)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(self.BTN_STYLE.format(cor=color))
        btn.clicked.connect(callback)
        return btn

    def _switch_page(self, page):
        self.stack.setCurrentWidget(page)

    def apply_theme(self):
        theme = "dark" if self.dark_mode else "light"
        self.setStyleSheet(self.THEMES[theme])

        # Atualiza também as telas internas
        self.gastos.apply_theme()
        self.numero_magico.atualizar_tema(self.dark_mode)
        self.metas.atualizar_tema(self.dark_mode)
        self.simulador.atualizar_tema(self.dark_mode)
        self.milhao.atualizar_tema(self.dark_mode)
        self.simples.atualizar_tema(self.dark_mode)

    def show_menu(self):
        self.stack.setCurrentIndex(0)

    def voltar_login(self):
        self.close()
        if self.voltar_callback:
            self.voltar_callback()
