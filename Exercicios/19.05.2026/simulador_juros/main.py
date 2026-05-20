import sys
from PyQt5.QtWidgets import QApplication
from ui import SimuladorJuros

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SimuladorJuros()
    janela.show()
    sys.exit(app.exec_())
