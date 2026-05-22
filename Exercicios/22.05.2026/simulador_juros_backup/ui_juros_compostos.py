from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QTableWidget, QHBoxLayout, QDateEdit
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QDate
from graficos import grafico_evolucao, grafico_composicao
from funcoes import calcular_juros, limpar_campos, exportar_dados

class SimuladorJuros(QWidget):
    """Tela do simulador de juros compostos.

    Esta classe renderiza um formulário de entrada, mostra resultados em tabela,
    gráficos de evolução e oferece navegação de volta ao menu principal.
    """
    def __init__(self, voltar_callback=None):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Juros Compostos")
        self.setGeometry(200, 100, 1100, 750)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)

        # Título
        titulo = QLabel("SIMULADOR DE JUROS COMPOSTOS")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:10px;")
        layout_principal.addWidget(titulo)

        # Entradas
        layout_inputs = QGridLayout()
        self.capital_inicial = QLineEdit()
        self.aporte_mensal = QLineEdit()
        self.taxa_juros = QLineEdit()
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])
        self.tempo = QLineEdit()
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Meses", "Anos"])
        self.data_inicio = QDateEdit()
        self.data_inicio.setDisplayFormat("dd/MM/yyyy")
        self.data_inicio.setDate(QDate.currentDate())

        for campo in [self.capital_inicial, self.aporte_mensal, self.taxa_juros, self.tempo]:
            campo.setStyleSheet("padding:6px; border:1px solid #D1D5DB; border-radius:6px;")

        layout_inputs.addWidget(QLabel("Valor Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 2)
        layout_inputs.addWidget(self.taxa_juros, 1, 2)
        layout_inputs.addWidget(self.tipo_taxa, 1, 3)
        layout_inputs.addWidget(QLabel("Tempo"), 0, 4)
        layout_inputs.addWidget(self.tempo, 1, 4)
        layout_inputs.addWidget(self.tipo_tempo, 1, 5)
        layout_inputs.addWidget(QLabel("Data de Início"), 0, 6)
        layout_inputs.addWidget(self.data_inicio, 1, 6)

        layout_principal.addLayout(layout_inputs)
        layout_principal.addSpacing(10)

        # Botões de ação: voltar, limpar, calcular e exportar
        botoes_layout = QHBoxLayout()
        btn_limpar = QPushButton("LIMPAR")
        btn_limpar.setStyleSheet("background:#6B7280; color:#fff; padding:10px; font-size:14px; border-radius:6px;")
        btn_limpar.clicked.connect(self.limpar)

        btn_calcular = QPushButton("CALCULAR")
        btn_calcular.setStyleSheet("background:#2563EB; color:#fff; padding:10px; font-size:14px; border-radius:6px;")
        btn_calcular.clicked.connect(self.calcular)

        btn_exportar = QPushButton("EXPORTAR")
        btn_exportar.setStyleSheet("background:#059669; color:#fff; padding:10px; font-size:14px; border-radius:6px;")
        btn_exportar.clicked.connect(self.exportar)

        btn_voltar = QPushButton("VOLTAR")
        btn_voltar.setStyleSheet("background:#4B5563; color:#fff; padding:10px; font-size:14px; border-radius:6px;")
        if self.voltar_callback:
            btn_voltar.clicked.connect(self.voltar_callback)
        else:
            btn_voltar.clicked.connect(self.close)

        botoes_layout.addWidget(btn_voltar)
        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_calcular)
        botoes_layout.addWidget(btn_exportar)
        layout_principal.addLayout(botoes_layout)
        layout_principal.addSpacing(10)

        # Totais
        totais_layout = QHBoxLayout()
        self.total_juros = QLabel("R$ 0.00")
        self.total_investido = QLabel("R$ 0.00")
        self.total_final = QLabel("R$ 0.00")

        self.total_juros.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_investido.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_final.setFont(QFont("Segoe UI", 16, QFont.Bold))

        self.total_juros.setStyleSheet("color:#2563EB;")
        self.total_investido.setStyleSheet("color:#059669;")
        self.total_final.setStyleSheet("color:#7C3AED;")

        bloco_juros = QVBoxLayout()
        bloco_juros.addWidget(QLabel("Total em Juros"))
        bloco_juros.addWidget(self.total_juros)

        bloco_investido = QVBoxLayout()
        bloco_investido.addWidget(QLabel("Valor Total Investido"))
        bloco_investido.addWidget(self.total_investido)

        bloco_final = QVBoxLayout()
        bloco_final.addWidget(QLabel("Valor Total Final"))
        bloco_final.addWidget(self.total_final)

        totais_layout.addLayout(bloco_juros)
        totais_layout.addLayout(bloco_investido)
        totais_layout.addLayout(bloco_final)
        layout_principal.addLayout(totais_layout)
        layout_principal.addSpacing(10)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "Data", "Saldo", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(150)
        self.tabela.setMinimumHeight(180)
        self.tabela.setMaximumHeight(220)
        layout_principal.addWidget(self.tabela)
        layout_principal.addSpacing(10)

        # Gráficos
        self.layout_graficos = QHBoxLayout()
        grafico1 = grafico_evolucao([], [], [])
        grafico2 = grafico_composicao(0, 0)
        grafico1.setMaximumHeight(250)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)
        layout_principal.addLayout(self.layout_graficos)

    def limpar(self):
        """Limpa todos os campos de entrada e reseta o estado da tela."""
        limpar_campos(self)

    def exportar(self):
        """Exporta os dados visíveis na tabela para CSV."""
        exportar_dados(self)

    def calcular(self):
        """Dispara o cálculo do simulador de juros compostos."""
        calcular_juros(self)
