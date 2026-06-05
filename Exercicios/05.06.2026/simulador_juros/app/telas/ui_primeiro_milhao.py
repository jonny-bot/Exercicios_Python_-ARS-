from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView, QAbstractItemView, QSizePolicy
)
from PyQt5.QtGui import QFont, QDoubleValidator
from PyQt5.QtCore import Qt
from core.funcoes import exportar_dados, format_currency, limpar_campos, validar_e_calcular
from core.graficos import grafico_evolucao
from app.tema import aplicar_tema   # usa tema centralizado


# constantes
META_PRIMEIRO_MILHAO = 1_000_000
LIMITE_MESES_SIMULACAO = 2400

class CalculadoraPrimeiroMilhao(QWidget):
    """Tela para cálculo do primeiro milhão."""
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.graficos_meses = []
        self.graficos_saldos = []
        self.graficos_juros = []
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
        layout_inputs.setContentsMargins(0, 0, 0, 0)
        layout_inputs.setHorizontalSpacing(18)
        layout_inputs.setVerticalSpacing(10)
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
        self.taxa_juros.setPlaceholderText("Ex.: 1.05 %")
        # formatação automática para taxa (duas casas)
        self.taxa_juros.editingFinished.connect(self._formatar_taxa)

        layout_inputs.addWidget(QLabel("Capital Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros"), 0, 2)
        # container com campo de taxa e rótulo de porcentagem
        from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel as QLabelW
        taxa_container = QWidget()
        taxa_h = QHBoxLayout(taxa_container)
        taxa_h.setContentsMargins(0, 0, 0, 0)
        taxa_h.setSpacing(6)
        taxa_h.addWidget(self.taxa_juros)
        percent_label = QLabelW("%")
        percent_label.setFixedWidth(20)
        percent_label.setAlignment(Qt.AlignCenter)
        taxa_h.addWidget(percent_label)
        layout_inputs.addWidget(taxa_container, 1, 2)
        layout_inputs.addWidget(QLabel("Tipo Taxa"), 0, 3)
        layout_inputs.addWidget(self.tipo_taxa, 1, 3)

        for i in range(4):
            layout_inputs.setColumnStretch(i, 1)

        layout_principal.addLayout(layout_inputs)

        # Botões
        botoes_layout = QHBoxLayout()
        botoes_layout.setContentsMargins(0, 0, 0, 0)
        botoes_layout.setSpacing(12)

        def estilizar_botao(botao, cor):
            botao.setCursor(Qt.PointingHandCursor)
            botao.setFixedHeight(40)
            botao.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            botao.setStyleSheet(f"""
                QPushButton {{
                    background:{cor};
                    color:#fff;
                    font-size:14px;
                    font-weight:500;
                    border:none;
                    border-radius:6px;
                    padding:10px 16px;
                    outline: none;
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
        btn_calcular.clicked.connect(lambda: validar_e_calcular(self))

        btn_exportar = QPushButton("EXPORTAR")
        estilizar_botao(btn_exportar, "#059669")
        btn_exportar.clicked.connect(self.exportar)

        botoes_layout.addWidget(btn_voltar)
        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_calcular)
        botoes_layout.addWidget(btn_exportar)
        layout_principal.addLayout(botoes_layout)

        # Totais (widget compacto acima da tabela)
        from PyQt5.QtWidgets import QWidget
        totais_widget = QWidget()
        totais_widget.setFixedHeight(80)
        totais_widget.setObjectName("totais_widget")
        totais_layout = QHBoxLayout(totais_widget)
        totais_layout.setContentsMargins(8, 8, 8, 8)
        totais_layout.setSpacing(30)

        self.meses_necessarios = QLabel("0 meses")
        self.anos_necessarios = QLabel("0 anos")
        self.meses_necessarios.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.anos_necessarios.setFont(QFont("Segoe UI", 18, QFont.Bold))

        bloco_meses = QVBoxLayout()
        bloco_meses.addWidget(QLabel("Meses Necessários"))
        bloco_meses.addWidget(self.meses_necessarios)

        bloco_anos = QVBoxLayout()
        bloco_anos.addWidget(QLabel("Anos Necessários"))
        bloco_anos.addWidget(self.anos_necessarios)

        totais_layout.addLayout(bloco_meses)
        totais_layout.addLayout(bloco_anos)
        totais_layout.addStretch(1)
        layout_principal.addWidget(totais_widget)

        # Tabela (segue lógica: Mês, Investimento Mensal, Juros, Total Investido, Total Juros, Acumulado)
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(["Meses", "Investimento Mensal", "Juros", "Total Investido", "Total Juros", "Acumulado"])
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.setMinimumHeight(140)
        self.tabela.setMaximumHeight(160)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela.verticalHeader().setVisible(False)
        layout_principal.addWidget(self.tabela)

        # Gráficos
        self.layout_graficos = QHBoxLayout()
        self.layout_graficos.setContentsMargins(0, 0, 0, 0)
        self.layout_graficos.setSpacing(12)
        self._atualizar_grafico([], [], [])
        layout_principal.addLayout(self.layout_graficos)

        # aplica tema inicial
        aplicar_tema(self, self.dark_mode)

    def atualizar_tema(self, dark_mode):
        """Atualiza o tema dinamicamente."""
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)
        self._atualizar_grafico(self.graficos_meses, self.graficos_saldos, self.graficos_juros)

    def _formatar_taxa(self):
        """Formata o campo de taxa para duas casas decimais usando ponto como separador."""
        try:
            texto = self.taxa_juros.text().strip()
            if not texto:
                return

            # remove espaços
            s = texto.replace(' ', '')

            # se contém vírgula ou ponto, usa _ler_valor para interpretar normalmente
            if ',' in s or '.' in s:
                valor = self._ler_valor(self.taxa_juros)
            else:
                # apenas dígitos: interpretar '105' como 1.05 (últimos 2 dígitos = decimais)
                if s.isdigit():
                    if len(s) >= 3:
                        valor = int(s) / 100.0
                    else:
                        # 1 ou 2 dígitos -> tratar como unidades (ex.: '1' -> 1.00 ; '12' -> 12.00)
                        valor = float(s)
                else:
                    # fallback: tentar interpretar com _ler_valor
                    valor = self._ler_valor(self.taxa_juros)

            # mantém duas casas decimais e usa ponto como separador (ex.: 1.05)
            formatted = f"{valor:.2f}"
            self.taxa_juros.setText(formatted)
        except Exception:
            # não interrompe fluxo em caso de erro de parsing
            pass

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

            # inicializa valores
            saldo = capital
            meses = 0
            saldos_plot = [saldo]
            juros_cumulativos = [0.0]
            total_investido = 0.0
            total_juros = 0.0
            self.tabela.setRowCount(0)

            # linha mês 0
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            itens0 = [
                QTableWidgetItem(str(0)),
                QTableWidgetItem(format_currency(0)),
                QTableWidgetItem(format_currency(0)),
                QTableWidgetItem(format_currency(0)),
                QTableWidgetItem(format_currency(0)),
                QTableWidgetItem(format_currency(saldo))
            ]
            for item in itens0:
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            for col, item in enumerate(itens0):
                self.tabela.setItem(row, col, item)

            # itera meses até atingir meta ou limite
            while saldo < META_PRIMEIRO_MILHAO and meses < LIMITE_MESES_SIMULACAO:
                meses += 1
                # juros do mês sobre o saldo atual
                juros_mes = saldo * taxa
                saldo = saldo + aporte + juros_mes
                total_investido += aporte
                total_juros += juros_mes

                saldos_plot.append(saldo)
                juros_cumulativos.append(total_juros)

                row = self.tabela.rowCount()
                self.tabela.insertRow(row)
                itens = [
                    QTableWidgetItem(str(meses)),
                    QTableWidgetItem(format_currency(aporte)),
                    QTableWidgetItem(format_currency(juros_mes)),
                    QTableWidgetItem(format_currency(total_investido)),
                    QTableWidgetItem(format_currency(total_juros)),
                    QTableWidgetItem(format_currency(saldo))
                ]
                for item in itens:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                for col, item in enumerate(itens):
                    self.tabela.setItem(row, col, item)

            if saldo < META_PRIMEIRO_MILHAO:
                self._mostrar_erro(
                    "A simulação passou de 200 anos. Aumente o aporte ou a taxa de juros."
                )
                self._atualizar_grafico(list(range(0, meses + 1)), saldos_plot, juros_cumulativos)
                return

            anos = meses / 12
            self.meses_necessarios.setText(f"{meses} meses")
            self.anos_necessarios.setText(f"{anos:.1f} anos")
            self._atualizar_grafico(list(range(0, meses + 1)), saldos_plot, juros_cumulativos)

        except ValueError:
            self._mostrar_erro("Preencha todos os campos com valores numéricos válidos.")
        except Exception as erro:
            self._mostrar_erro(f"Não foi possível calcular: {erro}")

    def limpar(self):
        limpar_campos(self)

    def exportar(self):
        exportar_dados(self)

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
        self.graficos_meses = meses
        self.graficos_saldos = saldos
        self.graficos_juros = juros

        for i in reversed(range(self.layout_graficos.count())):
            widget = self.layout_graficos.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        grafico = grafico_evolucao(meses, saldos, juros, dark_mode=self.dark_mode)
        grafico.setMinimumHeight(220)
        grafico.setMaximumHeight(360)
        from PyQt5.QtWidgets import QSizePolicy
        grafico.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # adiciona o gráfico ocupando toda a largura disponível
        # passando stretch=1 para o widget dentro do layout horizontal
        # remove stretches laterais para evitar centralização em coluna estreita
        self.layout_graficos.addWidget(grafico, 1)

    def _mostrar_erro(self, mensagem):
        QMessageBox.warning(self, "Dados inválidos", mensagem)


PrimeiroMilhao = CalculadoraPrimeiroMilhao
