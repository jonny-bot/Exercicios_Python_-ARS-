from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox, QShortcut,
    QPushButton, QTableWidget, QHBoxLayout, QDateEdit, QHeaderView, QAbstractItemView
)
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt, QDate
from core.graficos import grafico_evolucao, grafico_composicao
from core.funcoes import exportar_dados, format_currency, limpar_campos, validar_e_calcular
from app.tema import aplicar_tema


class SimuladorJuros(QWidget):
    """Tela do simulador de juros compostos."""

    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.graficos_meses = []
        self.graficos_saldos = []
        self.graficos_juros = []
        self.graficos_total_investido = 0.0
        self.graficos_total_juros = 0.0
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
        self.taxa_juros.setPlaceholderText("Ex.: 1.05 %")
        self.taxa_juros.editingFinished.connect(self._formatar_taxa)
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
        layout.addWidget(botao("CALCULAR", "#2563EB", lambda: validar_e_calcular(self)))
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
        tabela.setColumnCount(8)
        tabela.setHorizontalHeaderLabels([
            "Data", "Saldo", "Aporte", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        tabela.setMinimumHeight(220)
        tabela.setMaximumHeight(300)
        tabela.setAlternatingRowColors(True)
        tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        tabela.verticalHeader().setVisible(False)
        tabela.setColumnWidth(0, 80)
        
        header = tabela.horizontalHeader()
        for c in range(8):
            header.setSectionResizeMode(c, QHeaderView.Stretch)
        
        tabela.verticalHeader().setDefaultSectionSize(25)
        tabela.setStyleSheet("""
            QTableWidget {
                gridline-color: #cccccc;
                padding: 5px;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)

        self.tabela = tabela
        return tabela

    def _criar_graficos(self):
        self.layout_graficos = QHBoxLayout()
        grafico1 = grafico_evolucao([], [], [], dark_mode=self.dark_mode)
        grafico2 = grafico_composicao(0, 0, dark_mode=self.dark_mode)
        for g in (grafico1, grafico2):
            g.setMaximumHeight(250)
            self.layout_graficos.addWidget(g)
        return self.layout_graficos

    def _atualizar_grafico(self, meses, saldos, juros):
        self.graficos_meses = meses
        self.graficos_saldos = saldos
        self.graficos_juros = juros

        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        grafico1 = grafico_evolucao(meses, saldos, juros, dark_mode=self.dark_mode)
        grafico1.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)

        grafico2 = grafico_composicao(self.graficos_total_investido, self.graficos_total_juros, dark_mode=self.dark_mode)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico2)

        return self.layout_graficos

    # ---------------- Funções principais ---------------- #

    def atualizar_tema(self, dark_mode):
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)
        self._atualizar_grafico(self.graficos_meses, self.graficos_saldos, self.graficos_juros)

    def _formatar_taxa(self):
        texto = self.taxa_juros.text().strip()
        if not texto:
            return

        s = texto.replace(' ', '')
        try:
            if ',' in s or '.' in s:
                valor = self._ler_valor(self.taxa_juros)
            else:
                if s.isdigit():
                    if len(s) >= 3:
                        valor = int(s) / 100.0
                    else:
                        valor = float(s)
                else:
                    valor = self._ler_valor(self.taxa_juros)
            self.taxa_juros.setText(f"{valor:.2f}")
        except Exception:
            pass

    def _ler_valor(self, campo):
        texto = campo.text().strip().replace(" ", "")
        if not texto:
            raise ValueError

        if "," in texto:
            texto = texto.replace(".", "").replace(",", ".")
        elif texto.count(".") > 1:
            texto = texto.replace(".", "")
        elif "." in texto:
            parte_inteira, parte_decimal = texto.split(".")
            if len(parte_decimal) == 3 and parte_inteira:
                texto = texto.replace(".", "")

        return float(texto)

    def limpar(self):
        limpar_campos(self)

    def exportar(self):
        exportar_dados(self)

    def calcular(self):
        calcular_juros(self)
