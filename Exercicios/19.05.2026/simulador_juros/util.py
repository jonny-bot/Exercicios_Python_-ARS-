from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont

def criar_card(titulo, cor):
    frame = QFrame()
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

def limpar_campos(widget):
    widget.valor_inicial.clear()
    widget.aporte_mensal.clear()
    widget.taxa_juros.clear()
    widget.tempo.clear()
    widget.data_inicio.clear()
    widget.card_juros.valor_label.setText("R$ 0,00")
    widget.card_investido.valor_label.setText("R$ 0,00")
    widget.card_final.valor_label.setText("R$ 0,00")
    widget.tabela.setRowCount(0)
