from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QLineEdit, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class ControleGastos(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.dark_mode = dark_mode
        self.voltar_callback = voltar_callback
        self.gastos = []
        self.bancos = []
        self.salario = 0.0
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Painel Financeiro - Controle de Gastos")
        self.resize(1200, 700)

        main_layout = QVBoxLayout(self)

        # --- Cards de resumo ---
        cards_layout = QHBoxLayout()
        self.card_salario = self._build_card("Salário", "R$ 0,00")
        self.card_gastos = self._build_card("Total de Gastos", "R$ 0,00")
        self.card_saldo = self._build_card("Saldo Restante", "R$ 0,00")
        self.card_bancos = self._build_card("Total em Bancos", "R$ 0,00")
        cards_layout.addWidget(self.card_salario)
        cards_layout.addWidget(self.card_gastos)
        cards_layout.addWidget(self.card_saldo)
        cards_layout.addWidget(self.card_bancos)
        main_layout.addLayout(cards_layout)

        # --- Campo para salário ---
        salario_frame = QFrame()
        salario_layout = QHBoxLayout(salario_frame)
        label_salario = QLabel("Informe seu Salário:")
        label_salario.setFont(QFont("Segoe UI", 12))
        self.input_salario = QLineEdit()
        self.input_salario.setPlaceholderText("Ex: 2256.00")

        btn_salario = QPushButton("Atualizar Salário")
        btn_salario.setObjectName("salario")
        btn_salario.setFixedSize(140, 35)
        btn_salario.clicked.connect(self.atualizar_salario)
        salario_layout.addWidget(label_salario)
        salario_layout.addWidget(self.input_salario)
        salario_layout.addWidget(btn_salario)
        main_layout.addWidget(salario_frame)

        # --- Layout principal (Gastos + Bancos) ---
        content_layout = QHBoxLayout()

        # Seção de Gastos
        gastos_frame = QFrame()
        gastos_layout = QVBoxLayout(gastos_frame)
        gastos_label = QLabel("Gastos Mensais")
        gastos_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        gastos_layout.addWidget(gastos_label)

        self.table_gastos = QTableWidget(0, 2)
        self.table_gastos.setHorizontalHeaderLabels(["Categoria", "Valor (R$)"])
        self.table_gastos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        gastos_layout.addWidget(self.table_gastos)
        self.table_gastos.itemChanged.connect(self.editar_gasto)

        form_gasto = QFormLayout()
        self.input_categoria = QLineEdit()
        self.input_valor = QLineEdit()
        form_gasto.addRow("Categoria:", self.input_categoria)
        form_gasto.addRow("Valor (R$):", self.input_valor)
        gastos_layout.addLayout(form_gasto)

        btn_add_gasto = QPushButton("Adicionar Gasto")
        btn_add_gasto.setObjectName("addGasto")
        btn_add_gasto.setFixedSize(120, 35)
        btn_add_gasto.clicked.connect(self.adicionar_gasto)
        gastos_layout.addWidget(btn_add_gasto)

        btn_ver_grafico = QPushButton("Ver Gráfico de Pizza")
        btn_ver_grafico.setObjectName("verGrafico")
        btn_ver_grafico.setFixedSize(160, 35)
        btn_ver_grafico.clicked.connect(self.mostrar_grafico)
        gastos_layout.addWidget(btn_ver_grafico)

        content_layout.addWidget(gastos_frame)

        # Seção de Bancos
        bancos_frame = QFrame()
        bancos_layout = QVBoxLayout(bancos_frame)
        bancos_label = QLabel("Valores em Bancos")
        bancos_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        bancos_layout.addWidget(bancos_label)

        self.table_bancos = QTableWidget(0, 2)
        self.table_bancos.setHorizontalHeaderLabels(["Banco", "Saldo (R$)"])
        self.table_bancos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        bancos_layout.addWidget(self.table_bancos)
        self.table_bancos.itemChanged.connect(self.editar_banco)

        form_banco = QFormLayout()
        self.input_banco = QLineEdit()
        self.input_saldo = QLineEdit()
        form_banco.addRow("Banco:", self.input_banco)
        form_banco.addRow("Saldo (R$):", self.input_saldo)
        bancos_layout.addLayout(form_banco)

        btn_add_banco = QPushButton("Adicionar Banco")
        btn_add_banco.setObjectName("addBanco")
        btn_add_banco.setFixedSize(120, 35)
        btn_add_banco.clicked.connect(self.adicionar_banco)
        bancos_layout.addWidget(btn_add_banco)

        content_layout.addWidget(bancos_frame)
        main_layout.addLayout(content_layout)

        # Botão voltar
        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setObjectName("voltar")
        btn_voltar.setFixedSize(120, 35)
        btn_voltar.clicked.connect(self.voltar_callback)
        main_layout.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        self.apply_theme()

    def _build_card(self, titulo, valor):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Segoe UI", 12, QFont.Bold))
        label_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_titulo)

        label_valor = QLabel(valor)
        label_valor.setFont(QFont("Segoe UI", 14))
        label_valor.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_valor)

        frame.valor_label = label_valor
        return frame

    def atualizar_salario(self):
        salario_text = self.input_salario.text().strip()
        if not salario_text:
            return
        try:
            self.salario = float(salario_text)
        except ValueError:
            return
        self.card_salario.valor_label.setText(f"R$ {self.salario:,.2f}")
        self.atualizar_resumo()

    def adicionar_gasto(self):
        categoria = self.input_categoria.text().strip()
        valor_text = self.input_valor.text().strip()
        if not categoria or not valor_text:
            return
        try:
            valor = float(valor_text)
        except ValueError:
            return
        row = self.table_gastos.rowCount()
        self.table_gastos.insertRow(row)
        self.table_gastos.setItem(row, 0, QTableWidgetItem(categoria))
        self.table_gastos.setItem(row, 1, QTableWidgetItem(f"{valor:,.2f}"))
        self.gastos.append((categoria, valor))
        self.atualizar_resumo()
        self.input_categoria.clear()
        self.input_valor.clear()

    def adicionar_banco(self):
        banco = self.input_banco.text().strip()
        saldo_text = self.input_saldo.text().strip()
        if not banco or not saldo_text:
            return
        try:
            saldo = float(saldo_text)
        except ValueError:
            return
        row = self.table_bancos.rowCount()
        self.table_bancos.insertRow(row)
        self.table_bancos.setItem(row, 0, QTableWidgetItem(banco))
        self.table_bancos.setItem(row, 1, QTableWidgetItem(f"{saldo:,.2f}"))
        self.bancos.append((banco, saldo))
        self.atualizar_resumo()
        self.input_banco.clear()
        self.input_saldo.clear()

    def editar_gasto(self, item):
        row = item.row()
        col = item.column()
        if col == 1:
            try:
                novo_valor = float(item.text().replace(",", "."))
                categoria = self.table_gastos.item(row, 0).text()
                self.gastos[row] = (categoria, novo_valor)
                self.atualizar_resumo()
            except ValueError:
                pass

    def editar_banco(self, item):
        row = item.row()
        col = item.column()
        if col == 1:
            try:
                novo_saldo = float(item.text().replace(",", "."))
                banco = self.table_bancos.item(row, 0).text()
                self.bancos[row] = (banco, novo_saldo)
                self.atualizar_resumo()
            except ValueError:
                pass

    def mostrar_grafico(self):
        # Criar a janela e manter referência
        self.grafico_window = QWidget()
        self.grafico_window.setWindowTitle("Gráfico de Pizza - Gastos Mensais")
        self.grafico_window.resize(600, 500)
        layout = QVBoxLayout(self.grafico_window)

        # Criar gráfico proporcional ao salário
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        if self.salario <= 0:
            categorias = ["Sem salário definido"]
            valores = [1]
            self.ax.pie(valores, labels=categorias, colors=["#93C5FD"], startangle=90)
        else:
            total_gastos = sum(v for _, v in self.gastos)
            saldo_restante = max(self.salario - total_gastos, 0)
            categorias = ["Gastos", "Saldo Restante"]
            valores = [total_gastos, saldo_restante]
            self.ax.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90,
                        colors=["#EF4444", "#10B981"])
        self.ax.set_title("Distribuição do Salário")

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        # Botão fechar dentro da janela
        btn_fechar = QPushButton("Fechar")
        btn_fechar.setFixedSize(100, 30)
        btn_fechar.setStyleSheet("""
            QPushButton {
                background-color: #DC2626;
                color: white;
                border-radius: 6px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #B91C1C;
            }
        """)
        btn_fechar.clicked.connect(self.grafico_window.close)
        layout.addWidget(btn_fechar, alignment=Qt.AlignCenter)

        self.grafico_window.show()

    def atualizar_resumo(self):
        total_gastos = sum(v for _, v in self.gastos)
        total_bancos = sum(v for _, v in self.bancos)
        saldo = self.salario - total_gastos

        self.card_gastos.valor_label.setText(f"R$ {total_gastos:,.2f}")
        self.card_bancos.valor_label.setText(f"R$ {total_bancos:,.2f}")
        self.card_saldo.valor_label.setText(f"R$ {saldo:,.2f}")

    def apply_theme(self):
        theme_light = """
            QWidget { background-color: #F3F4F6; color: #111827; }
            QFrame { background-color: #FFFFFF; border-radius: 10px; padding: 10px; }
            QLabel { color: #111827; }
            QTableWidget { background-color: #FFFFFF; border-radius: 8px; gridline-color: #E5E7EB; }
            QHeaderView::section { background-color: #E5E7EB; color: #111827; font-weight: bold; }
            QLineEdit { background-color: #FFFFFF; border: 1px solid #D1D5DB; border-radius: 4px; padding: 4px; }
            QPushButton { border-radius: 6px; padding: 6px 10px; font-weight: bold; }
            QPushButton#addGasto { background-color: #2563EB; color: white; }
            QPushButton#addBanco { background-color: #2563EB; color: white; }
            QPushButton#salario { background-color: #10B981; color: white; }
            QPushButton#verGrafico { background-color: #F59E0B; color: white; }
            QPushButton#voltar { background-color: #6B7280; color: white; }
            QPushButton:hover { opacity: 0.85; }
        """
        theme_dark = """
            QWidget { background-color: #1F2937; color: #F9FAFB; }
            QFrame { background-color: #374151; border-radius: 10px; padding: 10px; }
            QLabel { color: #F9FAFB; }
            QTableWidget { background-color: #4B5563; border-radius: 8px; gridline-color: #6B7280; }
            QHeaderView::section { background-color: #6B7280; color: #F9FAFB; font-weight: bold; }
            QLineEdit { background-color: #4B5563; border: 1px solid #6B7280; border-radius: 4px; padding: 4px; color: #F9FAFB; }
            QPushButton { border-radius: 6px; padding: 6px 10px; font-weight: bold; }
            QPushButton#addGasto { background-color: #3B82F6; color: white; }
            QPushButton#addBanco { background-color: #3B82F6; color: white; }
            QPushButton#salario { background-color: #10B981; color: white; }
            QPushButton#verGrafico { background-color: #F59E0B; color: white; }
            QPushButton#voltar { background-color: #6B7280; color: white; }
            QPushButton:hover { opacity: 0.85; }
        """
        self.setStyleSheet(theme_dark if self.dark_mode else theme_light)
        