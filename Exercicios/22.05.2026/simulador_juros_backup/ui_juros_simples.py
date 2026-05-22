from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView
)
from PyQt5.QtGui import QFont, QColor, QPalette, QDoubleValidator, QIntValidator
from PyQt5.QtCore import Qt
from graficos import grafico_evolucao
from funcoes import exportar_dados

class JurosSimples(QWidget):
    """Tela para cálculo de juros simples.

    Captura capital, taxa e tempo e mostra a evolução mês a mês.
    """
    def __init__(self, voltar_callback=None):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora de Juros Simples")
        self.setGeometry(200, 100, 1100, 750)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(24, 24, 24, 24)
        layout_principal.setSpacing(14)

        titulo = QLabel("CALCULADORA DE JUROS SIMPLES")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:10px;")
        layout_principal.addWidget(titulo)

        layout_inputs = QGridLayout()
        layout_inputs.setHorizontalSpacing(14)
        layout_inputs.setVerticalSpacing(8)

        self.capital = QLineEdit()
        self.taxa = QLineEdit()
        self.tempo = QLineEdit()

        self.valor_validator = QDoubleValidator(0, 999999999, 2)
        self.valor_validator.setNotation(QDoubleValidator.StandardNotation)
        self.tempo_validator = QIntValidator(1, 1200)

        for campo in [self.capital, self.taxa]:
            campo.setValidator(self.valor_validator)
            campo.setMinimumHeight(34)
            campo.setStyleSheet(
                "padding:6px; border:1px solid #D1D5DB; border-radius:6px; background:#FFFFFF;"
            )

        self.tempo.setValidator(self.tempo_validator)
        self.tempo.setMinimumHeight(34)
        self.tempo.setStyleSheet(
            "padding:6px; border:1px solid #D1D5DB; border-radius:6px; background:#FFFFFF;"
        )

        self.capital.setPlaceholderText("Ex.: 10000")
        self.taxa.setPlaceholderText("Ex.: 1,5")
        self.tempo.setPlaceholderText("Ex.: 12")

        layout_inputs.addWidget(QLabel("Capital (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital, 1, 0)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 1)
        layout_inputs.addWidget(self.taxa, 1, 1)
        layout_inputs.addWidget(QLabel("Tempo (meses)"), 0, 2)
        layout_inputs.addWidget(self.tempo, 1, 2)

        layout_principal.addLayout(layout_inputs)
        layout_principal.addSpacing(10)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(10)

        btn_limpar = QPushButton("LIMPAR")
        btn_limpar.setCursor(Qt.PointingHandCursor)
        btn_limpar.setStyleSheet(
            "background:#6B7280; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_limpar.clicked.connect(self.limpar)

        btn_calcular = QPushButton("CALCULAR")
        btn_calcular.setCursor(Qt.PointingHandCursor)
        btn_calcular.setStyleSheet(
            "background:#2563EB; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_calcular.clicked.connect(self.calcular)

        btn_exportar = QPushButton("EXPORTAR")
        btn_exportar.setCursor(Qt.PointingHandCursor)
        btn_exportar.setStyleSheet(
            "background:#059669; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        btn_exportar.clicked.connect(lambda: exportar_dados(self))

        btn_voltar = QPushButton("VOLTAR")
        btn_voltar.setCursor(Qt.PointingHandCursor)
        btn_voltar.setStyleSheet(
            "background:#4B5563; color:#fff; padding:10px; font-size:14px; border-radius:6px;"
        )
        if self.voltar_callback:
            btn_voltar.clicked.connect(self.voltar_callback)
        else:
            btn_voltar.clicked.connect(self.close)

        botoes_layout.addWidget(btn_voltar)
        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_calcular)
        botoes_layout.addWidget(btn_exportar)
        layout_principal.addLayout(botoes_layout)

        totais_layout = QHBoxLayout()
        totais_layout.setSpacing(24)

        self.total_juros = QLabel("R$ 0,00")
        self.total_final = QLabel("R$ 0,00")

        self.total_juros.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_final.setFont(QFont("Segoe UI", 16, QFont.Bold))

        self.total_juros.setStyleSheet("color:#2563EB;")
        self.total_final.setStyleSheet("color:#7C3AED;")

        bloco_juros = QVBoxLayout()
        bloco_juros.addWidget(QLabel("Total em Juros"))
        bloco_juros.addWidget(self.total_juros)

        bloco_final = QVBoxLayout()
        bloco_final.addWidget(QLabel("Valor Total Final"))
        bloco_final.addWidget(self.total_final)

        totais_layout.addLayout(bloco_juros)
        totais_layout.addLayout(bloco_final)
        layout_principal.addLayout(totais_layout)
        layout_principal.addSpacing(10)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        # cabeçalhos e ajuste de largura para preencher a área disponível
        self.tabela.setHorizontalHeaderLabels(["Mês", "Capital", "Juros", "Montante"])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.horizontalHeader().setDefaultSectionSize(150)
        self.tabela.verticalHeader().setDefaultSectionSize(32)
        self.tabela.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela.setMinimumHeight(150)
        self.tabela.setMaximumHeight(175)
        layout_principal.addWidget(self.tabela)

        self.layout_graficos = QHBoxLayout()
        grafico = grafico_evolucao([], [], [])
        grafico.setMinimumHeight(180)
        grafico.setMaximumHeight(240)
        self.layout_graficos.addWidget(grafico)
        layout_principal.addLayout(self.layout_graficos)

    def calcular(self):
        """Executa o cálculo de juros simples e atualiza tabela e gráfico."""
        try:
            capital = self._ler_valor(self.capital)
            taxa = self._ler_valor(self.taxa)
            tempo = int(self.tempo.text())

            if tempo <= 0:
                raise ValueError

            self.tabela.setRowCount(0)
            montante = capital
            total_juros = 0
            meses = []
            saldos = []
            juros = []

            for mes in range(1, tempo + 1):
                juro_mes = capital * (taxa / 100)
                montante = capital + juro_mes * mes
                total_juros = juro_mes * mes

                row = self.tabela.rowCount()
                self.tabela.insertRow(row)
                itens = [
                    QTableWidgetItem(str(mes)),
                    QTableWidgetItem(f"R$ {capital:,.2f}"),
                    QTableWidgetItem(f"R$ {juro_mes:,.2f}"),
                    QTableWidgetItem(f"R$ {montante:,.2f}")
                ]
                for item in itens:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                for col, item in enumerate(itens):
                    self.tabela.setItem(row, col, item)

                meses.append(mes)
                saldos.append(montante)
                juros.append(total_juros)

            self.total_juros.setText(f"R$ {total_juros:,.2f}")
            self.total_final.setText(f"R$ {montante:,.2f}")

            for i in reversed(range(self.layout_graficos.count())):
                widget = self.layout_graficos.itemAt(i).widget()
                if widget:
                    widget.setParent(None)
            grafico = grafico_evolucao(meses, saldos, juros)
            grafico.setMinimumHeight(180)
            grafico.setMaximumHeight(240)
            self.layout_graficos.addWidget(grafico)

        except ValueError:
            self._mostrar_erro("Preencha todos os campos com valores numéricos válidos.")
        except Exception as e:
            self._mostrar_erro(f"Erro no cálculo de juros simples: {e}")

    def limpar(self):
        self.capital.clear()
        self.taxa.clear()
        self.tempo.clear()
        self.total_juros.setText("R$ 0,00")
        self.total_final.setText("R$ 0,00")
        self.tabela.setRowCount(0)
        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        grafico = grafico_evolucao([], [], [])
        grafico.setMinimumHeight(180)
        grafico.setMaximumHeight(240)
        self.layout_graficos.addWidget(grafico)

    def _ler_valor(self, campo):
        """Recebe texto de um QLineEdit e transforma em float.

        Suporta entrada com vírgula decimal e remove formatação de milhar.
        """
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

    def _mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Dados inválidos", mensagem)


CalculadoraJurosSimples = JurosSimples
