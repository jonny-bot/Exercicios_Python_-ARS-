from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView, QAbstractItemView
)
from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtCore import Qt
from funcoes import exportar_dados, format_currency
from graficos import grafico_evolucao
from tema import aplicar_tema   # usa tema centralizado

# constantes
META_PRIMEIRO_MILHAO = 1_000_000
LIMITE_MESES_SIMULACAO = 2400

class CalculadoraPrimeiroMilhao(QWidget):
    """Tela para cálculo do primeiro milhão."""
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora do Primeiro Milhão")
        self.setGeometry(200, 100, 1100, 750)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(24, 24, 24, 24)
        layout_principal.setSpacing(14)

        titulo = QLabel("CALCULADORA DO PRIMEIRO MILHÃO")
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

        self.validador_numerico = QDoubleValidator(0, 999999999, 2)
        self.validador_numerico.setNotation(QDoubleValidator.StandardNotation)

        for campo in [self.capital_inicial, self.aporte_mensal, self.taxa_juros]:
            campo.setValidator(self.validador_numerico)
            campo.setMinimumHeight(34)
        self.tipo_taxa.setMinimumHeight(34)

        self.capital_inicial.setPlaceholderText("Ex.: 10000")
        self.aporte_mensal.setPlaceholderText("Ex.: 1000")
        self.taxa_juros.setPlaceholderText("Ex.: 0,8")

        layout_inputs.addWidget(QLabel("Capital Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros"), 0, 2)
        layout_inputs.addWidget(self.taxa_juros, 1, 2)
        layout_inputs.addWidget(QLabel("Tipo Taxa"), 0, 3)
        layout_inputs.addWidget(self.tipo_taxa, 1, 3)

        layout_principal.addLayout(layout_inputs)

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
        self.meses_necessarios = QLabel("0 meses")
        self.anos_necessarios = QLabel("0 anos")
        self.meses_necessarios.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.anos_necessarios.setFont(QFont("Segoe UI", 16, QFont.Bold))

        bloco_meses = QVBoxLayout()
        bloco_meses.addWidget(QLabel("Meses Necessários"))
        bloco_meses.addWidget(self.meses_necessarios)

        bloco_anos = QVBoxLayout()
        bloco_anos.addWidget(QLabel("Anos Necessários"))
        bloco_anos.addWidget(self.anos_necessarios)

        totais_layout.addLayout(bloco_meses)
        totais_layout.addLayout(bloco_anos)
        layout_principal.addLayout(totais_layout)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Mês", "Saldo", "Aporte Acumulado", "Juros"])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.setMinimumHeight(150)
        self.tabela.setMaximumHeight(175)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.verticalHeader().setVisible(False)
        layout_principal.addWidget(self.tabela)

        # Gráficos
        self.layout_graficos = QHBoxLayout()
        self._atualizar_grafico([], [], [])
        layout_principal.addLayout(self.layout_graficos)

        # aplica tema inicial
        aplicar_tema(self, self.dark_mode)

    def atualizar_tema(self, dark_mode):
        """Atualiza o tema dinamicamente."""
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)

    def calcular(self):
        try:
            capital = self._ler_valor(self.capital_inicial)
            aporte = self._ler_valor(self.aporte_mensal)
            taxa = self._ler_valor(self.taxa_juros) / 100

            if self.tipo_taxa.currentText() == "Anual":
                taxa = (1 + taxa) ** (1/12) - 1

            if capital >= META_PRIMEIRO_MILHAO:
                self.meses_necessarios.setText("0 meses")
                self.anos_necessarios.setText("0 anos")
                self.tabela.setRowCount(0)
                self._atualizar_grafico([], [], [])
                return

            if aporte <= 0 and taxa <= 0:
                self._mostrar_erro(
                    "Com aporte mensal e taxa zerados, o valor nunca chegará a R$ 1.000.000."
                )
                return

            saldo = capital
            meses = 0
            saldos = []
            juros = []
            self.tabela.setRowCount(0)

            while saldo < META_PRIMEIRO_MILHAO and meses < LIMITE_MESES_SIMULACAO:
                saldo = saldo * (1 + taxa) + aporte
                meses += 1
                saldos.append(saldo)
                juros.append(saldo - (capital + aporte * meses))

                aporte_acumulado = aporte * meses
                row = self.tabela.rowCount()
                self.tabela.insertRow(row)
                itens = [
                    QTableWidgetItem(str(meses)),
                    QTableWidgetItem(format_currency(saldo)),
                    QTableWidgetItem(format_currency(aporte_acumulado)),
                    QTableWidgetItem(format_currency(juros[-1]))
                ]
                for item in itens:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                for col, item in enumerate(itens):
                    self.tabela.setItem(row, col, item)

            if saldo < META_PRIMEIRO_MILHAO:
                self._mostrar_erro(
                    "A simulação passou de 200 anos. Aumente o aporte ou a taxa de juros."
                )
                self._atualizar_grafico(list(range(1, meses + 1)), saldos, juros)
                return

            anos = meses / 12
            self.meses_necessarios.setText(f"{meses} meses")
            self.anos_necessarios.setText(f"{anos:.1f} anos")
            self._atualizar_grafico(list(range(1, meses + 1)), saldos, juros)

        except ValueError:
            self._mostrar_erro("Preencha todos os campos com valores numéricos válidos.")
        except Exception as erro:
            self._mostrar_erro(f"Não foi possível calcular: {erro}")

    def limpar(self):
        self.capital_inicial.clear()
        self.aporte_mensal.clear()
        self.taxa_juros.clear()
        self.tipo_taxa.setCurrentIndex(0)
        self.meses_necessarios.setText("0 meses")
        self.anos_necessarios.setText("0 anos")
        self.tabela.setRowCount(0)
        self._atualizar_grafico([], [], [])

    def _ler_valor(self, campo):
        # ... (função permanece igual)
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

    def _atualizar_grafico(self, meses, saldos, juros):
        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        grafico = grafico_evolucao(meses, saldos, juros)
        grafico.setMinimumHeight(180)
        grafico.setMaximumHeight(240)
        self.layout_graficos.addWidget(grafico)

    def _mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Dados inválidos", mensagem)


PrimeiroMilhao = CalculadoraPrimeiroMilhao
