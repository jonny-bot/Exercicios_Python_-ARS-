import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QLineEdit, QFormLayout, QFrame, QAbstractItemView,
    QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QLocale, pyqtSignal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class DraggableTableWidget(QTableWidget):
    """Tabela que permite reordenar linhas por drag and drop."""
    rowMoved = pyqtSignal(int, int)  # Sinal customizado: (from_row, to_row)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.source_row = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            item = self.itemAt(event.pos())
            if item:
                self.source_row = item.row()
        super().mousePressEvent(event)

    def dragMoveEvent(self, event):
        event.accept()
        super().dragMoveEvent(event)

    def dropEvent(self, event):
        if event.source() == self:
            source_row = self.source_row
            target_row = self.rowAt(event.pos().y())
            if target_row < 0:
                target_row = self.rowCount() - 1

            if source_row is not None and target_row >= 0 and source_row != target_row:
                self._move_row(source_row, target_row)
                self.rowMoved.emit(source_row, target_row)
            event.accept()
        else:
            super().dropEvent(event)

    def _move_row(self, source_row, target_row):
        if source_row == target_row:
            return

        row_data = []
        for col in range(self.columnCount()):
            item = self.takeItem(source_row, col)
            widget = self.cellWidget(source_row, col)
            if widget:
                self.removeCellWidget(source_row, col)
            row_data.append((item, widget))

        self.removeRow(source_row)
        self.insertRow(target_row)

        for col, (item, widget) in enumerate(row_data):
            if item:
                self.setItem(target_row, col, item)
            if widget:
                self.setCellWidget(target_row, col, widget)

        self.setCurrentCell(target_row, 0)


