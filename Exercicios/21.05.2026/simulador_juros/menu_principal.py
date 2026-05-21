from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
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
        self.setGeometry(200, 100, 500, 400)

        # Tema claro
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 12))

        layout = QVBoxLayout(self)

        # Título
        titulo = QLabel("CENTRAL DE SIMULADORES")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:20px;")
        layout.addWidget(titulo)

        # Botões
        btn_simulador = QPushButton("📈 Simulador de Juros Compostos")
        btn_simulador.setStyleSheet("background:#2563EB; color:#fff; padding:12px; font-size:14px; border-radius:6px;")
        btn_simulador.clicked.connect(self.abrir_simulador)
        layout.addWidget(btn_simulador)

        btn_milhao = QPushButton("💰 Calculadora do Primeiro Milhão")
        btn_milhao.setStyleSheet("background:#059669; color:#fff; padding:12px; font-size:14px; border-radius:6px;")
        btn_milhao.clicked.connect(self.abrir_primeiro_milhao)
        layout.addWidget(btn_milhao)

        btn_simples = QPushButton("📊 Calculadora de Juros Simples")
        btn_simples.setStyleSheet("background:#7C3AED; color:#fff; padding:12px; font-size:14px; border-radius:6px;")
        btn_simples.clicked.connect(self.abrir_juros_simples)
        layout.addWidget(btn_simples)

    def abrir_simulador(self):
        self.simulador = SimuladorJuros()
        self.simulador.show()

    def abrir_primeiro_milhao(self):
        self.milhao = CalculadoraPrimeiroMilhao()
        self.milhao.show()

    def abrir_juros_simples(self):
        self.simples = CalculadoraJurosSimples()
        self.simples.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = MenuPrincipal()
    menu.show()
    sys.exit(app.exec_())
