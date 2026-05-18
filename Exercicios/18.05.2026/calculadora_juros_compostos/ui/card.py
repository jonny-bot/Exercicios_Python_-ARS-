from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class Card(QFrame):

    def __init__(
        self,
        titulo,
        valor="R$ 0,00",
        cor="#22C55E"
    ):
        super().__init__()

        self.setStyleSheet("""
            background-color: #111827;
            border-radius: 14px;
        """)

        self.setFixedHeight(145)
        self.setMinimumWidth(220)

        layout = QVBoxLayout()

        layout.setContentsMargins(
            16,
            16,
            16,
            16
        )

        self.titulo = QLabel(titulo)

        self.titulo.setStyleSheet("""
            color: #94A3B8;
            font-size: 13px;
            font-weight: bold;
        """)

        self.valor = QLabel(valor)

        self.valor.setStyleSheet(f"""
            font-size: 26px;
            font-weight: bold;
            color: {cor};
        """)

        self.valor.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(self.titulo)
        layout.addWidget(self.valor)

        self.setLayout(layout)

    def atualizar(self, valor):
        self.valor.setText(valor)
        