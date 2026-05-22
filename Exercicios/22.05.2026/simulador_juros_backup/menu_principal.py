from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from ui_juros_compostos import SimuladorJuros
from ui_primeiro_milhao import CalculadoraPrimeiroMilhao
from ui_juros_simples import CalculadoraJurosSimples

class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu Principal - Simuladores Financeiros")
        self.resize(1100, 750)

        # Tema claro
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 12))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        # Usamos um stack para renderizar várias telas dentro da mesma janela
        self.stack = QStackedWidget()

        # Página inicial do menu
        menu_page = QWidget()
        menu_layout = QVBoxLayout(menu_page)
        menu_layout.setContentsMargins(24, 24, 24, 24)
        menu_layout.setSpacing(14)

        titulo = QLabel("CENTRAL DE SIMULADORES")
        titulo.setFont(QFont("Segoe UI", 24, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:20px;")
        menu_layout.addWidget(titulo)

        btn_simulador = QPushButton("📈 Simulador de Juros Compostos")
        btn_simulador.setStyleSheet("background:#2563EB; color:#fff; padding:16px; font-size:16px; border-radius:8px;")
        btn_simulador.clicked.connect(lambda: self.stack.setCurrentWidget(self.simulador))
        menu_layout.addWidget(btn_simulador)

        btn_milhao = QPushButton("💰 Calculadora do Primeiro Milhão")
        btn_milhao.setStyleSheet("background:#059669; color:#fff; padding:16px; font-size:16px; border-radius:8px;")
        btn_milhao.clicked.connect(lambda: self.stack.setCurrentWidget(self.milhao))
        menu_layout.addWidget(btn_milhao)

        btn_simples = QPushButton("📊 Calculadora de Juros Simples")
        btn_simples.setStyleSheet("background:#7C3AED; color:#fff; padding:16px; font-size:16px; border-radius:8px;")
        btn_simples.clicked.connect(lambda: self.stack.setCurrentWidget(self.simples))
        menu_layout.addWidget(btn_simples)

        btn_sair = QPushButton("SAIR")
        btn_sair.setStyleSheet("background:#EF4444; color:#fff; padding:16px; font-size:16px; border-radius:8px;")
        btn_sair.clicked.connect(QApplication.quit)
        menu_layout.addWidget(btn_sair)

        self.stack.addWidget(menu_page)

        self.simulador = SimuladorJuros(voltar_callback=self.show_menu)
        self.milhao = CalculadoraPrimeiroMilhao(voltar_callback=self.show_menu)
        self.simples = CalculadoraJurosSimples(voltar_callback=self.show_menu)

        self.stack.addWidget(self.simulador)
        self.stack.addWidget(self.milhao)
        self.stack.addWidget(self.simples)

        layout.addWidget(self.stack)

        # centraliza a janela na tela do usuário
        self.center_window()

    def show_menu(self):
        """Retorna à página inicial dentro do stack."""
        self.stack.setCurrentIndex(0)

    def center_window(self):
        """Posiciona a janela no centro do monitor do usuário."""
        screen = QApplication.primaryScreen().availableGeometry()
        frame = self.frameGeometry()
        frame.moveCenter(screen.center())
        self.move(frame.topLeft())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = MenuPrincipal()
    menu.show()
    sys.exit(app.exec_())
