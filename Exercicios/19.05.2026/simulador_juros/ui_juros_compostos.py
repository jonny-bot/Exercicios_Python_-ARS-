from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QHBoxLayout, QTableWidget, QSizePolicy, QScrollArea
)
from PyQt5.QtCore import Qt
from calculos import calcular_juros
from exportacao import exportar_dados
from util import criar_card, limpar_campos
from graficos import grafico_evolucao, grafico_composicao
from config import GEOMETRIA
from tema import aplicar_tema_claro, get_fonte
from estilos import criar_botao_estilizado, CAMPO_TEXTO
from validadores import ValidadorMonetario, ValidadorTaxa, ValidadorMeses

class SimuladorJuros(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Juros Compostos")
        x, y, width, height = GEOMETRIA["janela_grande"]
        self.setGeometry(x, y, width, height)

        # Aplicar tema
        aplicar_tema_claro(self)

        # Scroll geral
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        conteudo = QWidget()
        layout_principal = QVBoxLayout(conteudo)

        # Título
        titulo = QLabel("SIMULADOR DE JUROS COMPOSTOS")
        titulo.setFont(get_fonte("titulo_grande"))
        layout_principal.addWidget(titulo)

        # Entradas
        layout_inputs = QGridLayout()
        self.valor_inicial = QLineEdit()
        self.valor_inicial.setValidator(ValidadorMonetario())
        self.valor_inicial.setStyleSheet(CAMPO_TEXTO)
        self.valor_inicial.setMinimumHeight(34)
        
        self.aporte_mensal = QLineEdit()
        self.aporte_mensal.setValidator(ValidadorMonetario())
        self.aporte_mensal.setStyleSheet(CAMPO_TEXTO)
        self.aporte_mensal.setMinimumHeight(34)
        
        self.taxa_juros = QLineEdit()
        self.taxa_juros.setValidator(ValidadorTaxa())
        self.taxa_juros.setStyleSheet(CAMPO_TEXTO)
        self.taxa_juros.setMinimumHeight(34)
        
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])
        
        self.tempo = QLineEdit()
        self.tempo.setValidator(ValidadorMeses())
        self.tempo.setStyleSheet(CAMPO_TEXTO)
        self.tempo.setMinimumHeight(34)
        
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Meses", "Anos"])
        
        self.data_inicio = QLineEdit()
        self.data_inicio.setPlaceholderText("dd/mm/aaaa (ou deixe em branco para hoje)")
        self.data_inicio.setStyleSheet(CAMPO_TEXTO)
        self.data_inicio.setMinimumHeight(34)

        layout_inputs.addWidget(QLabel("Valor Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.valor_inicial, 1, 0)
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

        # Botões
        layout_botoes = QHBoxLayout()
        btn_voltar = criar_botao_estilizado("VOLTAR", "secundario")
        btn_limpar = criar_botao_estilizado("LIMPAR", "outline")
        btn_calcular = criar_botao_estilizado("CALCULAR", "primario")
        btn_exportar = criar_botao_estilizado("EXPORTAR", "sucesso")

        btn_voltar.clicked.connect(self.close)
        btn_limpar.clicked.connect(self.limpar)
        btn_calcular.clicked.connect(self.calcular)
        btn_exportar.clicked.connect(self.exportar)

        layout_botoes.addWidget(btn_voltar)
        layout_botoes.addWidget(btn_limpar)
        layout_botoes.addWidget(btn_calcular)
        layout_botoes.addWidget(btn_exportar)
        layout_principal.addLayout(layout_botoes)

        # Cards
        layout_resultados = QHBoxLayout()
        self.card_juros = criar_card("Total em Juros", "#2563EB")
        self.card_investido = criar_card("Valor Total Investido", "#059669")
        self.card_final = criar_card("Valor Total Final", "#7C3AED")

        layout_resultados.addWidget(self.card_juros)
        layout_resultados.addWidget(self.card_investido)
        layout_resultados.addWidget(self.card_final)
        layout_principal.addLayout(layout_resultados)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "Mês", "Saldo", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(150)

        # Exibir apenas 4 linhas visíveis e scrolls
        self.tabela.setMinimumHeight(160)
        self.tabela.setMaximumHeight(220)  # ← altura ajustada
        self.tabela.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tabela.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        layout_principal.addWidget(self.tabela)
        layout_principal.addSpacing(10)  # ← espaçamento entre tabela e gráficos

        # Área de gráficos menores
        self.layout_graficos = QHBoxLayout()

        meses_padrao = ["Mai/2026", "Jun/2026", "Jul/2026", "Ago/2026", "Set/2026"]
        saldos_padrao = [0, 0, 0, 0, 0]
        juros_padrao = [0, 0, 0, 0, 0]

        grafico1 = grafico_evolucao(meses_padrao, saldos_padrao, juros_padrao)
        grafico2 = grafico_composicao(0, 0)

        # Limitar altura dos gráficos
        grafico1.setMaximumHeight(220)
        grafico2.setMaximumHeight(220)

        self.layout_graficos.setSpacing(20)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)

        layout_principal.addLayout(self.layout_graficos)

        # Adiciona scroll geral
        scroll_area.setWidget(conteudo)
        layout_scroll = QVBoxLayout()
        layout_scroll.addWidget(scroll_area)
        self.setLayout(layout_scroll)

    def limpar(self):
        limpar_campos(self)

    def exportar(self):
        exportar_dados(self)

    def calcular(self):
        calcular_juros(self)

    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().show()
        super().closeEvent(event)
