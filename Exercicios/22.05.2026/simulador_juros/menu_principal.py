from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui_juros_compostos import SimuladorJuros
from ui_primeiro_milhao import CalculadoraPrimeiroMilhao
from ui_juros_simples import CalculadoraJurosSimples

class MenuPrincipal(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.dark_mode = dark_mode
        self.voltar_callback = voltar_callback
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu Principal - Simuladores Financeiros")
        self.resize(1100, 750)

        layout = QVBoxLayout(self)
        self.stack = QStackedWidget()

        # Header (tema controlado apenas em TelaLogin; aqui herdado)

        # Página inicial (menu)
        menu_page = QWidget()
        menu_layout = QVBoxLayout(menu_page)

        titulo = QLabel("CENTRAL DE SIMULADORES")
        titulo.setFont(QFont("Segoe UI", 24, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        menu_layout.addWidget(titulo, alignment=Qt.AlignCenter)

        # Função para estilizar botões
        def estilizar_botao(botao, cor):
            botao.setFixedSize(180, 55)
            botao.setCursor(Qt.PointingHandCursor)
            botao.setStyleSheet(f"""
                QPushButton {{
                    background:{cor};
                    color:#fff;
                    font-size:15px;
                    font-weight:500;
                    border-radius:8px;
                    padding:10px;
                }}
                QPushButton:hover {{
                    background-color:#333;
                }}
            """)

        # Botões principais
        btn_simulador = QPushButton("📈 Juros Compostos")
        estilizar_botao(btn_simulador, "#2563EB")
        btn_simulador.clicked.connect(lambda: self.stack.setCurrentWidget(self.simulador))
        menu_layout.addWidget(btn_simulador, alignment=Qt.AlignCenter)

        btn_milhao = QPushButton("💰 Primeiro Milhão")
        estilizar_botao(btn_milhao, "#059669")
        btn_milhao.clicked.connect(lambda: self.stack.setCurrentWidget(self.milhao))
        menu_layout.addWidget(btn_milhao, alignment=Qt.AlignCenter)

        btn_simples = QPushButton("📊 Juros Simples")
        estilizar_botao(btn_simples, "#7C3AED")
        btn_simples.clicked.connect(lambda: self.stack.setCurrentWidget(self.simples))
        menu_layout.addWidget(btn_simples, alignment=Qt.AlignCenter)

        # Botão Logout (voltar para login)
        btn_logout = QPushButton("LOGOUT")
        estilizar_botao(btn_logout, "#F59E0B")
        btn_logout.clicked.connect(self.voltar_login)
        menu_layout.addWidget(btn_logout, alignment=Qt.AlignCenter)

        # Botão sair
        btn_sair = QPushButton("SAIR")
        estilizar_botao(btn_sair, "#EF4444")
        btn_sair.clicked.connect(QApplication.quit)
        menu_layout.addWidget(btn_sair, alignment=Qt.AlignCenter)

        self.stack.addWidget(menu_page)

        # Instancia telas com suporte ao tema
        self.simulador = SimuladorJuros(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.milhao = CalculadoraPrimeiroMilhao(voltar_callback=self.show_menu, dark_mode=self.dark_mode)
        self.simples = CalculadoraJurosSimples(voltar_callback=self.show_menu, dark_mode=self.dark_mode)

        self.stack.addWidget(self.simulador)
        self.stack.addWidget(self.milhao)
        self.stack.addWidget(self.simples)

        layout.addWidget(self.stack)
        self.apply_theme()


    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget { background-color: #1F2937; color: #F9FAFB; }
                QLabel { color: #F9FAFB; }
            """)
        else:
            self.setStyleSheet("""
                QWidget { background-color: #F3F4F6; color: #111827; }
                QLabel { color: #111827; }
            """)

        # Atualiza também as telas internas
        self.simulador.atualizar_tema(self.dark_mode)
        self.milhao.atualizar_tema(self.dark_mode)
        self.simples.atualizar_tema(self.dark_mode)

    # Tema é controlado pela Tela de Login; MenuPrincipal apenas herda e aplica

    def show_menu(self):
        self.stack.setCurrentIndex(0)

    def voltar_login(self):
        self.close()
        if self.voltar_callback:
            self.voltar_callback()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = MenuPrincipal()
    menu.show()
    sys.exit(app.exec_())
