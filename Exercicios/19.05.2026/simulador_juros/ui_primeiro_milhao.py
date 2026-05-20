from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from graficos import grafico_evolucao

class CalculadoraPrimeiroMilhao(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora - Primeiro Milhão")
        self.setGeometry(200, 100, 800, 600)

        # 🎨 Tema claro padronizado
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)

        fonte_padrao = QFont("Segoe UI", 12)
        self.setFont(fonte_padrao)

        layout_principal = QVBoxLayout(self)

        # 🏷️ Título estilizado
        titulo = QLabel("CALCULADORA DO PRIMEIRO MILHÃO")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:20px;")
        layout_principal.addWidget(titulo)

        # 📥 Entradas
        layout_inputs = QGridLayout()
        self.valor_inicial = QLineEdit()
        self.aporte_mensal = QLineEdit()
        self.taxa_juros = QLineEdit()
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])

        # Estilo dos campos
        for campo in [self.valor_inicial, self.aporte_mensal, self.taxa_juros]:
            campo.setStyleSheet("padding:8px; border:1px solid #D1D5DB; border-radius:6px;")

        layout_inputs.addWidget(QLabel("Valor Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.valor_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 2)
        layout_inputs.addWidget(self.taxa_juros, 1, 2)
        layout_inputs.addWidget(self.tipo_taxa, 1, 3)

        layout_principal.addLayout(layout_inputs)
        layout_principal.addSpacing(15)

        # 🔘 Botões estilizados
        layout_botoes = QHBoxLayout()

        btn_voltar = QPushButton("VOLTAR")
        btn_voltar.setStyleSheet("""
            background:#9CA3AF;
            color:#111827;
            padding:12px;
            font-size:14px;
            border-radius:6px;
        """)
        btn_voltar.clicked.connect(self.close)

        btn_calcular = QPushButton("CALCULAR TEMPO")
        btn_calcular.setStyleSheet("""
            background:#2563EB;
            color:#fff;
            padding:12px;
            font-size:14px;
            border-radius:6px;
        """)
        btn_calcular.clicked.connect(self.calcular)

        layout_botoes.addWidget(btn_voltar)
        layout_botoes.addWidget(btn_calcular)
        layout_principal.addLayout(layout_botoes)
        layout_principal.addSpacing(15)

        # 📊 Resultado em card
        self.resultado = QLabel("Tempo estimado: -")
        self.resultado.setFont(QFont("Segoe UI", 14))
        self.resultado.setStyleSheet("""
            background:#E5E7EB;
            color:#111827;
            padding:12px;
            border-radius:6px;
            font-weight:bold;
        """)
        self.resultado.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(self.resultado)
        layout_principal.addSpacing(20)

        # 📈 Gráfico
        self.layout_grafico = QHBoxLayout()
        layout_principal.addLayout(self.layout_grafico)

    def calcular(self):
        try:
            valor_inicial = float(self.valor_inicial.text())
            aporte = float(self.aporte_mensal.text())
            taxa = float(self.taxa_juros.text())
            if self.tipo_taxa.currentText() == "Anual":
                taxa = taxa / 12

            saldo = valor_inicial
            meses = []
            saldos = []
            juros = []
            mes = 0

            while saldo < 1_000_000:
                saldo = saldo * (1 + taxa/100) + aporte
                meses.append(mes)
                saldos.append(saldo)
                juros.append(saldo - (valor_inicial + aporte*mes))
                mes += 1

            anos = mes // 12
            self.resultado.setText(f"Tempo estimado: {mes} meses (~{anos} anos)")

            # Atualiza gráfico
            for i in reversed(range(self.layout_grafico.count())):
                self.layout_grafico.itemAt(i).widget().setParent(None)

            grafico = grafico_evolucao(meses, saldos, juros)
            grafico.setMaximumHeight(250)
            self.layout_grafico.addWidget(grafico)

        except:
            self.resultado.setText("Erro nos valores informados.")

    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().show()
        super().closeEvent(event)
