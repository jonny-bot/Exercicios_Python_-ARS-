from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QTableWidget, QHBoxLayout, QDateEdit, QHeaderView, QAbstractItemView
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDate
from graficos import grafico_evolucao, grafico_composicao
from funcoes import calcular_juros, limpar_campos, exportar_dados
from tema import aplicar_tema


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
        layout_principal.addLayout(self._criar_inputs())
        layout_principal.addSpacing(10)

        # Botões
        layout_principal.addLayout(self._criar_botoes())

        # Totais
        layout_principal.addLayout(self._criar_totais())

        # Tabela
        layout_principal.addWidget(self._criar_tabela())

        # Gráficos
        layout_principal.addLayout(self._criar_graficos())

        # Aplica tema inicial
        aplicar_tema(self, self.dark_mode)

    # ---------------- Métodos auxiliares ---------------- #

    def _criar_inputs(self):
        layout = QGridLayout()

        self.capital_inicial = QLineEdit()
        self.aporte_mensal = QLineEdit()
        self.taxa_juros = QLineEdit()
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])
        self.tempo = QLineEdit()
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Anos", "Meses"])
        self.data_inicio = QDateEdit()
        self.data_inicio.setDisplayFormat("dd/MM/yyyy")
        self.data_inicio.setDate(QDate.currentDate())

        campos = [
            ("Valor Inicial (R$)", self.capital_inicial, 0),
            ("Aporte Mensal (R$)", self.aporte_mensal, 1),
            ("Taxa de Juros (%)", self.taxa_juros, 2),
            ("Tempo", self.tempo, 4),
            ("Data de Início", self.data_inicio, 6),
        ]

        for label, widget, col in campos:
            layout.addWidget(QLabel(label), 0, col)
            layout.addWidget(widget, 1, col)

        layout.addWidget(self.tipo_taxa, 1, 3)
        layout.addWidget(self.tipo_tempo, 1, 5)

        return layout

    def _criar_botoes(self):
        layout = QHBoxLayout()
        layout.setSpacing(10)

        def botao(texto, cor, callback):
            btn = QPushButton(texto)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(40)
            btn.setStyleSheet(f"""
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
            btn.clicked.connect(callback)
            return btn

        layout.addWidget(botao("VOLTAR", "#4B5563", self.voltar_callback or self.close))
        layout.addWidget(botao("LIMPAR", "#6B7280", self.limpar))
        layout.addWidget(botao("CALCULAR", "#2563EB", self.calcular))
        layout.addWidget(botao("EXPORTAR", "#059669", lambda: exportar_dados(self)))

        return layout

    def _criar_totais(self):
        layout = QHBoxLayout()
        self.total_juros = QLabel("R$ 0.00")
        self.total_investido = QLabel("R$ 0.00")
        self.total_final = QLabel("R$ 0.00")

        for lbl in [self.total_juros, self.total_investido, self.total_final]:
            lbl.setFont(QFont("Segoe UI", 16, QFont.Bold))

        blocos = [
            ("Total em Juros", self.total_juros),
            ("Valor Total Investido", self.total_investido),
            ("Valor Total Final", self.total_final),
        ]

        for titulo, valor in blocos:
            bloco = QVBoxLayout()
            bloco.addWidget(QLabel(titulo))
            bloco.addWidget(valor)
            layout.addLayout(bloco)

        return layout

    def _criar_tabela(self):
        tabela = QTableWidget()
        tabela.setColumnCount(7)
        tabela.setHorizontalHeaderLabels([
            "Data", "Saldo", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        tabela.setMinimumHeight(180)
        tabela.setMaximumHeight(220)
        tabela.setAlternatingRowColors(True)
        tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        tabela.verticalHeader().setVisible(False)

        header = tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for c in range(1, 7):
            header.setSectionResizeMode(c, QHeaderView.Stretch)

        self.tabela = tabela
        return tabela

    def _criar_graficos(self):
        self.layout_graficos = QHBoxLayout()
        grafico1 = grafico_evolucao([], [], [])
        grafico2 = grafico_composicao(0, 0)
        for g in (grafico1, grafico2):
            g.setMaximumHeight(250)
            self.layout_graficos.addWidget(g)
        return self.layout_graficos

    # ---------------- Funções principais ---------------- #

    def atualizar_tema(self, dark_mode):
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)

    def limpar(self):
        limpar_campos(self)

    def exportar(self):
        exportar_dados(self)

    def calcular(self):
        calcular_juros(self)
