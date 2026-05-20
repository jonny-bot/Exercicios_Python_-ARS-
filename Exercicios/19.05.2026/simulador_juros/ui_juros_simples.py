from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QComboBox,
    QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CalculadoraJurosSimples(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora - Juros Simples")
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
        titulo = QLabel("CALCULADORA DE JUROS SIMPLES")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color:#111827; margin-bottom:20px;")
        layout_principal.addWidget(titulo)

        # 📥 Entradas
        layout_inputs = QGridLayout()
        self.capital = QLineEdit()
        self.taxa = QLineEdit()
        self.tempo = QLineEdit()
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Meses", "Anos"])

        # Estilo dos campos
        for campo in [self.capital, self.taxa, self.tempo]:
            campo.setStyleSheet("padding:8px; border:1px solid #D1D5DB; border-radius:6px;")

        layout_inputs.addWidget(QLabel("Capital Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.capital, 1, 0)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 1)
        layout_inputs.addWidget(self.taxa, 1, 1)
        layout_inputs.addWidget(QLabel("Tempo"), 0, 2)
        layout_inputs.addWidget(self.tempo, 1, 2)
        layout_inputs.addWidget(self.tipo_tempo, 1, 3)

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

        btn_calcular = QPushButton("CALCULAR")
        btn_calcular.setStyleSheet("""
            background:#7C3AED;
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
        self.resultado = QLabel("Resultado: -")
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
            capital = float(self.capital.text())
            taxa = float(self.taxa.text())
            tempo = int(self.tempo.text())
            if self.tipo_tempo.currentText() == "Anos":
                tempo = tempo * 12

            juros = capital * (taxa/100) * tempo
            montante = capital + juros

            self.resultado.setText(f"Juros: R$ {juros:,.2f} | Montante: R$ {montante:,.2f}")

            # Atualiza gráfico
            for i in reversed(range(self.layout_grafico.count())):
                self.layout_grafico.itemAt(i).widget().setParent(None)

            meses = list(range(tempo+1))
            saldos = [capital + (capital * (taxa/100) * m) for m in meses]

            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(meses, saldos, color="#2563EB", linewidth=2)
            ax.set_title("Crescimento com Juros Simples", fontsize=12, pad=15)
            ax.set_xlabel("Meses", fontsize=10)
            ax.set_ylabel("Valor (R$)", fontsize=10)
            ax.grid(True, linestyle="--", alpha=0.4)

            fig.subplots_adjust(top=0.85, bottom=0.25, left=0.12, right=0.95)
            grafico = FigureCanvas(fig)
            grafico.setMaximumHeight(250)
            self.layout_grafico.addWidget(grafico)

        except:
            self.resultado.setText("Erro nos valores informados.")

    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().show()
        super().closeEvent(event)
