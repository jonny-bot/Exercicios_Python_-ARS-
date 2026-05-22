from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QTableWidget, QHBoxLayout, QDateEdit, QHeaderView, QAbstractItemView
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate
from graficos import grafico_evolucao, grafico_composicao
from funcoes import calcular_juros, limpar_campos, exportar_dados
from tema import aplicar_tema   # usa tema centralizado

class SimuladorJuros(QWidget):
    """Tela do simulador de juros compostos."""
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Juros Compostos")
        self.setGeometry(200, 100, 1100, 750)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)

        # Título
        titulo = QLabel("SIMULADOR DE JUROS COMPOSTOS")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
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

        # Botões
        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(10)

        def estilizar_botao(botao, cor):
            botao.setCursor(Qt.PointingHandCursor)
            botao.setFixedHeight(40)
            botao.setStyleSheet(f"""
                QPushButton {{
                    background:{cor};
                    color:#fff;
                    font-size:14px;
                    font-weight:500;
                    border:none;
                    border-radius:6px;
                    padding:10px 16px;
                }}
                QPushButton:hover {{
                    background-color:#333333;
                }}
            """)

        btn_voltar = QPushButton("VOLTAR")
        estilizar_botao(btn_voltar, "#4B5563")
        if self.voltar_callback:
            btn_voltar.clicked.connect(self.voltar_callback)
        else:
            btn_voltar.clicked.connect(self.close)

        btn_limpar = QPushButton("LIMPAR")
        estilizar_botao(btn_limpar, "#6B7280")
        btn_limpar.clicked.connect(self.limpar)

        btn_calcular = QPushButton("CALCULAR")
        estilizar_botao(btn_calcular, "#2563EB")
        btn_calcular.clicked.connect(self.calcular)

        btn_exportar = QPushButton("EXPORTAR")
        estilizar_botao(btn_exportar, "#059669")
        btn_exportar.clicked.connect(lambda: exportar_dados(self))

        botoes_layout.addWidget(btn_voltar)
        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_calcular)
        botoes_layout.addWidget(btn_exportar)
        layout_principal.addLayout(botoes_layout)

        # Totais
        totais_layout = QHBoxLayout()
        self.total_juros = QLabel("R$ 0.00")
        self.total_investido = QLabel("R$ 0.00")
        self.total_final = QLabel("R$ 0.00")

        self.total_juros.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_investido.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_final.setFont(QFont("Segoe UI", 16, QFont.Bold))

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

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "Data", "Saldo", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        self.tabela.setMinimumHeight(180)
        self.tabela.setMaximumHeight(220)

        # Melhorias de usabilidade: linhas alternadas, seleção por linha,
        # proibição de edição direta e ocultar cabeçalho vertical.
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.verticalHeader().setVisible(False)

        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for c in range(1, 7):
            header.setSectionResizeMode(c, QHeaderView.Stretch)
        layout_principal.addWidget(self.tabela)

        # Gráficos
        self.layout_graficos = QHBoxLayout()
        grafico1 = grafico_evolucao([], [], [])
        grafico2 = grafico_composicao(0, 0)
        grafico1.setMaximumHeight(250)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)
        layout_principal.addLayout(self.layout_graficos)

        # Aplica tema inicial
        aplicar_tema(self, self.dark_mode)

    def atualizar_tema(self, dark_mode):
        """Atualiza o tema dinamicamente."""
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)

    def limpar(self):
        limpar_campos(self)

    def exportar(self):
        exportar_dados(self)

    def calcular(self):
        calcular_juros(self)
