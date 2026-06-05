import sys
from PyQt5.QtWidgets import QApplication
from app.tela_login import init_db, TelaLogin


def main():
    init_db()
    app = QApplication(sys.argv)
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
