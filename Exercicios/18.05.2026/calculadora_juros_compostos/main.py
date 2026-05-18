import sys

from PySide6.QtWidgets import (
    QApplication
)

from ui.janela import Janela


def main():

    app = QApplication(sys.argv)

    janela = Janela()

    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    