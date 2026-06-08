import json
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidgetItem, QSpinBox, QFileDialog, QMessageBox,
    QFrame, QLineEdit, QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from app.tema import aplicar_tema
from .controle_gastos import DraggableTableWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ReservaEmergencia(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self.gastos = []

        # ✅ Chamada obrigatória para criar a interface e a tabela
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("🦺 Reserva de Emergência")
        layout = QVBoxLayout(self)

        # 🔹 Define o fundo e bordas arredondadas da janela
        self.setStyleSheet("background-color: #F3F4F6; border-radius: 16px;")

        # --- Título ---
        titulo = QLabel("Reserva de Emergência")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # --- Tabela de gastos (criada antes de ser usada) ---
        self.table_gastos = DraggableTableWidget(0, 3)

        self.table_gastos.setMinimumWidth(600)

        self.table_gastos.setHorizontalHeaderLabels(["Categoria", "Valor (R$)", "Ações"])
        self.table_gastos.setMinimumHeight(420)
        self.table_gastos.setColumnWidth(0, 320)
        self.table_gastos.setColumnWidth(1, 180)
        self.table_gastos.setColumnWidth(2, 220)
        self.table_gastos.verticalHeader().setDefaultSectionSize(42)
        self.table_gastos.setAlternatingRowColors(True)
        self.table_gastos.setStyleSheet("""
            QTableWidget {
                background-color: #F9FAFB;
                gridline-color: #D1D5DB;
                font-size: 15px;
                border: 1px solid #D1D5DB;
            }
            QHeaderView::section {
                background-color: #E5E7EB;
                font-weight: bold;
                border: 1px solid #D1D5DB;
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #DBEAFE;
                color: #111827;
            }
        """)

        # --- Layout horizontal principal para tabela + gráfico ---
        tabela_grafico_layout = QHBoxLayout()

        # 🔹 Tabela de gastos
        tabela_grafico_layout.addWidget(self.table_gastos, stretch=4)

        # 🔹 Gráfico e indicador
        grafico_layout = QVBoxLayout()
        grafico_layout.setContentsMargins(10, 0, 10, 0)
        grafico_layout.setSpacing(10)

        self.figura = Figure(figsize=(7, 4))  # aumenta a largura do gráfico
        self.canvas = FigureCanvas(self.figura)
        grafico_layout.addWidget(self.canvas)

        self.lbl_total = QLabel("Total de gastos: R$ 0,00")
        self.lbl_total.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.lbl_total.setAlignment(Qt.AlignCenter)
        grafico_layout.addWidget(self.lbl_total)

        # 🔹 Faz o gráfico ocupar mais espaço horizontal
        tabela_grafico_layout.addLayout(grafico_layout, stretch=3)

        layout.addLayout(tabela_grafico_layout)

        # --- Campos para adicionar novo gasto ---
        form_gasto = QHBoxLayout()
        form_gasto.setSpacing(10)
        form_gasto.setAlignment(Qt.AlignCenter)

        # Campo Categoria
        self.input_categoria = QLineEdit()
        self.input_categoria.setPlaceholderText("Categoria")
        self.input_categoria.setFixedWidth(200)
        self.input_categoria.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #CBD5E1;
                border-radius: 10px;
                padding: 6px 10px;
                font-size: 13px;
                color: #1E293B;
            }
        """)

        # Campo Valor
        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("Valor (R$)")
        self.input_valor.setFixedWidth(100)
        self.input_valor.textChanged.connect(self._formatar_valor)
        self.input_valor.setStyleSheet(self.input_categoria.styleSheet())

        # Campo Meses de segurança
        lbl_meses = QLabel("Meses de segurança:")
        lbl_meses.setFont(QFont("Segoe UI", 11))
        lbl_meses.setStyleSheet("color: #475569; font-weight: 500;")

        self.spin_meses = QSpinBox()
        self.spin_meses.setRange(1, 24)
        self.spin_meses.setValue(6)
        self.spin_meses.setFixedWidth(70)
        self.spin_meses.setStyleSheet("""
            QSpinBox {
                background-color: white;
                border: 2px solid #CBD5E1;
                border-radius: 10px;
                padding: 6px 10px;
                font-size: 13px;
                color: #1E293B;
            }
        """)

        btn_adicionar = QPushButton("➕ Adicionar Gasto")
        btn_adicionar.setFixedWidth(180)
        btn_adicionar.setMinimumHeight(36)
        btn_adicionar.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self._style_button(btn_adicionar)
        btn_adicionar.clicked.connect(self.adicionar_gasto)  # 🔹 Conecta o botão à função

        # ✅ Adiciona tudo no mesmo layout
        form_gasto.addStretch(1)
        form_gasto.addWidget(self.input_categoria)
        form_gasto.addWidget(self.input_valor)
        form_gasto.addWidget(lbl_meses)
        form_gasto.addWidget(self.spin_meses)
        form_gasto.addWidget(btn_adicionar)
        form_gasto.addStretch(1)
        layout.addLayout(form_gasto)

        # --- Campo de meses ---
        lbl_meses = QLabel("Meses de segurança:")
        lbl_meses.setFont(QFont("Segoe UI", 11))
        lbl_meses.setStyleSheet("color: #475569; font-weight: 500;")

        self.spin_meses = QSpinBox()
        self.spin_meses.setRange(1, 24)
        self.spin_meses.setValue(6)
        self.spin_meses.setFixedWidth(90)
        self.spin_meses.setStyleSheet("""
            QSpinBox {
                background-color: white;
                border: 2px solid #CBD5E1;
                border-radius: 10px;
                padding: 6px 10px;
                font-size: 13px;
                color: #1E293B;
            }
            QSpinBox:hover {
                border: 2px solid #3B82F6;
            }
            QSpinBox:focus {
                border: 2px solid #2563EB;
                background-color: #F8FAFC;
            }
        """)

        # --- Resultado ---
        self.lbl_resultado = QLabel("Reserva necessária: R$ 0,00")
        self.lbl_resultado.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.lbl_resultado.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lbl_resultado)

        # --- Botões principais ---
        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(20)
        botoes_layout.setAlignment(Qt.AlignCenter)

        btn_salvar = QPushButton("💾 Salvar Gastos")
        btn_salvar.clicked.connect(self.salvar_gastos)
        self._style_button(btn_salvar)
        botoes_layout.addWidget(btn_salvar)

        btn_carregar = QPushButton("📂 Carregar Gastos")
        btn_carregar.clicked.connect(self.carregar_gastos)
        self._style_button(btn_carregar)
        botoes_layout.addWidget(btn_carregar)

        btn_calcular = QPushButton("📊 Calcular Reserva")
        btn_calcular.clicked.connect(self.calcular_reserva)
        self._style_button(btn_calcular)
        botoes_layout.addWidget(btn_calcular)

        btn_voltar = QPushButton("↩️ Voltar")
        btn_voltar.clicked.connect(self.voltar_callback)
        self._style_button(btn_voltar)
        botoes_layout.addWidget(btn_voltar)

        layout.addLayout(botoes_layout)

        # --- Atualiza gráfico ao abrir ---
        self.atualizar_grafico()
        aplicar_tema(self, self.dark_mode)

    def _style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3B82F6, stop:1 #2563EB
                );
                color: white;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-radius: 12px;
                padding: 10px 18px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.15);
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #60A5FA, stop:1 #3B82F6
                );
            }
            QPushButton:pressed {
                background-color: #1E40AF;
                box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);
            }
        """)

    # --- Função para adicionar gasto ---
    def adicionar_gasto(self):
        categoria = self.input_categoria.text().strip()
        valor_texto = self.input_valor.text().strip()

        if not categoria or not valor_texto:
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha categoria e valor.")
            return

        try:
            valor = self._converter_valor(valor_texto)
        except ValueError:
            QMessageBox.warning(self, "Valor inválido", "Digite um valor numérico válido.")
            return

        row = self.table_gastos.rowCount()
        self.table_gastos.insertRow(row)

        # Sempre cria QTableWidgetItem para categoria e valor
        item_categoria = QTableWidgetItem(categoria)
        item_val = QTableWidgetItem(f"R$ {valor:,.2f}")
        item_val.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.table_gastos.setItem(row, 0, item_categoria)
        self.table_gastos.setItem(row, 1, item_val)

        # Botões de ação na coluna 2
        self._criar_botoes_acao(row)

        # Atualiza lista interna e gráfico
        self.gastos.append((categoria, valor))
        self.atualizar_grafico()

        # Limpa campos
        self.input_categoria.clear()
        self.input_valor.clear()
        self.input_categoria.setFocus()

    # --- Função para salvar gastos ---
    def salvar_gastos(self):
        caminho, _ = QFileDialog.getSaveFileName(
            self, "Salvar Gastos Mensais", "gastos_mensais.json",
            "JSON (*.json);;Todos os arquivos (*)"
        )
        if not caminho:
            return

        dados = [{"categoria": c, "valor": v} for c, v in self.gastos]

        try:
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "Salvar Gastos", f"Gastos salvos em:\n{caminho}")
        except Exception as e:
            QMessageBox.warning(self, "Erro ao salvar", f"Não foi possível salvar o arquivo:\n{e}")

    def carregar_gastos(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self, "Selecionar arquivo de gastos mensais", "",
            "JSON (*.json);;Todos os arquivos (*)"
        )
        if not caminho:
            return

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)

            self.table_gastos.setRowCount(0)
            self.gastos = []

            for item in dados:
                categoria = item.get("categoria", "")
                valor = self._converter_valor(item.get("valor", "0"))

                row = self.table_gastos.rowCount()
                self.table_gastos.insertRow(row)
                self.table_gastos.setItem(row, 0, QTableWidgetItem(categoria))
                item_val = QTableWidgetItem(f"R$ {valor:,.2f}")
                item_val.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.table_gastos.setItem(row, 1, item_val)

                self._criar_botoes_acao(row)
                self.gastos.append((categoria, valor))

            self.atualizar_grafico()
            QMessageBox.information(self, "Carregar Gastos", "Gastos carregados com sucesso!")

        except Exception as e:
            QMessageBox.warning(self, "Erro ao carregar", f"Não foi possível carregar o arquivo:\n{e}")

    def atualizar_grafico(self):
        categorias = [c for c, _ in self.gastos]
        valores = [v for _, v in self.gastos]

        self.figura.clear()
        ax = self.figura.add_subplot(111)

        if valores:
            ax.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90)
            ax.set_title("Distribuição dos Gastos", fontsize=14, fontweight="bold")
        else:
            ax.text(0.5, 0.5, "Sem dados de gastos", fontsize=14,
                    ha="center", va="center", color="#6B7280")
            ax.set_title("Distribuição dos Gastos", fontsize=14, fontweight="bold")

        self.canvas.draw()
        total = sum(valores)
        self.lbl_total.setText(f"Total de gastos: R$ {total:,.2f}")

    def remover_gasto(self, row):
        if 0 <= row < self.table_gastos.rowCount():
            # Remove widgets da linha (botões de ação)
            for col in range(self.table_gastos.columnCount()):
                widget = self.table_gastos.cellWidget(row, col)
                if widget:
                    widget.deleteLater()
                    self.table_gastos.removeCellWidget(row, col)

            # Remove a linha da tabela
            self.table_gastos.removeRow(row)

            # Remove da lista interna
            if 0 <= row < len(self.gastos):
                del self.gastos[row]

            self.atualizar_grafico()

    def mover_gasto_cima(self, row):
        if row > 0:
            self.gastos[row], self.gastos[row - 1] = self.gastos[row - 1], self.gastos[row]
            self._trocar_linhas_tabela(row, row - 1)

    def mover_gasto_baixo(self, row):
        if row < len(self.gastos) - 1:
            self.gastos[row], self.gastos[row + 1] = self.gastos[row + 1], self.gastos[row]
            self._trocar_linhas_tabela(row, row + 1)

    def editar_gasto(self, row):
        valor_item = self.table_gastos.item(row, 1)
        if valor_item:
            valor_atual = valor_item.text().replace("R$", "").replace(".", "").replace(",", ".").strip()
            novo_valor, ok = QInputDialog.getText(self, "Editar valor", "Novo valor (R$):", text=valor_atual)
            if ok and novo_valor:
                try:
                    valor = float(novo_valor.replace("R$", "").replace(".", "").replace(",", "."))
                    valor_item.setText(f"R$ {valor:,.2f}")
                    self.gastos[row] = (self.gastos[row][0], valor)  # ✅ Atualiza lista interna
                    self.atualizar_grafico()
                except ValueError:
                    QMessageBox.warning(self, "Valor inválido", "Digite um valor numérico válido.")

    def _criar_botoes_acao(self, row):
        actions_widget = QWidget()
        actions_layout = QHBoxLayout(actions_widget)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(6)
        actions_layout.setAlignment(Qt.AlignCenter)

        btn_up = QPushButton("⬆️")
        btn_down = QPushButton("⬇️")
        btn_edit = QPushButton("✏️")
        btn_remove = QPushButton("🗑️")

        for btn in [btn_up, btn_down, btn_edit, btn_remove]:
            btn.setFixedSize(36, 36)

        btn_up.clicked.connect(lambda _, r=row: self.mover_gasto_cima(r))
        btn_down.clicked.connect(lambda _, r=row: self.mover_gasto_baixo(r))
        btn_edit.clicked.connect(lambda _, r=row: self.editar_gasto(r))
        btn_remove.clicked.connect(lambda _, r=row: self.remover_gasto(r))

        actions_layout.addWidget(btn_up)
        actions_layout.addWidget(btn_down)
        actions_layout.addWidget(btn_edit)
        actions_layout.addWidget(btn_remove)
        actions_widget.setLayout(actions_layout)
        self.table_gastos.setCellWidget(row, 2, actions_widget)

    def _formatar_valor(self, texto):
        texto_limpo = ''.join(filter(str.isdigit, texto))
        if not texto_limpo:
            self.input_valor.setText("")
            return

        valor = int(texto_limpo) / 100
        texto_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        self.input_valor.blockSignals(True)
        self.input_valor.setText(texto_formatado)
        self.input_valor.blockSignals(False)

    def _trocar_linhas_tabela(self, row1, row2):
        for col in range(self.table_gastos.columnCount()):
            item1 = self.table_gastos.takeItem(row1, col)
            item2 = self.table_gastos.takeItem(row2, col)
            self.table_gastos.setItem(row1, col, item2)
            self.table_gastos.setItem(row2, col, item1)

    def _converter_valor(self, texto):
        """Converte texto monetário para float com segurança."""
        texto_limpo = texto.replace("R$", "").replace(" ", "").strip()

        # Caso americano: 1,000.00 → 1000.00
        if "." in texto_limpo and "," in texto_limpo:
            texto_limpo = texto_limpo.replace(",", "")  # remove vírgula de milhar

        # Caso brasileiro: 1.000,00 → 1000.00
        elif "," in texto_limpo:
            texto_limpo = texto_limpo.replace(".", "").replace(",", ".")

        # Caso simples: 1000.00 → 1000.00
        else:
            texto_limpo = texto_limpo.replace(",", "")

        try:
            return float(texto_limpo)
        except ValueError:
            QMessageBox.warning(self, "Valor inválido", f"Não foi possível converter o valor: {texto}")
            return 0.0

    def calcular_reserva(self):
        """Calcula o total e a reserva necessária com base nos meses de segurança."""
        total = 0.0
        print("🔎 Iniciando cálculo da reserva...")

        for row in range(self.table_gastos.rowCount()):
            valor_item = self.table_gastos.item(row, 1)
            if valor_item and valor_item.text().strip():
                texto_valor = valor_item.text()
                valor = self._converter_valor(texto_valor)
                total += valor
                print(f"✅ Linha {row}: {texto_valor} → {valor}")
            else:
                print(f"⚠️ Linha {row}: sem valor válido")

        meses = self.spin_meses.value()
        reserva = total * meses

        print(f"📊 Total de gastos: {total}")
        print(f"📌 Meses de segurança: {meses}")
        print(f"💰 Reserva necessária: {reserva}")

        self.lbl_total.setText(f"Total de gastos: R$ {total:,.2f}")
        self.lbl_resultado.setText(f"Reserva necessária: R$ {reserva:,.2f}")

    def atualizar_tema(self, dark_mode):
        self.dark_mode = dark_mode
        aplicar_tema(self, self.dark_mode)

        # --- Atualiza o gráfico ao abrir ---
        self.atualizar_grafico()
