from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit,
    QPushButton, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QFont, QColor, QPalette, QDoubleValidator
from PyQt5.QtCore import Qt
from graficos import grafico_evolucao
from funcoes import exportar_dados

META_PRIMEIRO_MILHAO = 1_000_000
LIMITE_MESES_SIMULACAO = 2400


class PrimeiroMilhao(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora do Primeiro Milhão")
        self.setGeometry(200, 100, 1100, 750)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(24, 24, 24, 24)
        layout_principal.setSpacing(14)

        titulo = QLabel("CALCULADORA DO PRIMEIRO MILHÃO")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:10px;")
        layout_principal.addWidget(titulo)

        layout_inputs = QGridLayout()
        layout_inputs.setHorizontalSpacing(14)
        layout_inputs.setVerticalSpacing(8)

        self.capital_inicial = QLineEdit()
        self.aporte_mensal = QLineEdit()
        self.taxa_juros = QLineEdit()

        self.validador_numerico = QDoubleValidator(0, 999999999, 2)
        self.validador_numerico.setNotation(QDoubleValidator.StandardNotation)

        for campo in [self.capital_inicial, self.aporte_mensal, self.taxa_juros]:
            campo.setValidator(self.validador_numerico)
            campo.setMinimumHeight(34)
            campo.setStyleSheet(
                "padding:6px; border:1px solid #D1D5DB; border-radius:6px; background:#FFFFFF;"
            )

        self.capital_inicial.setPlaceholderText("Ex.: 10000")
        self.aporte_mensal.setPlaceholderText("Ex.: 1000")
        self.taxa_juros.setPlaceholderText("Ex.: 0,8")

        layout_inputs.addWidget(QLabel("Capital Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros (% ao mês)"), 0, 2)
        layout_inputs.addWidget(self.taxa_juros, 1, 2)

        layout_principal.addLayout(layout_inputs)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(10)

        btn_calcular = QPushButton("CALCULAR")
        btn_calcular.setCursor(Qt.PointingHandCursor)
        btn_calcular.setStyleSheet(
            "background:#2563EB; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_calcular.clicked.connect(self.calcular)

        btn_limpar = QPushButton("LIMPAR")
        btn_limpar.setCursor(Qt.PointingHandCursor)
        btn_limpar.setStyleSheet(
            "background:#6B7280; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_limpar.clicked.connect(self.limpar)

        btn_exportar = QPushButton("EXPORTAR")
        btn_exportar.setCursor(Qt.PointingHandCursor)
        btn_exportar.setStyleSheet(
            "background:#059669; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_exportar.clicked.connect(lambda: exportar_dados(self))

        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_calcular)
        botoes_layout.addWidget(btn_exportar)
        layout_principal.addLayout(botoes_layout)

        totais_layout = QHBoxLayout()
        totais_layout.setSpacing(24)

        self.meses_necessarios = QLabel("0 meses")
        self.anos_necessarios = QLabel("0 anos")

        self.meses_necessarios.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.anos_necessarios.setFont(QFont("Segoe UI", 16, QFont.Bold))

        self.meses_necessarios.setStyleSheet("color:#2563EB;")
        self.anos_necessarios.setStyleSheet("color:#7C3AED;")

        bloco_meses = QVBoxLayout()
        bloco_meses.addWidget(QLabel("Meses Necessários"))
        bloco_meses.addWidget(self.meses_necessarios)

        bloco_anos = QVBoxLayout()
        bloco_anos.addWidget(QLabel("Anos Necessários"))
        bloco_anos.addWidget(self.anos_necessarios)

        totais_layout.addLayout(bloco_meses)
        totais_layout.addLayout(bloco_anos)
        layout_principal.addLayout(totais_layout)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Mês", "Saldo", "Aporte Acumulado", "Juros"])
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(150)
        self.tabela.setMinimumHeight(220)
        self.tabela.setMaximumHeight(250)
        layout_principal.addWidget(self.tabela)

        self.layout_graficos = QHBoxLayout()
        self._atualizar_grafico([], [], [])
        layout_principal.addLayout(self.layout_graficos)

    def calcular(self):
        try:
            capital = self._ler_valor(self.capital_inicial)
            aporte = self._ler_valor(self.aporte_mensal)
            taxa = self._ler_valor(self.taxa_juros) / 100

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
                    QTableWidgetItem(f"R$ {saldo:,.2f}"),
                    QTableWidgetItem(f"R$ {aporte_acumulado:,.2f}"),
                    QTableWidgetItem(f"R$ {juros[-1]:,.2f}")
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
        self.meses_necessarios.setText("0 meses")
        self.anos_necessarios.setText("0 anos")
        self.tabela.setRowCount(0)
        self._atualizar_grafico([], [], [])

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

    def _atualizar_grafico(self, meses, saldos, juros):
        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        grafico = grafico_evolucao(meses, saldos, juros)
        grafico.setMaximumHeight(300)
        self.layout_graficos.addWidget(grafico)

    def _mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Dados inválidos", mensagem)


CalculadoraPrimeiroMilhao = PrimeiroMilhao
