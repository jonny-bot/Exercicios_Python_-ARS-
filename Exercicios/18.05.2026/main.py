import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QFrame
)
from PyQt5.QtGui import QFont, QColor, QPalette

class SimuladorJuros(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Juros Compostos")
        self.setGeometry(200, 100, 900, 500)

        # Tema claro
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#F9FAFB"))
        palette.setColor(QPalette.WindowText, QColor("#111827"))
        self.setPalette(palette)

        fonte_padrao = QFont("Segoe UI", 12)
        self.setFont(fonte_padrao)

        layout_principal = QVBoxLayout()

        # Título
        titulo = QLabel("SIMULADOR DE JUROS COMPOSTOS")
        titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        layout_principal.addWidget(titulo)

        # Entradas
        layout_inputs = QGridLayout()

        self.valor_inicial = QLineEdit()
        self.aporte_mensal = QLineEdit()
        self.taxa_juros = QLineEdit()
        self.tipo_taxa = QComboBox()
        self.tipo_taxa.addItems(["Mensal", "Anual"])
        self.tempo = QLineEdit()
        self.tipo_tempo = QComboBox()
        self.tipo_tempo.addItems(["Meses", "Anos"])

        layout_inputs.addWidget(QLabel("Valor Inicial (R$)"), 0, 0)
        layout_inputs.addWidget(self.valor_inicial, 1, 0)
        layout_inputs.addWidget(QLabel("Aporte Mensal (R$)"), 0, 1)
        layout_inputs.addWidget(self.aporte_mensal, 1, 1)
        layout_inputs.addWidget(QLabel("Taxa de Juros (%)"), 0, 2)
        layout_inputs.addWidget(self.taxa_juros, 1, 2)
        layout_inputs.addWidget(self.tipo_taxa, 1, 3)
        layout_inputs.addWidget(QLabel("Tempo"), 0, 4)
        layout_inputs.addWidget(self.tempo, 1, 4)
        layout_inputs.addWidget(self.tipo_tempo, 1, 5)

        layout_principal.addLayout(layout_inputs)

        # Botões
        layout_botoes = QHBoxLayout()
        btn_limpar = QPushButton("LIMPAR")
        btn_calcular = QPushButton("CALCULAR")

        btn_limpar.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: #111827;
                border: 1px solid #D1D5DB;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E5E7EB;
            }
        """)

        btn_calcular.setStyleSheet("""
            QPushButton {
                background-color: #111827;
                color: #FFFFFF;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1F2937;
            }
        """)

        btn_limpar.clicked.connect(self.limpar)
        btn_calcular.clicked.connect(self.calcular)

        layout_botoes.addWidget(btn_limpar)
        layout_botoes.addWidget(btn_calcular)
        layout_principal.addLayout(layout_botoes)

        # Resultados em cards
        layout_resultados = QHBoxLayout()
        self.card_juros = self.criar_card("Total em Juros", "#2563EB")
        self.card_investido = self.criar_card("Valor Total Investido", "#059669")
        self.card_final = self.criar_card("Valor Total Final", "#7C3AED")

        layout_resultados.addWidget(self.card_juros)
        layout_resultados.addWidget(self.card_investido)
        layout_resultados.addWidget(self.card_final)

        layout_principal.addLayout(layout_resultados)
        self.setLayout(layout_principal)

    def criar_card(self, titulo, cor):
        frame = QFrame()
        frame.setStyleSheet("background:#fff; border-radius:10px; border:1px solid #ddd; padding:15px;")
        layout = QVBoxLayout(frame)
        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Segoe UI", 12, QFont.Bold))
        valor = QLabel("R$ 0,00")
        valor.setFont(QFont("Segoe UI", 18, QFont.Bold))
        valor.setStyleSheet(f"color: {cor};")
        layout.addWidget(label_titulo)
        layout.addWidget(valor)
        frame.valor_label = valor
        return frame

    def limpar(self):
        self.valor_inicial.clear()
        self.aporte_mensal.clear()
        self.taxa_juros.clear()
        self.tempo.clear()
        self.card_juros.valor_label.setText("R$ 0,00")
        self.card_investido.valor_label.setText("R$ 0,00")
        self.card_final.valor_label.setText("R$ 0,00")

    def calcular(self):
        try:
            valor_inicial = float(self.valor_inicial.text())
            aporte_mensal = float(self.aporte_mensal.text())
            taxa = float(self.taxa_juros.text()) / 100
            tipo_taxa = self.tipo_taxa.currentText()
            tempo = int(self.tempo.text())
            tipo_tempo = self.tipo_tempo.currentText()

            if tipo_taxa == "Anual":
                taxa /= 12
            if tipo_tempo == "Anos":
                tempo *= 12

            valor_final = valor_inicial * (1 + taxa) ** tempo
            valor_final += aporte_mensal * (((1 + taxa) ** tempo - 1) / taxa)

            total_investido = valor_inicial + (aporte_mensal * tempo)
            total_juros = valor_final - total_investido

            self.card_juros.valor_label.setText(f"R$ {total_juros:,.2f}")
            self.card_investido.valor_label.setText(f"R$ {total_investido:,.2f}")
            self.card_final.valor_label.setText(f"R$ {valor_final:,.2f}")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SimuladorJuros()
    janela.show()
    sys.exit(app.exec_())