class ControleGastos(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.gastos = []
        self.bancos = []
        self.salario = 0.0
        self._formatting = False
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Painel Financeiro - Controle de Gastos")
        self.resize(1200, 700)

        main_layout = QVBoxLayout(self)

        # --- Cards de resumo ---
        cards_layout = QHBoxLayout()
        self.card_salario = self._build_card("🤑 Salário", "R$ 0,00")
        self.card_gastos = self._build_card("💸 Total de Gastos", "R$ 0,00")
        self.card_saldo = self._build_card("🏧 Saldo Restante", "R$ 0,00")
        self.card_bancos = self._build_card("🏦 Total em Bancos", "R$ 0,00")
        cards_layout.addWidget(self.card_salario)
        cards_layout.addWidget(self.card_gastos)
        cards_layout.addWidget(self.card_saldo)
        cards_layout.addWidget(self.card_bancos)
        main_layout.addLayout(cards_layout)

        # --- Campo para salário ---
        salario_frame = QFrame()
        salario_frame.setMaximumWidth(520)
        salario_layout = QHBoxLayout(salario_frame)
        salario_layout.setContentsMargins(0, 0, 0, 0)
        salario_layout.setSpacing(10)
        salario_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_salario = QLabel("Informe seu Salário:")
        label_salario.setFont(QFont("Segoe UI", 12))
        self.input_salario = QLineEdit()
        self.input_salario.setPlaceholderText("R$ 0,00")
        self.input_salario.setFixedWidth(220)
        self.input_salario.setFixedHeight(40)
        self.locale = QLocale(QLocale.Portuguese, QLocale.Brazil)
        self.input_salario.textChanged.connect(self.formatar_input_salario)

        btn_salario = QPushButton("Atualizar Salário")
        btn_salario.setFixedSize(140, 40)
        btn_salario.clicked.connect(self.atualizar_salario)
        self._style_button(btn_salario)
        salario_layout.addWidget(label_salario)
        salario_layout.addWidget(self.input_salario)
        salario_layout.addWidget(btn_salario)
        salario_layout.addStretch()
        main_layout.addWidget(salario_frame, alignment=Qt.AlignLeft)

        # --- Layout principal (Gastos + Bancos) ---
        content_layout = QHBoxLayout()

        # Seção de Gastos
        gastos_frame = QFrame()
        gastos_layout = QVBoxLayout(gastos_frame)
        gastos_label = QLabel("📈 Gastos Mensais")
        gastos_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        gastos_layout.addWidget(gastos_label)

        self.table_gastos = DraggableTableWidget(0, 3)  # Categoria, Valor, Ações
        self.table_gastos.setHorizontalHeaderLabels(["Categoria", "Valor (R$)", "Ações"])
        self.table_gastos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_gastos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        gastos_layout.addWidget(self.table_gastos)
        self.table_gastos.itemChanged.connect(self.editar_gasto)
        self.table_gastos.rowMoved.connect(self.on_gasto_row_moved)

        form_gasto = QFormLayout()
        self.input_categoria = QLineEdit()
        self.input_categoria.setFixedWidth(360)
        self.input_categoria.setFixedHeight(30)
        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("R$ 0,00")
        self.input_valor.setFixedWidth(140)
        self.input_valor.setFixedHeight(30)
        self.input_valor.textChanged.connect(self.formatar_input_valor)
        form_gasto.addRow("Categoria:", self.input_categoria)
        form_gasto.addRow("Valor (R$):", self.input_valor)
        gastos_layout.addLayout(form_gasto)

        # --- Botões lado a lado ---
        botoes_layout = QHBoxLayout()
        btn_add_gasto = QPushButton("➕ Adicionar Gasto")
        btn_add_gasto.setFixedSize(140, 35)
        btn_add_gasto.clicked.connect(self.adicionar_gasto)
        self._style_button(btn_add_gasto)
        botoes_layout.addWidget(btn_add_gasto)

        btn_ver_grafico = QPushButton("📊 Ver Gráfico de Pizza")
        btn_ver_grafico.setFixedSize(160, 35)
        btn_ver_grafico.clicked.connect(self.mostrar_grafico)
        self._style_button(btn_ver_grafico)
        botoes_layout.addWidget(btn_ver_grafico)

        gastos_layout.addLayout(botoes_layout)

        # Seção de Bancos
        bancos_frame = QFrame()
        bancos_layout = QVBoxLayout(bancos_frame)
        bancos_label = QLabel("🏦 Valores em Bancos")
        bancos_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        bancos_layout.addWidget(bancos_label)

        self.table_bancos = DraggableTableWidget(0, 3)
        self.table_bancos.setHorizontalHeaderLabels(["Banco", "Saldo (R$)", "Ações"])
        self.table_bancos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_bancos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        bancos_layout.addWidget(self.table_bancos)
        self.table_bancos.itemChanged.connect(self.editar_banco)
        self.table_bancos.rowMoved.connect(self.on_banco_row_moved)

        form_banco = QFormLayout()
        self.input_banco = QLineEdit()
        self.input_banco.setFixedWidth(260)
        self.input_banco.setFixedHeight(30)
        self.input_saldo = QLineEdit()
        self.input_saldo.setPlaceholderText("R$ 0,00")
        self.input_saldo.setFixedWidth(140)
        self.input_saldo.setFixedHeight(30)
        self.input_saldo.textChanged.connect(self.formatar_input_saldo)
        form_banco.addRow("Banco:", self.input_banco)
        form_banco.addRow("Saldo (R$):", self.input_saldo)
        bancos_layout.addLayout(form_banco)

        btn_add_banco = QPushButton("➕  Adicionar Banco")
        btn_add_banco.setFixedSize(140, 35)
        btn_add_banco.clicked.connect(self.adicionar_banco)
        self._style_button(btn_add_banco)

        btn_ver_grafico_bancos = QPushButton("📊 Ver Gráfico de Bancos")
        btn_ver_grafico_bancos.setFixedSize(170, 35)
        btn_ver_grafico_bancos.clicked.connect(self.mostrar_grafico_bancos)
        self._style_button(btn_ver_grafico_bancos)

        botoes_bancos_layout = QHBoxLayout()
        botoes_bancos_layout.setSpacing(12)
        botoes_bancos_layout.addWidget(btn_add_banco)
        botoes_bancos_layout.addWidget(btn_ver_grafico_bancos)
        bancos_layout.addLayout(botoes_bancos_layout)

        content_layout.addWidget(gastos_frame)
        content_layout.addWidget(bancos_frame)
        main_layout.addLayout(content_layout)

        # Botão voltar
        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setFixedSize(120, 35)
        self._style_button(btn_voltar)
        if self.voltar_callback:
            btn_voltar.clicked.connect(self.voltar_callback)
        else:
            btn_voltar.clicked.connect(self.close)
        main_layout.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        # Tema escuro opcional
        if self.dark_mode:
            self.setStyleSheet("background-color: #1e1e1e; color: white;")

    # --- Métodos auxiliares ---
    def _build_card(self, titulo, valor):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Segoe UI", 12, QFont.Bold))
        label_valor = QLabel(valor)
        label_valor.setFont(QFont("Segoe UI", 14))
        layout.addWidget(label_titulo)
        layout.addWidget(label_valor)
        return frame

    def formatar_input_salario(self):
        if self._formatting:
            return
        try:
            self._formatting = True
            texto = self.input_salario.text()
            digits = re.sub(r"\D", "", texto)
            if digits == "":
                self.input_salario.blockSignals(True)
                self.input_salario.setText("")
                self.input_salario.blockSignals(False)
            else:
                value = int(digits) / 100.0
                formatted = f"R$ {value:,.2f}"
                formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
                self.input_salario.blockSignals(True)
                self.input_salario.setText(formatted)
                self.input_salario.blockSignals(False)
        finally:
            self._formatting = False

    def formatar_input_valor(self):
        if self._formatting:
            return
        try:
            self._formatting = True
            texto = self.input_valor.text()
            digits = re.sub(r"\D", "", texto)
            if digits == "":
                self.input_valor.blockSignals(True)
                self.input_valor.setText("")
                self.input_valor.blockSignals(False)
            else:
                value = int(digits) / 100.0
                formatted = f"R$ {value:,.2f}"
                formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
                self.input_valor.blockSignals(True)
                self.input_valor.setText(formatted)
                self.input_valor.blockSignals(False)
        finally:
            self._formatting = False

    def formatar_input_saldo(self):
        if self._formatting:
            return
        try:
            self._formatting = True
            texto = self.input_saldo.text()
            digits = re.sub(r"\D", "", texto)
            if digits == "":
                self.input_saldo.blockSignals(True)
                self.input_saldo.setText("")
                self.input_saldo.blockSignals(False)
            else:
                value = int(digits) / 100.0
                formatted = f"R$ {value:,.2f}"
                formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
                self.input_saldo.blockSignals(True)
                self.input_saldo.setText(formatted)
                self.input_saldo.blockSignals(False)
        finally:
            self._formatting = False

    def _parse_monetary(self, texto: str) -> float:
        """Converte texto formatado (ex: '1.234,56' ou '1234.56') para float."""
        if texto is None:
            raise ValueError("texto nulo")
        t = texto.strip()
        if not t:
            raise ValueError("texto vazio")
        t = t.replace("R$", "").replace(" ", "")
        # Se vem no formato brasileiro 1.234,56 -> remover pontos e trocar vírgula por ponto
        if t.count(',') == 1 and t.count('.') >= 1:
            t = t.replace('.', '').replace(',', '.')
        else:
            t = t.replace(',', '.')
        return float(t)

    def _format_currency(self, valor):
        try:
            valor_float = float(valor)
        except (TypeError, ValueError):
            valor_float = 0.0
        return self.locale.toString(valor_float, 'f', 2)

    def _style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 12px;
            }
            QPushButton:hover {
                background-color: #1D4ED8;
            }
            QPushButton:pressed {
                background-color: #1E40AF;
            }
        """)

    def adicionar_gasto(self):
        categoria = self.input_categoria.text().strip()
        valor_texto = self.input_valor.text().strip()
        if not categoria or not valor_texto:
            return
        try:
            valor = self._parse_monetary(valor_texto)
        except ValueError:
            return

        row = self.table_gastos.rowCount()
        self.table_gastos.insertRow(row)
        self.table_gastos.setItem(row, 0, QTableWidgetItem(categoria))
        item_val = QTableWidgetItem("R$ " + self._format_currency(valor))
        item_val.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.table_gastos.setItem(row, 1, item_val)

        # Ações: editar, mover, remover
        actions_widget = QWidget()
        actions_layout = QHBoxLayout(actions_widget)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(2)

        btn_up = QPushButton("⬆️")
        btn_up.setFixedSize(25, 25)
        btn_up.setToolTip("Mover gasto para cima")
        btn_up.clicked.connect(lambda _, r=row: self.mover_gasto_cima(r))

        btn_down = QPushButton("⬇️")
        btn_down.setFixedSize(25, 25)
        btn_down.setToolTip("Mover gasto para baixo")
        btn_down.clicked.connect(lambda _, r=row: self.mover_gasto_baixo(r))

        btn_edit = QPushButton("✏️")
        btn_edit.setFixedSize(25, 25)
        btn_edit.setToolTip("Editar valor do gasto")
        btn_edit.clicked.connect(lambda _, r=row: self.editar_gasto_por_botao(r))
        
        btn_remove = QPushButton("🚮")
        btn_remove.setFixedSize(25, 25)
        btn_remove.setToolTip("Remover gasto")
        btn_remove.clicked.connect(lambda _, r=row: self.remover_gasto(r))
        
        actions_layout.addWidget(btn_up)
        actions_layout.addWidget(btn_down)
        actions_layout.addWidget(btn_edit)
        actions_layout.addWidget(btn_remove)

        self.table_gastos.setCellWidget(row, 2, actions_widget)

        self.gastos.append((categoria, valor))
        self.atualizar_resumo()
        self.input_categoria.clear()
        self.input_valor.clear()

    def remover_gasto(self, row):
        if 0 <= row < len(self.gastos):
            self.table_gastos.removeRow(row)
            del self.gastos[row]
            self.atualizar_resumo()

    def remover_banco(self, row):
        if 0 <= row < len(self.bancos):
            self.table_bancos.removeRow(row)
            del self.bancos[row]
            self.atualizar_resumo()

    def mover_gasto_cima(self, row):
        if row > 0:
            # Trocar dados na lista
            self.gastos[row], self.gastos[row - 1] = self.gastos[row - 1], self.gastos[row]
            # Trocar linhas na tabela
            self._trocar_linhas_tabela(self.table_gastos, row, row - 1)
            self.atualizar_resumo()

    def mover_gasto_baixo(self, row):
        if row < len(self.gastos) - 1:
            # Trocar dados na lista
            self.gastos[row], self.gastos[row + 1] = self.gastos[row + 1], self.gastos[row]
            # Trocar linhas na tabela
            self._trocar_linhas_tabela(self.table_gastos, row, row + 1)
            self.atualizar_resumo()

    def mover_banco_cima(self, row):
        if row > 0:
            # Trocar dados na lista
            self.bancos[row], self.bancos[row - 1] = self.bancos[row - 1], self.bancos[row]
            # Trocar linhas na tabela
            self._trocar_linhas_tabela(self.table_bancos, row, row - 1)
            self.atualizar_resumo()

    def mover_banco_baixo(self, row):
        if row < len(self.bancos) - 1:
            # Trocar dados na lista
            self.bancos[row], self.bancos[row + 1] = self.bancos[row + 1], self.bancos[row]
            # Trocar linhas na tabela
            self._trocar_linhas_tabela(self.table_bancos, row, row + 1)
            self.atualizar_resumo()

    def _trocar_linhas_tabela(self, table, row1, row2):
        """Troca duas linhas de uma tabela e reconstrói os botões de ações."""
        # Copia células de row1 para temp
        temp_cells = []
        for col in range(table.columnCount()):
            item = table.item(row1, col)

            if item:
                temp_cells.append((col, item.clone()))
            widget = table.cellWidget(row1, col)

            if widget:
                temp_cells.append((col, widget))

        # Move cells de row2 para row1
        for col in range(table.columnCount()):
            item = table.item(row2, col)
            if item:
                table.setItem(row1, col, item.clone())
            widget = table.cellWidget(row2, col)
            if widget:
                table.setCellWidget(row1, col, widget)

        # Move temp para row2
        for col, cell in temp_cells:
            if isinstance(cell, QTableWidgetItem):
                table.setItem(row2, col, cell)
            else:
                table.setCellWidget(row2, col, cell)

        # Reconstrói botões com índices corretos
        self._reconstruir_botoes_acao(table, row1)
        self._reconstruir_botoes_acao(table, row2)

    def _reconstruir_botoes_acao(self, table, row):
        """Reconstrói os botões de ação para a linha, corrigindo os índices."""
        actions_widget = QWidget()
        actions_layout = QHBoxLayout(actions_widget)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(2)

        if table == self.table_gastos:
            btn_up = QPushButton("⬆️")
            btn_up.setFixedSize(25, 25)
            btn_up.setToolTip("Mover gasto para cima")
            btn_up.clicked.connect(lambda _, r=row: self.mover_gasto_cima(r))

            btn_down = QPushButton("⬇️")
            btn_down.setFixedSize(25, 25)
            btn_down.setToolTip("Mover gasto para baixo")
            btn_down.clicked.connect(lambda _, r=row: self.mover_gasto_baixo(r))

            btn_edit = QPushButton("✏️")
            btn_edit.setFixedSize(25, 25)
            btn_edit.setToolTip("Editar valor do gasto")
            btn_edit.clicked.connect(lambda _, r=row: self.editar_gasto_por_botao(r))

            btn_remove = QPushButton("🚮")
            btn_remove.setFixedSize(25, 25)
            btn_remove.setToolTip("Remover gasto")
            btn_remove.clicked.connect(lambda _, r=row: self.remover_gasto(r))

        else:  # table_bancos
            btn_up = QPushButton("⬆️")
            btn_up.setFixedSize(25, 25)
            btn_up.setToolTip("Mover banco para cima")
            btn_up.clicked.connect(lambda _, r=row: self.mover_banco_cima(r))

            btn_down = QPushButton("⬇️")
            btn_down.setFixedSize(25, 25)
            btn_down.setToolTip("Mover banco para baixo")
            btn_down.clicked.connect(lambda _, r=row: self.mover_banco_baixo(r))

            btn_edit = QPushButton("✏️")
            btn_edit.setFixedSize(25, 25)
            btn_edit.setToolTip("Editar saldo do banco")
            btn_edit.clicked.connect(lambda _, r=row: self.editar_banco_por_botao(r))

            btn_remove = QPushButton("🚮")
            btn_remove.setFixedSize(25, 25)
            btn_remove.setToolTip("Remover banco")
            btn_remove.clicked.connect(lambda _, r=row: self.remover_banco(r))

        actions_layout.addWidget(btn_up)
        actions_layout.addWidget(btn_down)
        actions_layout.addWidget(btn_edit)
        actions_layout.addWidget(btn_remove)

        table.setCellWidget(row, 2, actions_widget)

    def on_gasto_row_moved(self, from_row, to_row):
        """Callback quando uma linha de gasto é movida por drag and drop."""
        self.gastos = []
        for row in range(self.table_gastos.rowCount()):
            categoria_item = self.table_gastos.item(row, 0)
            valor_item = self.table_gastos.item(row, 1)
            if categoria_item and valor_item:
                categoria = categoria_item.text()
                valor = self._parse_monetary(valor_item.text())
                self.gastos.append((categoria, valor))
        self.atualizar_resumo()

    def on_banco_row_moved(self, from_row, to_row):
        """Callback quando uma linha de banco é movida por drag and drop."""
        self.bancos = []
        for row in range(self.table_bancos.rowCount()):
            banco_item = self.table_bancos.item(row, 0)
            saldo_item = self.table_bancos.item(row, 1)
            if banco_item and saldo_item:
                banco = banco_item.text()
                saldo = self._parse_monetary(saldo_item.text())
                self.bancos.append((banco, saldo))
        self.atualizar_resumo()

    def editar_gasto_por_botao(self, row):
        item_categoria = self.table_gastos.item(row, 0)
        item_valor = self.table_gastos.item(row, 1)
        if item_categoria and item_valor:
            categoria = item_categoria.text()
            valor_atual = item_valor.text().replace("R$", "").strip()
            novo_texto, ok = QInputDialog.getText(
                self,
                "Editar Gasto",
                f"Novo valor para '{categoria}':",
                QLineEdit.Normal,
                valor_atual
            )
            if ok and novo_texto.strip():
                try:
                    novo_valor = self._parse_monetary(novo_texto)
                except ValueError:
                    return
                self.gastos[row] = (categoria, novo_valor)
                self.table_gastos.blockSignals(True)
                item_valor.setText("R$ " + self._format_currency(novo_valor))
                item_valor.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table_gastos.blockSignals(False)
                self.atualizar_resumo()

    def editar_banco_por_botao(self, row):
        item_banco = self.table_bancos.item(row, 0)
        item_saldo = self.table_bancos.item(row, 1)
        if item_banco and item_saldo:
            banco = item_banco.text()
            saldo_atual = item_saldo.text().replace("R$", "").strip()
            novo_texto, ok = QInputDialog.getText(
                self,
                "Editar Banco",
                f"Novo saldo para '{banco}':",
                QLineEdit.Normal,
                saldo_atual
            )
            if ok and novo_texto.strip():
                try:
                    novo_saldo = self._parse_monetary(novo_texto)
                except ValueError:
                    return
                self.bancos[row] = (banco, novo_saldo)
                self.table_bancos.blockSignals(True)
                item_saldo.setText("R$ " + self._format_currency(novo_saldo))
                item_saldo.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table_bancos.blockSignals(False)
                self.atualizar_resumo()

    def editar_gasto(self, item):
        row = item.row()
        col = item.column()
        if col == 1 and 0 <= row < len(self.gastos):
            texto = item.text().strip()
            if not texto:
                return
            try:
                novo_valor = self._parse_monetary(texto)
                categoria_item = self.table_gastos.item(row, 0)
                if not categoria_item:
                    return
                categoria = categoria_item.text()
                self.gastos[row] = (categoria, novo_valor)
                self.table_gastos.blockSignals(True)
                item.setText("R$ " + self._format_currency(novo_valor))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table_gastos.blockSignals(False)
                self.atualizar_resumo()
            except (ValueError, IndexError, AttributeError):
                pass

    def editar_banco(self, item):
        row = item.row()
        col = item.column()
        if col == 1:
            try:
                novo_saldo = self._parse_monetary(item.text())
                banco = self.table_bancos.item(row, 0).text()
                self.bancos[row] = (banco, novo_saldo)
                self.table_bancos.blockSignals(True)
                item.setText("R$ " + self._format_currency(novo_saldo))
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table_bancos.blockSignals(False)
                self.atualizar_resumo()
            except (ValueError, IndexError, AttributeError):
                pass

    def adicionar_banco(self):
        nome_banco = self.input_banco.text().strip()
        saldo_texto = self.input_saldo.text().strip()
        if not nome_banco or not saldo_texto:
            return
        try:
            saldo = self._parse_monetary(saldo_texto)
        except ValueError:
            return

        row = self.table_bancos.rowCount()
        self.table_bancos.insertRow(row)
        self.table_bancos.setItem(row, 0, QTableWidgetItem(nome_banco))
        item_saldo = QTableWidgetItem("R$ " + self._format_currency(saldo))
        item_saldo.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.table_bancos.setItem(row, 1, item_saldo)
        # Ações: mover, editar, remover
        actions_widget = QWidget()
        actions_layout = QHBoxLayout(actions_widget)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(2)

        btn_up = QPushButton("⬆️")
        btn_up.setFixedSize(25, 25)
        btn_up.setToolTip("Mover banco para cima")
        btn_up.clicked.connect(lambda _, r=row: self.mover_banco_cima(r))

        btn_down = QPushButton("⬇️")
        btn_down.setFixedSize(25, 25)
        btn_down.setToolTip("Mover banco para baixo")
        btn_down.clicked.connect(lambda _, r=row: self.mover_banco_baixo(r))

        btn_edit = QPushButton("✏️")
        btn_edit.setFixedSize(25, 25)
        btn_edit.setToolTip("Editar saldo do banco")
        btn_edit.clicked.connect(lambda _, r=row: self.editar_banco_por_botao(r))

        btn_remove = QPushButton("🚮")
        btn_remove.setFixedSize(25, 25)
        btn_remove.setToolTip("Remover banco")
        btn_remove.clicked.connect(lambda _, r=row: self.remover_banco(r))

        actions_layout.addWidget(btn_up)
        actions_layout.addWidget(btn_down)
        actions_layout.addWidget(btn_edit)
        actions_layout.addWidget(btn_remove)

        self.table_bancos.setCellWidget(row, 2, actions_widget)

        self.bancos.append((nome_banco, saldo))
        self.atualizar_resumo()
        self.input_banco.clear()
        self.input_saldo.clear()

    def atualizar_resumo(self):
        total_gastos = sum(v for _, v in self.gastos)
        total_bancos = sum(v for _, v in self.bancos)
        saldo_restante = self.salario - total_gastos
        self.card_gastos.findChildren(QLabel)[1].setText("R$ " + self._format_currency(total_gastos))
        self.card_saldo.findChildren(QLabel)[1].setText("R$ " + self._format_currency(saldo_restante))
        self.card_bancos.findChildren(QLabel)[1].setText("R$ " + self._format_currency(total_bancos))

    def atualizar_salario(self):
        texto = self.input_salario.text().strip()
        if not texto:
            return
        try:
            self.salario = self._parse_monetary(texto)
            self.card_salario.findChildren(QLabel)[1].setText("R$ " + self._format_currency(self.salario))
            self.atualizar_resumo()
        except ValueError:
            pass

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("background-color: #1e1e1e; color: white;")
        else:
            self.setStyleSheet("")

    def mostrar_grafico(self):
        self.grafico_window = QWidget()
        self.grafico_window.setWindowTitle("Gráfico de Pizza - Gastos Mensais")
        self.grafico_window.resize(800, 600)
        layout = QVBoxLayout(self.grafico_window)

        self.fig, self.ax = plt.subplots(figsize=(6, 5))

        if self.salario <= 0:
            categorias = ["Sem salário definido"]
            valores = [1]
            cores = ["#93C5FD"]
        else:
            categorias = [cat for cat, _ in self.gastos]
            valores = [val for _, val in self.gastos]
            total_gastos = sum(valores)
            saldo_restante = max(self.salario - total_gastos, 0)

            categorias.append("Saldo Restante")
            valores.append(saldo_restante)

            # Paleta inspirada no exemplo da internet
            cores = ["#4285F4", "#FF00FF", "#FFD700", "#800080", "#FF8C00"]

        wedges, texts, autotexts = self.ax.pie(
            valores,
            labels=categorias,
            autopct="%1.1f%%",
            startangle=90,
            colors=cores,
            textprops={"color": "white", "fontsize": 10}
        )

        self.ax.set_title("Distribuição do Salário", fontsize=12, fontweight="bold")

        # Adiciona legenda lateral
        self.ax.legend(
            wedges,
            categorias,
            title="Categorias",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1)
        )

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        btn_fechar = QPushButton("Fechar")
        btn_fechar.setFixedSize(100, 30)
        self._style_button(btn_fechar)
        btn_fechar.clicked.connect(self.grafico_window.close)
        layout.addWidget(btn_fechar, alignment=Qt.AlignCenter)

        self.grafico_window.show()

    def mostrar_grafico_bancos(self):
        self.grafico_window = QWidget()
        self.grafico_window.setWindowTitle("Gráfico de Pizza - Valores em Bancos")
        self.grafico_window.resize(800, 600)
        layout = QVBoxLayout(self.grafico_window)

        self.fig, self.ax = plt.subplots(figsize=(6, 5))

        if not self.bancos:
            categorias = ["Sem bancos cadastrados"]
            valores = [1]
            cores = ["#93C5FD"]
        else:
            categorias = [banco for banco, _ in self.bancos]
            valores = [saldo for _, saldo in self.bancos]
            cores = ["#2563EB", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899"]

        wedges, texts, autotexts = self.ax.pie(
            valores,
            labels=categorias,
            autopct="%1.1f%%",
            startangle=90,
            colors=cores,
            textprops={"color": "white", "fontsize": 10}
        )

        self.ax.set_title("Distribuição dos Saldos em Bancos", fontsize=12, fontweight="bold")

        self.ax.legend(
            wedges,
            categorias,
            title="Bancos",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1)
        )

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        btn_fechar = QPushButton("Fechar")
        btn_fechar.setFixedSize(100, 30)
        self._style_button(btn_fechar)
        btn_fechar.clicked.connect(self.grafico_window.close)
        layout.addWidget(btn_fechar, alignment=Qt.AlignCenter)

        self.grafico_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControleGastos()
    window.show()
    sys.exit(app.exec_())
