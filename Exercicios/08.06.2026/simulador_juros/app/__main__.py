from .tela_login import init_db, TelaLogin
from PyQt5.QtWidgets import QApplication
import sys


def main():
    init_db()
    app = QApplication(sys.argv)
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
