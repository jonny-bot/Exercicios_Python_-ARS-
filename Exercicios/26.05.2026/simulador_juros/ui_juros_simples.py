from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView, QAbstractItemView, QDateEdit
)
from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator
from PyQt5.QtCore import Qt, QDate
from graficos import grafico_evolucao, grafico_composicao
from funcoes import exportar_dados, format_currency
from tema import aplicar_tema   # usa tema centralizado

class JurosSimples(QWidget):
    """Tela para cálculo de juros simples."""
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora de Juros Simples")
        self.setGeometry(200, 100, 1100, 750)
        self.setFont(QFont("Segoe UI", 11))

        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(24, 24, 24, 24)
        layout_principal.setSpacing(14)

        titulo = QLabel("CALCULADORA DE JUROS SIMPLES")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(titulo)

        # Entradas
        layout_inputs = QGridLayout()
        self.capital = QLineEdit()
        self.taxa = QLineEdit()
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])
        self.tempo = QLineEdit()
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Meses", "Anos"])
        self.data_inicio = QDateEdit()
        self.data_inicio.setDisplayFormat("dd/MM/yyyy")
        self.data_inicio.setDate(QDate.currentDate())
        # tipo_tempo já criado acima; não recriar aqui

        self.valor_validator = QDoubleValidator(0, 999999999, 2)
        self.tempo_validator = QIntValidator(1, 1200)

        self.capital.setValidator(self.valor_validator)
        self.taxa.setValidator(self.valor_validator)
        self.tempo.setValidator(self.tempo_validator)

        self.tipo_taxa.setFixedWidth(120)
        self.tempo.setFixedWidth(105)
        self.tipo_tempo.setFixedWidth(110)
        self.data_inicio.setFixedWidth(140)

        layout_inputs.addWidget(QLabel("Capital (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital, 1, 0)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 1)
        layout_inputs.addWidget(self.taxa, 1, 1)
        layout_inputs.addWidget(QLabel("Tipo Taxa"), 0, 2)
        layout_inputs.addWidget(self.tipo_taxa, 1, 2)
        layout_inputs.addWidget(QLabel("Tempo"), 0, 3)
        layout_inputs.addWidget(self.tempo, 1, 3)
        layout_inputs.addWidget(QLabel("Tipo Tempo"), 0, 4)
        layout_inputs.addWidget(self.tipo_tempo, 1, 4)
        layout_inputs.addWidget(QLabel("Data de Início"), 0, 5)
        layout_inputs.addWidget(self.data_inicio, 1, 5)

        # Distribui colunas com mais espaço para os campos principais
        layout_inputs.setColumnStretch(0, 2)
        layout_inputs.setColumnStretch(1, 2)
        layout_inputs.setColumnStretch(2, 1)
        layout_inputs.setColumnStretch(3, 1)
        layout_inputs.setColumnStretch(4, 1)
        layout_inputs.setColumnStretch(5, 1)

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
        self.total_juros = QLabel("R$ 0,00")
        self.total_final = QLabel("R$ 0,00")
        self.total_juros.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.total_final.setFont(QFont("Segoe UI", 16, QFont.Bold))

        bloco_juros = QVBoxLayout()
        bloco_juros.addWidget(QLabel("Total em Juros"))
        bloco_juros.addWidget(self.total_juros)

        bloco_final = QVBoxLayout()
        bloco_final.addWidget(QLabel("Valor Total Final"))
        bloco_final.addWidget(self.total_final)

        totais_layout.addLayout(bloco_juros)
        totais_layout.addLayout(bloco_final)
        layout_principal.addLayout(totais_layout)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Mês", "Capital", "Juros", "Montante"])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.verticalHeader().setDefaultSectionSize(34)
        self.tabela.setMaximumHeight(34 * 4 + 60)
        layout_principal.addWidget(self.tabela)

        # Gráficos: evolução (linha) + composição (pizza)
        self.layout_graficos = QHBoxLayout()
        grafico1 = grafico_evolucao([], [], [])
        grafico2 = grafico_composicao(0, 0)
        grafico1.setMaximumHeight(250)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)
        layout_principal.addLayout(self.layout_graficos)

        # aplica tema inicial
        aplicar_tema(self, self.dark_mode)

    def atualizar_tema(self, dark_mode):
        """Atualiza o tema dinamicamente."""
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)

    def calcular(self):
        """Executa o cálculo de juros simples e atualiza tabela e gráfico."""
        try:
            capital = self._ler_valor(self.capital)
            taxa = self._ler_valor(self.taxa)
            tempo_text = self.tempo.text().strip()
            if not tempo_text:
                raise ValueError
            tempo = int(tempo_text)

            if self.tipo_tempo.currentText() == "Anos":
                tempo = tempo * 12

            # Converte taxa anual para mensal quando selecionado
            if self.tipo_taxa.currentText() == "Anual":
                taxa = (1 + taxa/100) ** (1/12) * 100 - 100

            if tempo <= 0:
                raise ValueError

            self.tabela.setRowCount(0)
            montante = capital
            total_juros = 0
            meses = []
            saldos = []
            juros = []

            start_qdate = getattr(self.data_inicio, "date", lambda: QDate.currentDate())()

            for mes in range(1, tempo + 1):
                juro_mes = capital * (taxa / 100)
                montante = capital + juro_mes * mes
                total_juros = juro_mes * mes

                try:
                    qdate_mes = start_qdate.addMonths(mes - 1)
                    data_str = qdate_mes.toString("MM/yyyy")
                    meses.append(qdate_mes.toPyDate())
                except Exception:
                    data_str = str(mes)
                    meses.append(mes)

                row = self.tabela.rowCount()
                self.tabela.insertRow(row)
                itens = [
                    QTableWidgetItem(data_str),
                    QTableWidgetItem(format_currency(capital)),
                    QTableWidgetItem(format_currency(juro_mes)),
                    QTableWidgetItem(format_currency(montante))
                ]
                for item in itens:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                for col, item in enumerate(itens):
                    self.tabela.setItem(row, col, item)

                saldos.append(montante)
                juros.append(total_juros)

            self.total_juros.setText(format_currency(total_juros))
            self.total_final.setText(format_currency(montante))

            for i in reversed(range(self.layout_graficos.count())):
                widget = self.layout_graficos.itemAt(i).widget()
                if widget:
                    widget.setParent(None)
            grafico1 = grafico_evolucao(meses, saldos, juros)
            grafico2 = grafico_composicao(capital, total_juros)
            grafico1.setMinimumHeight(180)
            grafico1.setMaximumHeight(240)
            grafico2.setMinimumHeight(180)
            grafico2.setMaximumHeight(240)
            self.layout_graficos.addWidget(grafico1)
            self.layout_graficos.addWidget(grafico2)

        except ValueError:
            self._mostrar_erro("Preencha todos os campos com valores numéricos válidos.")
        except Exception as e:
            self._mostrar_erro(f"Erro no cálculo de juros simples: {e}")

    def limpar(self):
        self.capital.clear()
        self.taxa.clear()
        self.tempo.clear()
        self.tipo_tempo.setCurrentIndex(0)
        self.tipo_taxa.setCurrentIndex(0)
        self.data_inicio.setDate(QDate.currentDate())
        self.total_juros.setText("R$ 0,00")
        self.total_final.setText("R$ 0,00")
        self.tabela.setRowCount(0)
        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        grafico1 = grafico_evolucao([], [], [])
        grafico2 = grafico_composicao(0, 0)
        grafico1.setMinimumHeight(180)
        grafico1.setMaximumHeight(240)
        grafico2.setMinimumHeight(180)
        grafico2.setMaximumHeight(240)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)

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

    def _mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Dados inválidos", mensagem)


CalculadoraJurosSimples = JurosSimples
