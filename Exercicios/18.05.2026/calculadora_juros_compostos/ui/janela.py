from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHeaderView,
    QScrollArea,
    QFileDialog
)

from PySide6.QtCore import Qt

from core.calculos import (
    calcular_simulacao
)

from core.formatacao import (
    formatar_moeda
)

from ui.card import Card

from exports.exportador import (
    exportar_csv,
    exportar_excel,
    exportar_json
)


class Janela(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Calculadora Financeira"
        )

        self.resize(1750, 950)

        self.setStyleSheet("""
            QWidget {
                background-color: #0F172A;
                color: white;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLineEdit, QComboBox {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 12px;
                padding: 10px;
                min-height: 26px;
                font-size: 15px;
                color: white;
            }

            QComboBox::drop-down {
                border: none;
                width: 40px;
                background: transparent;
            }

            QComboBox::down-arrow {
                image: none;
                width: 0px;
                height: 0px;

                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 8px solid #CBD5E1;

                margin-right: 15px;
            }

            QLineEdit:focus,
            QComboBox:focus {
                border: 1px solid #3B82F6;
            }

            QPushButton {
                background-color: #1D4ED8;
                border: none;
                border-radius: 10px;
                padding: 12px;
                min-width: 180px;
                font-size: 15px;
                color: white;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #3B82F6;
            }

            QTableWidget {
                background-color: #111827;
                alternate-background-color: #172036;
                selection-background-color: #2563EB;
                selection-color: white;
                color: white;
                border-radius: 14px;
                gridline-color: #1E293B;
                padding: 10px;
            }

            QHeaderView::section {
                background-color: #1E293B;
                padding: 12px;
                border: none;
                font-weight: bold;
            }
        """)

        self.historico_atual = []

        container = QWidget()

        main_layout = QVBoxLayout(container)

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        main_layout.setSpacing(25)

        titulo = QLabel(
            "Calculadora de Juros Compostos"
        )

        titulo.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
        """)

        main_layout.addWidget(titulo)

        # PAINEL INPUTS

        painel = QFrame()

        painel.setStyleSheet("""
            background-color: #111827;
            border-radius: 14px;
        """)

        grid = QGridLayout()

        grid.setContentsMargins(
            20,
            20,
            20,
            20
        )

        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(15)

        self.valor_inicial = QLineEdit()
        self.valor_inicial.setPlaceholderText(
            "1000"
        )

        self.aporte = QLineEdit()
        self.aporte.setPlaceholderText(
            "100"
        )

        self.rendimento = QLineEdit()
        self.rendimento.setPlaceholderText(
            "12"
        )

        self.tempo = QLineEdit()
        self.tempo.setPlaceholderText(
            "20"
        )

        self.tipo_taxa = QComboBox()

        self.tipo_taxa.addItems([
            "mensal",
            "anual"
        ])

        self.tipo_tempo = QComboBox()

        self.tipo_tempo.addItems([
            "meses",
            "anos"
        ])

        campos = [
            ("Valor Inicial", self.valor_inicial),
            ("Aporte Mensal", self.aporte),
            ("Rendimento (%)", self.rendimento),
            ("Tipo Taxa", self.tipo_taxa),
            ("Tempo", self.tempo),
            ("Tipo Tempo", self.tipo_tempo),
        ]

        coluna = 0

        for texto, widget in campos:

            label = QLabel(texto)

            label.setStyleSheet("""
                color: #CBD5E1;
                font-size: 13px;
                font-weight: bold;
            """)

            grid.addWidget(
                label,
                0,
                coluna
            )

            grid.addWidget(
                widget,
                1,
                coluna
            )

            coluna += 1

        painel.setLayout(grid)

        main_layout.addWidget(painel)

        # CARDS

        cards = QHBoxLayout()

        cards.setSpacing(12)

        self.card_final = Card(
            "SALDO FINAL",
            cor="#22C55E"
        )

        self.card_investido = Card(
            "TOTAL INVESTIDO",
            cor="#3B82F6"
        )

        self.card_juros = Card(
            "JUROS LÍQUIDOS",
            cor="#EAB308"
        )

        self.card_ir = Card(
            "IR TOTAL",
            cor="#EF4444"
        )

        self.card_media = Card(
            "RENDIMENTO FINAL",
            cor="#8B5CF6"
        )

        cards.addWidget(self.card_final)

        cards.addWidget(
            self.card_investido
        )

        cards.addWidget(
            self.card_juros
        )

        cards.addWidget(
            self.card_ir
        )

        cards.addWidget(
            self.card_media
        )

        main_layout.addLayout(cards)

        # BOTÕES EXPORTAÇÃO

        botoes = QHBoxLayout()

        self.btn_excel = QPushButton(
            "Exportar Excel"
        )

        self.btn_csv = QPushButton(
            "Exportar CSV"
        )

        self.btn_json = QPushButton(
            "Exportar JSON"
        )

        botoes.addWidget(
            self.btn_excel
        )

        botoes.addWidget(
            self.btn_csv
        )

        botoes.addWidget(
            self.btn_json
        )

        botoes.addStretch()

        main_layout.addLayout(botoes)

        # TABELA

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(7)

        self.tabela.setHorizontalHeaderLabels([
            "Mês",
            "Saldo Inicial",
            "Base Cálculo",
            "Rendimento Bruto",
            "IR",
            "Rendimento Líquido",
            "Saldo Final"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabela.verticalHeader().setVisible(
            False
        )

        self.tabela.setAlternatingRowColors(
            True
        )

        self.tabela.setMinimumHeight(500)

        main_layout.addWidget(
            self.tabela
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setWidget(container)

        scroll.setFrameShape(QFrame.NoFrame)

        layout_principal = QVBoxLayout()

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.addWidget(scroll)

        self.setLayout(layout_principal)

        # EVENTOS

        self.valor_inicial.textChanged.connect(
            self.calcular
        )

        self.aporte.textChanged.connect(
            self.calcular
        )

        self.rendimento.textChanged.connect(
            self.calcular
        )

        self.tempo.textChanged.connect(
            self.calcular
        )

        self.tipo_taxa.currentTextChanged.connect(
            self.calcular
        )

        self.tipo_tempo.currentTextChanged.connect(
            self.calcular
        )

        self.btn_excel.clicked.connect(
            self.exportar_excel
        )

        self.btn_csv.clicked.connect(
            self.exportar_csv
        )

        self.btn_json.clicked.connect(
            self.exportar_json
        )

    def calcular(self):

        try:

            resultado = calcular_simulacao(

                valor_inicial=float(
                    self.valor_inicial.text()
                ),

                aporte=float(
                    self.aporte.text()
                ),

                rendimento=float(
                    self.rendimento.text()
                ),

                tipo_taxa=self.tipo_taxa.currentText(),

                tempo=int(
                    self.tempo.text()
                ),

                tipo_tempo=self.tipo_tempo.currentText()
            )

        except:
            return

        self.card_final.atualizar(
            formatar_moeda(
                resultado["saldo_final"]
            )
        )

        self.card_investido.atualizar(
            formatar_moeda(
                resultado["total_investido"]
            )
        )

        self.card_juros.atualizar(
            formatar_moeda(
                resultado["total_juros"]
            )
        )

        self.card_ir.atualizar(
            formatar_moeda(
                resultado["total_ir"]
            )
        )

        self.card_media.atualizar(
            formatar_moeda(
                resultado[
                    "ultimo_rendimento"
                ]
            )
        )

        historico = resultado["historico"]

        self.historico_atual = historico

        self.tabela.setRowCount(
            len(historico)
        )

        for linha, item in enumerate(historico):

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    str(item["mes"])
                )
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    formatar_moeda(
                        item["saldo_inicial"]
                    )
                )
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(
                    formatar_moeda(
                        item["base_calculo"]
                    )
                )
            )

            self.tabela.setItem(
                linha,
                3,
                QTableWidgetItem(
                    formatar_moeda(
                        item["rendimento_bruto"]
                    )
                )
            )

            self.tabela.setItem(
                linha,
                4,
                QTableWidgetItem(
                    formatar_moeda(
                        item["ir"]
                    )
                )
            )

            self.tabela.setItem(
                linha,
                5,
                QTableWidgetItem(
                    formatar_moeda(
                        item["rendimento_liquido"]
                    )
                )
            )

            self.tabela.setItem(
                linha,
                6,
                QTableWidgetItem(
                    formatar_moeda(
                        item["saldo_final"]
                    )
                )
            )

    def exportar_excel(self):

        if not self.historico_atual:
            return

        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Excel",
            "juros_compostos.xlsx",
            "Excel (*.xlsx)"
        )

        if caminho:

            exportar_excel(
                self.historico_atual,
                caminho
            )

    def exportar_csv(self):

        if not self.historico_atual:
            return

        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar CSV",
            "juros_compostos.csv",
            "CSV (*.csv)"
        )

        if caminho:

            exportar_csv(
                self.historico_atual,
                caminho
            )

    def exportar_json(self):

        if not self.historico_atual:
            return

        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar JSON",
            "juros_compostos.json",
            "JSON (*.json)"
        )

        if caminho:

            exportar_json(
                self.historico_atual,
                caminho
            )
            