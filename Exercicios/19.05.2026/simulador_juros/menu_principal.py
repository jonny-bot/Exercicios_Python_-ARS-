from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from ui_juros_compostos import SimuladorJuros
from ui_primeiro_milhao import CalculadoraPrimeiroMilhao
from ui_juros_simples import CalculadoraJurosSimples
from config import GEOMETRIA, APP_TITLE
from tema import aplicar_tema_claro, get_fonte
from estilos import criar_botao_estilizado

class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"Menu Principal - {APP_TITLE}")
        x, y, width, height = GEOMETRIA["menu"]
        self.setGeometry(x, y, width, height)

        # Aplicar tema
        aplicar_tema_claro(self)

        layout = QVBoxLayout(self)

        # Título estilizado
        titulo = QLabel("CENTRAL DE SIMULADORES")
        titulo.setFont(get_fonte("titulo_grande"))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)
        layout.addSpacing(20)

        # Botão Simulador de Juros Compostos
        btn_simulador = criar_botao_estilizado("📈 Simulador de Juros Compostos", "primario")
        btn_simulador.clicked.connect(self.abrir_simulador)
        layout.addWidget(btn_simulador)
        layout.addSpacing(10)

        # Botão Calculadora Primeiro Milhão
        btn_milhao = criar_botao_estilizado("💰 Calculadora do Primeiro Milhão", "sucesso")
        btn_milhao.clicked.connect(self.abrir_primeiro_milhao)
        layout.addWidget(btn_milhao)
        layout.addSpacing(10)

        # Botão Calculadora Juros Simples
        btn_simples = criar_botao_estilizado("📊 Calculadora de Juros Simples", "roxo")
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
