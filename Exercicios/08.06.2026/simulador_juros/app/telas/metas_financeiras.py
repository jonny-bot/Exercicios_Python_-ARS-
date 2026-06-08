import json
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QFileDialog, QMessageBox,
    QSizePolicy, QRadioButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MetasFinanceiras(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self._formatting_meta = False
        self.chart_canvas = None
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Metas Financeiras")
        self.resize(900, 600)

        main = QVBoxLayout(self)

        titulo = QLabel("🎯 Metas Financeiras")
        titulo.setFont(QFont("Segoe UI Semibold", 26))
        titulo.setAlignment(Qt.AlignCenter)
        main.addWidget(titulo)

        descricao = QLabel("Área para definir e acompanhar metas financeiras.")
        descricao.setFont(QFont("Segoe UI", 12))
        descricao.setAlignment(Qt.AlignCenter)
        main.addWidget(descricao)

        # Linha superior: meta total + meses + opções
        row_meta = QHBoxLayout()

        self.input_meta = QLineEdit()
        self.input_meta.setPlaceholderText("R$ 0,00")
        self.input_meta.setFixedHeight(40)
        self.input_meta.setFixedWidth(240)
        self.input_meta.setAlignment(Qt.AlignRight)
        self.input_meta.setMaxLength(18)
        self.input_meta.textChanged.connect(self.on_valor_changed)

        self.input_meses = QLineEdit("12")
        self.input_meses.setFixedHeight(40)
        self.input_meses.setFixedWidth(80)
        self.input_meses.setAlignment(Qt.AlignCenter)
        self.input_meses.setEnabled(False)
        self.input_meses.setStyleSheet("background-color: #D1D5DB; color: #6B7280; border-radius: 8px;")

        self.chk_editar_meses = QCheckBox("Editar Número de Meses")
        self.chk_editar_meses.stateChanged.connect(self.toggle_edicao_meses)

        # Campo Valor em Conta
        self.input_valor_conta = QLineEdit()
        self.input_valor_conta.setPlaceholderText("R$ 0,00")
        self.input_valor_conta.setFixedHeight(40)
        self.input_valor_conta.setFixedWidth(180)
        self.input_valor_conta.setAlignment(Qt.AlignRight)
        self.input_valor_conta.setStyleSheet("background-color: #FFFFFF; color: #374151; border-radius: 8px;")
        self.input_valor_conta.textChanged.connect(self.on_valor_changed)

        btn_distribuir = QPushButton("Distribuir")
        btn_distribuir.setFixedHeight(40)
        btn_distribuir.setFixedWidth(180)
        btn_distribuir.setStyleSheet("background-color: #2563EB; color: white; border-radius: 8px;")
        btn_distribuir.clicked.connect(self.distribuir_meta)

        self.chk_mes_atual = QCheckBox("Começar do mês atual")
        row_meta.addWidget(self.chk_mes_atual)

        # Radio buttons Casal / Solteiro
        self.radio_solteiro = QRadioButton("Solteiro")
        self.radio_casal = QRadioButton("Casal")
        self.radio_solteiro.setChecked(True)

        row_meta.addWidget(QLabel("Meta Total:"))
        row_meta.addWidget(self.input_meta)
        row_meta.addWidget(QLabel("Total de Meses:"))
        row_meta.addWidget(self.input_meses)
        row_meta.addWidget(self.chk_editar_meses)
        row_meta.addWidget(self.radio_solteiro)
        row_meta.addWidget(self.radio_casal)
        row_meta.addWidget(QLabel("Valor em Conta:"))
        row_meta.addWidget(self.input_valor_conta)
        row_meta.addWidget(btn_distribuir)
        main.addLayout(row_meta)

        # Tabela
        self.tabela = QTableWidget(12, 3)
        self.tabela.setHorizontalHeaderLabels(["Mês", "Valor (R$)", "Pago"])
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setMinimumWidth(480)
        self.tabela.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.tabela.setColumnWidth(0, 160)
        self.tabela.setColumnWidth(1, 180)
        self.tabela.setColumnWidth(2, 80)
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tabela.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tabela.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        for i, m in enumerate(meses):
            item = QTableWidgetItem(m)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.tabela.setItem(i, 0, item)
            val_item = QTableWidgetItem("R$ 0,00")
            val_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tabela.setItem(i, 1, val_item)
            chk = QCheckBox()
            chk.stateChanged.connect(self.atualizar_indicador_e_grafico)
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setAlignment(Qt.AlignCenter)
            container_layout.addWidget(chk)
            self.tabela.setCellWidget(i, 2, container)

        # Indicadores e gráfico
        self.label_valor_depositado = QLabel("Valor Já Depositado: R$ 0,00")
        self.label_valor_depositado.setFont(QFont("Segoe UI Semibold", 12))
        self.label_valor_depositado.setAlignment(Qt.AlignCenter)

        self.label_meta_alcancada = QLabel("Meta Alcançada 🎉")
        self.label_meta_alcancada.setFont(QFont("Segoe UI Semibold", 14))
        self.label_meta_alcancada.setAlignment(Qt.AlignCenter)
        self.label_meta_alcancada.setStyleSheet("color:#10B981; font-weight:600;")
        self.label_meta_alcancada.setVisible(False)

        self.chart_layout = QVBoxLayout()
        self.chart_canvas = None
        self._update_chart(0.0, 0.0)

        chart_area = QVBoxLayout()
        chart_area.addWidget(self.label_valor_depositado)
        chart_area.addWidget(self.label_meta_alcancada)
        chart_area.addLayout(self.chart_layout)
        chart_area.addStretch(1)

        content = QHBoxLayout()
        content.addWidget(self.tabela)
        content.addLayout(chart_area)
        main.addLayout(content)

        # Rodapé reorganizado
        botoes_acao = QHBoxLayout()
        botoes_acao.setSpacing(60)
        botoes_acao.setContentsMargins(40, 20, 40, 20)

        btn_salvar = QPushButton("Salvar Metas")
        btn_salvar.setFixedHeight(40)
        btn_salvar.setFixedWidth(180)
        btn_salvar.setStyleSheet("background-color: #2563EB; color: white; border-radius: 8px;")
        btn_salvar.clicked.connect(self.salvar_metas)

        btn_carregar = QPushButton("Carregar Metas")
        btn_carregar.setFixedHeight(40)
        btn_carregar.setFixedWidth(180)
        btn_carregar.setStyleSheet("background-color: #10B981; color: white; border-radius: 8px;")
        btn_carregar.clicked.connect(self.carregar_metas)

        btn_resetar = QPushButton("Resetar Tabela")
        btn_resetar.setFixedHeight(40)
        btn_resetar.setFixedWidth(180)
        btn_resetar.setStyleSheet("background-color: #DC2626; color: white; border-radius: 8px;")
        btn_resetar.clicked.connect(self.resetar_tudo)

        botoes_acao.addStretch(1)
        botoes_acao.addWidget(btn_salvar)
        botoes_acao.addStretch(1)
        botoes_acao.addWidget(btn_carregar)
        botoes_acao.addStretch(1)
        botoes_acao.addWidget(btn_resetar)
        botoes_acao.addStretch(1)

        main.addLayout(botoes_acao)

        # Botão de voltar
        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setFixedHeight(40)
        btn_voltar.setFixedWidth(240)
        btn_voltar.clicked.connect(self.voltar)
        main.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        # Tema escuro
        self.atualizar_tema(True)

    def toggle_edicao_meses(self, state):
        """Alterna entre modo bloqueado e editável do campo Total de Meses."""
        if state == Qt.Checked:
            self.input_meses.setEnabled(True)
            self.input_meses.setStyleSheet("background-color: #FFFFFF; color: #111827; border-radius: 8px;")
        else:
            self.input_meses.setEnabled(False)
            self.input_meses.setText("12")
            self.input_meses.setStyleSheet("background-color: #D1D5DB; color: #6B7280; border-radius: 8px;")

    from datetime import datetime

    def distribuir_meta(self):
        meta_total = self._parse_currency(self.input_meta.text())
        valor_em_conta = self._parse_currency(self.input_valor_conta.text())
        nova_meta = max(meta_total - valor_em_conta, 0)

        try:
            meses = int(self.input_meses.text())
        except:
            meses = 12
        if meses <= 0:
            meses = 12

        # ✅ Atualiza o número de linhas da tabela
        self.tabela.setRowCount(meses)

        # Lista de nomes dos meses
        meses_nomes = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        # ✅ Se a opção estiver marcada, começa do mês atual
        start_index = datetime.now().month - 1 if self.chk_mes_atual.isChecked() else 0

        # Preenche os nomes dos meses dinamicamente
        for i in range(meses):
            nome_mes = meses_nomes[(start_index + i) % 12] + (f" {((start_index + i) // 12) + 1}" if meses > 12 else "")
            item = QTableWidgetItem(nome_mes)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.tabela.setItem(i, 0, item)

        # Progressão aritmética: 1 + 2 + ... + n
        soma_pesos = sum(range(1, meses + 1))

        # Distribui os valores proporcionalmente
        for i in range(meses):
            peso = i + 1
            valor_mes = (peso / soma_pesos) * nova_meta
            val_item = QTableWidgetItem(self._format_currency(valor_mes))
            val_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tabela.setItem(i, 1, val_item)

            chk = QCheckBox()
            chk.stateChanged.connect(self.atualizar_indicador_e_grafico)
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setAlignment(Qt.AlignCenter)
            container_layout.addWidget(chk)
            self.tabela.setCellWidget(i, 2, container)

        # ✅ Atualiza indicadores e gráfico
        self.atualizar_indicador_e_grafico()

    def mostrar_valor_em_conta(self):
        valor_em_conta = self._format_currency(self.calcular_valor_em_conta())
        QMessageBox.information(self, "Valor Já em Conta", f"Você possui {valor_em_conta} disponível.")

    def _parse_currency(self, text):
        try:
            # Remove caracteres não numéricos
            clean = text.replace("R$", "").replace(".", "").replace(",", ".").strip()
            if clean == "":
                return 0.0
            return float(clean)
        except:
            return 0.0

    def _format_currency(self, value):
        # formato BR: 1.234,56
        s = f"{value:,.2f}"
        s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f"R$ {s}"

    def on_valor_changed(self):
        campo = self.sender()
        texto = campo.text()
        numeros = ''.join(c for c in texto if c.isdigit())

        if not numeros:
            valor_formatado = "R$ 0,00"
        else:
            valor = int(numeros)
            valor_formatado = f"R$ {valor / 100:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        campo.blockSignals(True)
        campo.setText(valor_formatado)
        campo.blockSignals(False)

    def _map_cursor_position(self, old_cursor, old_text, new_text):
        digits_before = sum(1 for ch in old_text[:old_cursor] if ch.isdigit())
        if digits_before == 0:
            return len(new_text) if old_cursor > len(old_text) else 0
        digit_count = 0
        for idx, ch in enumerate(new_text):
            if ch.isdigit():
                digit_count += 1
            if digit_count == digits_before:
                return idx + 1
        return len(new_text)

    def salvar_metas(self):
        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar metas financeiras",
            "metas_financeiras.json",
            "JSON (*.json);;Todos os arquivos (*)"
        )
        if not caminho:
            return

        metas = []
        for i in range(self.tabela.rowCount()):
            mes = self.tabela.item(i, 0).text()
            valor = self.tabela.item(i, 1).text() if self.tabela.item(i, 1) else "R$ 0,00"
            cb = self._get_checkbox(i)
            pago = bool(cb.isChecked()) if cb is not None else False
            metas.append({"mes": mes, "valor": valor, "pago": pago})

        dados = {
            "meta_total": self.input_meta.text(),
            "valor_em_conta": self.input_valor_conta.text(),
            "modo": "Casal" if self.radio_casal.isChecked() else "Solteiro",
            "total_meses": self.input_meses.text(),  # ✅ novo campo
            "metas": metas
        }

        try:
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "Salvar metas", f"Arquivo salvo em:\n{caminho}")
        except Exception as e:
            QMessageBox.warning(self, "Erro ao salvar", f"Não foi possível salvar o arquivo:\n{e}")

    def carregar_metas(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Carregar metas financeiras",
            "",
            "JSON (*.json);;Todos os arquivos (*)"
        )
        if not caminho:
            return

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)

            self.tabela.blockSignals(True)
            self.input_meta.blockSignals(True)
            self.input_valor_conta.blockSignals(True)
            self.input_meses.blockSignals(True)
            try:
                # ✅ restaura meta total e valor em conta
                self.input_meta.setText(dados.get("meta_total", "R$ 0,00"))
                self.input_valor_conta.setText(dados.get("valor_em_conta", "R$ 0,00"))

                # ✅ restaura número de meses
                total_meses = int(dados.get("total_meses", "12"))
                self.input_meses.setText(str(total_meses))

                # ✅ ajusta número de linhas da tabela
                self.tabela.setRowCount(total_meses)

                # ✅ restaura modo Solteiro/Casal
                modo = dados.get("modo", "Solteiro")
                self.radio_solteiro.setChecked(modo == "Solteiro")
                self.radio_casal.setChecked(modo == "Casal")

                # ✅ restaura metas mensais
                metas = dados.get("metas", [])
                for i, meta in enumerate(metas[:total_meses]):
                    mes = meta.get("mes", f"Mês {i+1}")
                    item = QTableWidgetItem(mes)
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    self.tabela.setItem(i, 0, item)

                    valor = meta.get("valor", "R$ 0,00")
                    val_item = QTableWidgetItem(valor)
                    val_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    self.tabela.setItem(i, 1, val_item)

                    cb = QCheckBox()
                    cb.setChecked(bool(meta.get("pago", False)))
                    cb.stateChanged.connect(self.atualizar_indicador_e_grafico)
                    container = QWidget()
                    container_layout = QHBoxLayout(container)
                    container_layout.setContentsMargins(0, 0, 0, 0)
                    container_layout.setAlignment(Qt.AlignCenter)
                    container_layout.addWidget(cb)
                    self.tabela.setCellWidget(i, 2, container)
            finally:
                self.tabela.blockSignals(False)
                self.input_meta.blockSignals(False)
                self.input_valor_conta.blockSignals(False)
                self.input_meses.blockSignals(False)

            # ✅ recalcula distribuição conforme número de meses carregado
            self.distribuir_meta()

            # ✅ atualiza gráfico e indicador com os novos dados
            # self.atualizar_indicador_e_grafico()

            QMessageBox.information(self, "Carregar metas", "Metas carregadas com sucesso.")
        except Exception as e:
            QMessageBox.warning(self, "Erro ao carregar", f"Não foi possível carregar o arquivo:\n{e}")

    def resetar_tudo(self):
        """Reseta tabela, gráfico e campos para iniciar nova meta."""
        self.input_meta.clear()
        self.input_valor_conta.setText("R$ 0,00")
        self.input_meses.setText("12")
        self.chk_editar_meses.setChecked(False)
        self.input_meses.setEnabled(False)
        self.input_meses.setStyleSheet("background-color: #D1D5DB; color: #6B7280; border-radius: 8px;")

        # ✅ Resetar modo Solteiro/Casal
        self.radio_solteiro.setChecked(True)
        self.radio_casal.setChecked(False)

        # ✅ Resetar opção "Começar do mês atual"
        self.chk_mes_atual.setChecked(False)

        # Limpa tabela
        self.tabela.setRowCount(12)
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        for i, m in enumerate(meses):
            item = QTableWidgetItem(m)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.tabela.setItem(i, 0, item)
            val_item = QTableWidgetItem("R$ 0,00")
            val_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tabela.setItem(i, 1, val_item)
            chk = QCheckBox()
            chk.stateChanged.connect(self.atualizar_indicador_e_grafico)
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setAlignment(Qt.AlignCenter)
            container_layout.addWidget(chk)
            self.tabela.setCellWidget(i, 2, container)

        # Reseta gráfico e indicadores
        self.label_valor_depositado.setText("Valor Já Depositado: R$ 0,00")
        self.label_meta_alcancada.setVisible(False)
        self._update_chart(0.0, 0.0)

    def atualizar_indicador_e_grafico(self):
        depositado = 0.0
        total_meta = 0.0

        # Soma dos valores da tabela
        for i in range(self.tabela.rowCount()):
            val_item = self.tabela.item(i, 1)
            if val_item:
                valor = self._parse_currency(val_item.text())
                total_meta += valor

                chk_container = self.tabela.cellWidget(i, 2)
                if chk_container:
                    chk = chk_container.layout().itemAt(0).widget()
                    if chk.isChecked():
                        depositado += valor

        # Ajuste para modo Casal
        if self.radio_casal.isChecked():
            depositado *= 2
            total_meta *= 2

        # Valor já em conta informado pelo usuário
        valor_em_conta = self._parse_currency(self.input_valor_conta.text())

        # Progresso acumulado = saldo inicial + depósitos realizados
        acumulado = valor_em_conta + depositado

        # Atualiza indicadores
        self.label_valor_depositado.setText(f"Valor Já Depositado: {self._format_currency(acumulado)}")

        # Atualiza gráfico com base no acumulado e meta total
        self._update_chart(acumulado, meta_total := self._parse_currency(self.input_meta.text()))

        # Exibe mensagem de meta alcançada
        self.label_meta_alcancada.setVisible(acumulado >= meta_total and meta_total > 0)

    def _update_chart(self, acumulado, meta_total):
        if self.chart_canvas:
            self.chart_layout.removeWidget(self.chart_canvas)
            self.chart_canvas.deleteLater()
            self.chart_canvas = None

        progresso = (acumulado / meta_total * 100) if meta_total > 0 else 0
        restante = max(100 - progresso, 0)

        fig = Figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        ax.pie(
            [progresso, restante],
            labels=["Acumulado", "Faltante"],
            autopct="%1.1f%%",
            colors=["#10B981", "#F59E0B"],
            startangle=90,
        )
        ax.set_title("Progresso da Meta", fontsize=14)

        self.chart_canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(self.chart_canvas)

    def _get_checkbox(self, row: int):
        widget = self.tabela.cellWidget(row, 2)
        if widget is None:
            return None
        if isinstance(widget, QCheckBox):
            return widget
        # widget is likely a container; find QCheckBox inside
        cb = widget.findChild(QCheckBox)
        return cb

    def atualizar_tema(self, dark_mode: bool):
        self.dark_mode = dark_mode
        if self.dark_mode:
            self.setStyleSheet(
                "QWidget { background-color: #121212; color: #E6E6E6; }"
                "QLabel { color: #E6E6E6; }"
                "QLineEdit { background-color: #1E1E1E; color: #E6E6E6; border: 1px solid #333333; border-radius: 8px; padding: 8px; }"
                "QPushButton { background-color: #2563EB; color: white; border: none; border-radius: 10px; padding: 10px 18px; font-weight: 600; }"
                "QPushButton:hover { background-color: #1D4ED8; }"
                "QPushButton#voltar { background-color: #4B5563; }"
                "QPushButton#voltar:hover { background-color: #374151; }"
                "QPushButton#resetar { background-color: #DC2626; }"
                "QPushButton#resetar:hover { background-color: #B91C1C; }"
                "QPushButton#carregar { background-color: #10B981; }"
                "QPushButton#carregar:hover { background-color: #059669; }"
                "QPushButton#distribuir { background-color: #F59E0B; }"
                "QPushButton#distribuir:hover { background-color: #D97706; }"
            )
            self.tabela.setStyleSheet(
                "QTableWidget { background-color: #1B1B1B; color: #E6E6E6; gridline-color: #333333; }"
                "QHeaderView::section { background-color: #1F2937; color: #E6E6E6; border: none; }"
            )
        else:
            self.setStyleSheet(
                "QWidget { background-color: #F5F5F5; color: #111827; }"
                "QLabel { color: #111827; }"
                "QLineEdit { background-color: #FFFFFF; color: #111827; border: 1px solid #D1D5DB; border-radius: 8px; padding: 8px; }"
                "QPushButton { background-color: #2563EB; color: white; border: none; border-radius: 10px; padding: 10px 18px; font-weight: 600; }"
                "QPushButton:hover { background-color: #1D4ED8; }"
                "QPushButton#voltar { background-color: #4B5563; }"
                "QPushButton#voltar:hover { background-color: #374151; }"
                "QPushButton#resetar { background-color: #DC2626; }"
                "QPushButton#resetar:hover { background-color: #B91C1C; }"
                "QPushButton#carregar { background-color: #10B981; }"
                "QPushButton#carregar:hover { background-color: #059669; }"
                "QPushButton#distribuir { background-color: #F59E0B; }"
                "QPushButton#distribuir:hover { background-color: #D97706; }"
            )
            self.tabela.setStyleSheet(
                "QTableWidget { background-color: #FFFFFF; color: #111827; gridline-color: #D1D5DB; }"
                "QHeaderView::section { background-color: #E5E7EB; color: #111827; border: none; }"
            )

    def voltar(self):
        if self.voltar_callback:
            self.voltar_callback()
