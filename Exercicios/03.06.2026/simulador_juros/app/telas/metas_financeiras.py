import json

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QFileDialog, QMessageBox,
    QSizePolicy
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

        # Campo para inserir a meta total
        row_meta = QHBoxLayout()
        self.input_meta = QLineEdit()
        self.input_meta.setPlaceholderText("R$ 0,00")
        self.input_meta.setFixedHeight(40)
        self.input_meta.setFixedWidth(240)
        self.input_meta.setAlignment(Qt.AlignRight)
        self.input_meta.setMaxLength(18)
        self.input_meta.textChanged.connect(self.on_meta_total_changed)
        btn_distribuir = QPushButton("Distribuir")
        btn_distribuir.setObjectName("distribuir")
        btn_distribuir.setFixedHeight(40)
        btn_distribuir.setFixedWidth(180)
        btn_distribuir.clicked.connect(self.distribuir_meta)
        row_meta.addWidget(QLabel("Meta Total:"))
        row_meta.addWidget(self.input_meta)
        row_meta.addWidget(btn_distribuir)
        main.addLayout(row_meta)

        # Tabela com meses e status de pagamento
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
            # colocar checkbox centralizado em um container para alinhamento correto
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setAlignment(Qt.AlignCenter)
            container_layout.addWidget(chk)
            self.tabela.setCellWidget(i, 2, container)

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

        botoes_acao = QHBoxLayout()
        btn_salvar = QPushButton("Salvar Metas")
        btn_salvar.setObjectName("salvar")
        btn_salvar.setFixedHeight(40)
        btn_salvar.setFixedWidth(180)
        btn_salvar.clicked.connect(self.salvar_metas)
        btn_carregar = QPushButton("Carregar Metas")
        btn_carregar.setObjectName("carregar")
        btn_carregar.setFixedHeight(40)
        btn_carregar.setFixedWidth(180)
        btn_carregar.clicked.connect(self.carregar_metas)
        btn_resetar = QPushButton("Resetar Tabela")
        btn_resetar.setObjectName("resetar")
        btn_resetar.setFixedHeight(40)
        btn_resetar.setFixedWidth(180)
        btn_resetar.clicked.connect(self.resetar_tabela)
        botoes_acao.addWidget(btn_salvar)
        botoes_acao.addWidget(btn_carregar)
        botoes_acao.addWidget(btn_resetar)
        main.addLayout(botoes_acao)

        # Botão de voltar padrão
        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setObjectName("voltar")
        btn_voltar.setFixedHeight(40)
        btn_voltar.setFixedWidth(240)
        btn_voltar.clicked.connect(self.voltar)
        main.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        # Força tema escuro por padrão nesta tela para evitar inconsistências
        self.atualizar_tema(True)

    def distribuir_meta(self):
        text = self.input_meta.text()
        total = self._parse_currency(text)
        if total is None:
            return

        weights = list(range(1, 13))
        total_weight = sum(weights)
        distributed = [total * w / total_weight for w in weights]

        for i, value in enumerate(distributed):
            self.tabela.item(i, 1).setText(self._format_currency(value))
            cb = self._get_checkbox(i)
            if cb is not None:
                cb.blockSignals(True)
                cb.setChecked(False)
                cb.blockSignals(False)

        self.atualizar_indicador_e_grafico()

    def _parse_currency(self, text):
        if not text:
            return None
        s = text.replace("R$", "").replace(".", "").replace(",", ".").strip()
        try:
            return float(s)
        except Exception:
            return None

    def _format_currency(self, value):
        # formato BR: 1.234,56
        s = f"{value:,.2f}"
        s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f"R$ {s}"

    def on_meta_total_changed(self, text):
        if self._formatting_meta:
            return
        self._formatting_meta = True
        old_cursor = self.input_meta.cursorPosition()
        digits = ''.join(ch for ch in text if ch.isdigit())
        if digits == "":
            self.input_meta.setText("")
            self._formatting_meta = False
            return
        value = int(digits) / 100.0
        formatted = self._format_currency(value)
        self.input_meta.setText(formatted)
        self.input_meta.setCursorPosition(self._map_cursor_position(old_cursor, text, formatted))
        self._formatting_meta = False

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
        for i in range(12):
            mes = self.tabela.item(i, 0).text()
            valor = self.tabela.item(i, 1).text() if self.tabela.item(i, 1) else "R$ 0,00"
            cb = self._get_checkbox(i)
            pago = bool(cb.isChecked()) if cb is not None else False
            metas.append({"mes": mes, "valor": valor, "pago": pago})

        dados = {
            "meta_total": self.input_meta.text(),
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

            # bloqueia sinais para evitar múltiplos handlers enquanto atualiza a UI
            self.tabela.blockSignals(True)
            self.input_meta.blockSignals(True)
            try:
                self.input_meta.setText(dados.get("meta_total", ""))
                metas = dados.get("metas", [])
                for i, meta in enumerate(metas[:12]):
                    if self.tabela.item(i, 1):
                        self.tabela.item(i, 1).setText(meta.get("valor", "R$ 0,00"))
                    cb = self._get_checkbox(i)
                    if cb is not None:
                        cb.blockSignals(True)
                        cb.setChecked(bool(meta.get("pago", False)))
                        cb.blockSignals(False)
            finally:
                self.tabela.blockSignals(False)
                self.input_meta.blockSignals(False)
            # Atualiza o indicador uma vez após todas as alterações
            self.atualizar_indicador_e_grafico()
            QMessageBox.information(self, "Carregar metas", "Metas carregadas com sucesso.")
        except Exception as e:
            QMessageBox.warning(self, "Erro ao carregar", f"Não foi possível carregar o arquivo:\n{e}")

    def resetar_tabela(self):
        self.input_meta.clear()
        for i in range(12):
            if self.tabela.item(i, 1):
                self.tabela.item(i, 1).setText("R$ 0,00")
            cb = self._get_checkbox(i)
            if cb is not None:
                cb.blockSignals(True)
                cb.setChecked(False)
                cb.blockSignals(False)
        self.atualizar_indicador_e_grafico()

    def atualizar_indicador_e_grafico(self, state=0):
        depositado = 0.0
        total_meta = self._parse_currency(self.input_meta.text()) or 0.0
        for i in range(12):
            cb = self._get_checkbox(i)
            if cb is not None and cb.isChecked():
                if self.tabela.item(i, 1):
                    depositado += self._parse_currency(self.tabela.item(i, 1).text()) or 0.0

        if total_meta == 0.0:
            total_meta = sum(
                self._parse_currency(self.tabela.item(i, 1).text()) or 0.0
                for i in range(12)
                if self.tabela.item(i, 1)
            )

        restante = max(total_meta - depositado, 0.0)
        self.label_valor_depositado.setText(f"Valor Já Depositado: {self._format_currency(depositado)}")
        achieved = total_meta > 0 and depositado >= (total_meta - 1e-6)
        if achieved:
            self.label_meta_alcancada.setText(f"Meta Alcançada — {self._format_currency(total_meta)}")
        self.label_meta_alcancada.setVisible(achieved)
        self._update_chart(depositado, restante)

    def _update_chart(self, depositado, restante):
        if self.chart_canvas is not None:
            self.chart_layout.removeWidget(self.chart_canvas)
            self.chart_canvas.setParent(None)
            self.chart_canvas = None

        fig = Figure(figsize=(4, 3), constrained_layout=True)
        ax = fig.add_subplot(111)
        if depositado <= 0 and restante <= 0:
            values = [1]
            labels = ["Sem dados"]
            colors = ["#9CA3AF"]
            ax.pie(values, labels=labels, colors=colors, startangle=90)
        else:
            values = [depositado, restante] if restante > 0 else [depositado]
            labels = ["Depositado", "Restante"] if restante > 0 else ["Depositado"]
            colors = ["#10B981", "#F59E0B"] if restante > 0 else ["#10B981"]
            ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)

        ax.set_title("Progresso de Depósito", fontsize=14, pad=18)
        if self.dark_mode:
            fig.patch.set_facecolor("#1F2937")
            ax.set_facecolor("#111827")
            ax.title.set_color("#E6E6E6")
        else:
            fig.patch.set_facecolor("#F3F4F6")
            ax.set_facecolor("#FFFFFF")
            ax.title.set_color("#111827")

        try:
            fig.tight_layout()
        except Exception:
            fig.subplots_adjust(top=0.92)

        self.chart_canvas = FigureCanvas(fig)
        self.chart_layout.addWidget(self.chart_canvas)
        # Ensure no separate pyplot figure windows remain open
        try:
            plt.close(fig)
        except Exception:
            pass

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
