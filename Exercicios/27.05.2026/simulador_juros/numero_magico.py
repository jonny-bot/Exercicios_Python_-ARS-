from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import requests
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import re


def get_inflacao_anual():
    """
    Puxa a inflação anual (IPCA acumulado em 12 meses) da API do IBGE.
    """
    try:
        url = "https://api.sidra.ibge.gov.br/values/t/7060/n1/all/v/2265/p/last"
        response = requests.get(url)
        data = response.json()
        inflacao_anual = float(data[0]['V'])
        return round(inflacao_anual, 2)
    except Exception:
        return 5.0  # fallback padrão (5% ao ano)


class NumeroMagico(QWidget):
    def __init__(self, voltar_callback=None, dark_mode=False):
        super().__init__()
        self.voltar_callback = voltar_callback
        self.dark_mode = dark_mode
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Número Mágico")
        self.resize(950, 700)

        inflacao_atual = get_inflacao_anual()
        taxa_saque_atual = 4

        # Tema condicional
        if self.dark_mode:
            self.setStyleSheet("""
                QWidget { background-color: #121212; color: #E0E0E0; }
                QLabel { color: #FFFFFF; }
                QLineEdit {
                    background-color: #1E1E1E;
                    color: #FFFFFF;
                    border: 1px solid #333333;
                    border-radius: 6px;
                    padding: 6px;
                }
                QFrame {
                    background-color: #1E1E1E;
                    border: 1px solid #333333;
                    border-radius: 6px;
                }
                QPushButton {
                    border-radius: 8px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton#calcular {
                    background-color: #4CAF50;
                    color: white;
                }
                QPushButton#calcular:hover {
                    background-color: #45A049;
                }
                QPushButton#voltar {
                    background-color: #2196F3;
                    color: white;
                }
                QPushButton#voltar:hover {
                    background-color: #1976D2;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget { background-color: #F5F5F5; color: #000000; }
                QLabel { color: #000000; }
                QLineEdit {
                    background-color: #FFFFFF;
                    color: #000000;
                    border: 1px solid #CCCCCC;
                    border-radius: 6px;
                    padding: 6px;
                }
                QFrame {
                    background-color: #FFFFFF;
                    border: 1px solid #CCCCCC;
                    border-radius: 6px;
                }
                QPushButton {
                    border-radius: 8px;
                    padding: 10px;
                    font-weight: bold;
                }
                QPushButton#calcular {
                    background-color: #4CAF50;
                    color: white;
                }
                QPushButton#calcular:hover {
                    background-color: #45A049;
                }
                QPushButton#voltar {
                    background-color: #2196F3;
                    color: white;
                }
                QPushButton#voltar:hover {
                    background-color: #1976D2;
                }
            """)

        main_layout = QVBoxLayout(self)

        titulo = QLabel("NÚMERO MÁGICO")
        titulo.setFont(QFont("Segoe UI Semibold", 28))
        titulo.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(titulo)

        subtitulo = QLabel("Cálculo baseado no cenário atual (Inflação Anual e Taxa de Saque)")
        subtitulo.setFont(QFont("Segoe UI Light", 14))
        subtitulo.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitulo)

        form_layout = QFormLayout()
        # Campo Meta Mensal com prefixo R$
        meta_container = QFrame()
        meta_layout = QHBoxLayout(meta_container)
        meta_layout.setContentsMargins(0, 0, 0, 0)
        meta_layout.setSpacing(0)
        label_r = QLabel("R$")
        label_r.setFixedWidth(44)
        label_r.setFixedHeight(36)
        label_r.setAlignment(Qt.AlignCenter)
        # estilo será aplicado conforme tema abaixo
        self.input_meta = QLineEdit()
        self.input_meta.setPlaceholderText("0,00")
        self.input_meta.setAlignment(Qt.AlignRight)
        self.input_meta.setFixedHeight(36)
        # estilo será aplicado conforme tema abaixo
        self._formatting = False
        self.input_meta.textChanged.connect(self.on_meta_changed)
        meta_layout.addWidget(label_r)
        meta_layout.addWidget(self.input_meta, 1)
        form_layout.addRow("Meta Mensal:", meta_container)

        # Campo Margem com sufixo %
        margem_container = QFrame()
        margem_layout = QHBoxLayout(margem_container)
        margem_layout.setContentsMargins(0, 0, 0, 0)
        margem_layout.setSpacing(0)
        self.input_margem = QLineEdit()
        self.input_margem.setPlaceholderText("20")
        self.input_margem.setAlignment(Qt.AlignRight)
        self.input_margem.setFixedHeight(36)
        # estilo será aplicado conforme tema abaixo
        self.input_margem.textChanged.connect(self.on_margem_changed)
        label_pct = QLabel("%")
        label_pct.setFixedWidth(32)
        label_pct.setFixedHeight(36)
        label_pct.setAlignment(Qt.AlignCenter)
        # estilo será aplicado conforme tema abaixo
        margem_layout.addWidget(self.input_margem, 1)
        margem_layout.addWidget(label_pct)
        form_layout.addRow("Margem (%):", margem_container)

        # Aplica estilos específicos para tema claro/escuro nos widgets de prefix/sufix e inputs
        if self.dark_mode:
            label_r.setStyleSheet(
                "background:#1E1E1E; color:#E0E0E0; border:1px solid #333333; border-top-left-radius:6px; border-bottom-left-radius:6px;"
            )
            self.input_meta.setStyleSheet(
                "border:1px solid #333333; border-left: none; border-top-right-radius:6px; border-bottom-right-radius:6px; padding-right:8px; background:#1B1B1B; color:#E0E0E0;"
            )
            label_pct.setStyleSheet(
                "background:#1E1E1E; color:#E0E0E0; border:1px solid #333333; border-top-right-radius:6px; border-bottom-right-radius:6px;"
            )
            self.input_margem.setStyleSheet(
                "border:1px solid #333333; border-right: none; border-top-left-radius:6px; border-bottom-left-radius:6px; padding-right:8px; background:#1B1B1B; color:#E0E0E0;"
            )
        else:
            label_r.setStyleSheet(
                "background:#f0f0f0; color:#000; border:1px solid #ddd; border-top-left-radius:6px; border-bottom-left-radius:6px;"
            )
            self.input_meta.setStyleSheet(
                "border:1px solid #ddd; border-left: none; border-top-right-radius:6px; border-bottom-right-radius:6px; padding-right:8px; background:#fff; color:#111827;"
            )
            label_pct.setStyleSheet(
                "background:#f0f0f0; color:#000; border:1px solid #ddd; border-top-right-radius:6px; border-bottom-right-radius:6px;"
            )
            self.input_margem.setStyleSheet(
                "border:1px solid #ddd; border-right: none; border-top-left-radius:6px; border-bottom-left-radius:6px; padding-right:8px; background:#fff; color:#111827;"
            )

        self.input_inflacao = QLineEdit(str(inflacao_atual) + "%")
        self.input_inflacao.setReadOnly(True)
        form_layout.addRow("Inflação Anual:", self.input_inflacao)

        self.input_taxa_saque = QLineEdit(str(taxa_saque_atual) + "%")
        self.input_taxa_saque.setReadOnly(True)
        form_layout.addRow("Taxa de Saque Anual:", self.input_taxa_saque)

        main_layout.addLayout(form_layout)

        resultados_layout = QHBoxLayout()

        frame_fluxo = QFrame()
        frame_fluxo.setLayout(QVBoxLayout())
        self.label_resultado_fluxo = QLabel("Fluxo de Caixa: R$ 0,00")
        self.label_resultado_fluxo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.label_resultado_fluxo.setAlignment(Qt.AlignCenter)
        self.label_explicacao_fluxo = QLabel("Baseado na inflação anual real.")
        self.label_explicacao_fluxo.setAlignment(Qt.AlignCenter)
        frame_fluxo.layout().addWidget(self.label_resultado_fluxo)
        frame_fluxo.layout().addWidget(self.label_explicacao_fluxo)

        frame_trinity = QFrame()
        frame_trinity.setLayout(QVBoxLayout())
        self.label_resultado_trinity = QLabel("Trinity Study: R$ 0,00")
        self.label_resultado_trinity.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.label_resultado_trinity.setAlignment(Qt.AlignCenter)
        self.label_explicacao_trinity = QLabel("Baseado em saque anual de 4%, preservando o principal.")
        self.label_explicacao_trinity.setAlignment(Qt.AlignCenter)
        frame_trinity.layout().addWidget(self.label_resultado_trinity)
        frame_trinity.layout().addWidget(self.label_explicacao_trinity)

        resultados_layout.addWidget(frame_fluxo)
        resultados_layout.addWidget(frame_trinity)
        main_layout.addLayout(resultados_layout)

        self.figure = plt.figure(facecolor="#121212" if self.dark_mode else "#F5F5F5")
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        btn_calcular = QPushButton("Calcular")
        btn_calcular.setObjectName("calcular")
        btn_calcular.setMinimumHeight(50)
        btn_calcular.clicked.connect(self.calcular)
        main_layout.addWidget(btn_calcular)

        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setObjectName("voltar")
        btn_voltar.setMinimumHeight(50)
        btn_voltar.clicked.connect(self.voltar)
        main_layout.addWidget(btn_voltar)

    def calcular(self):
        try:
            meta = float(self.input_meta.text().replace("R$", "").replace(".", "").replace(",", "."))
            margem = meta * (float(self.input_margem.text().replace("%", "").replace(",", ".")) / 100)

            inflacao_raw = float(self.input_inflacao.text().replace("%", "").replace(",", "."))
            inflacao = inflacao_raw / 100
            numero_fluxo = (meta + margem) / inflacao

            taxa_saque_raw = float(self.input_taxa_saque.text().replace("%", "").replace(",", "."))
            taxa_saque = taxa_saque_raw / 100
            numero_trinity = (meta * 12) / taxa_saque
            numero_trinity *= 1 + (float(self.input_margem.text().replace("%", "").replace(",", ".")) / 100)

            self.label_resultado_fluxo.setText(
                f"Fluxo de Caixa: R$ {numero_fluxo:,.2f}".replace(",", "*").replace(".", ",").replace("*", ".")
            )
            self.label_resultado_trinity.setText(
                f"Trinity Study: R$ {numero_trinity:,.2f}".replace(",", "*").replace(".", ",").replace("*", ".")
            )

            self.plot_comparativo(numero_fluxo, numero_trinity)

        except ValueError:
            self.label_resultado_fluxo.setText("Erro nos valores")
            self.label_resultado_trinity.setText("Erro nos valores")
    def plot_comparativo(self, fluxo, trinity):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(["Fluxo de Caixa", "Trinity Study"], [fluxo, trinity],
               color=["#4CAF50", "#2196F3"], alpha=0.85)

        # Ajusta cores conforme tema
        if self.dark_mode:
            fundo = "#121212"
            cor_texto = "white"
        else:
            fundo = "#F5F5F5"
            cor_texto = "black"

        ax.set_facecolor(fundo)
        ax.tick_params(colors=cor_texto)
        ax.set_title("Comparativo dos Cálculos", color=cor_texto, fontsize=14, fontweight="bold")
        ax.set_ylabel("Valor (R$)", color=cor_texto, fontsize=12)

        # Rótulos de valores acima das barras
        valores = [fluxo, trinity]
        for i, v in enumerate(valores):
            ax.text(i, v + (v * 0.02),
                    f"R$ {v:,.0f}".replace(",", "*").replace(".", ",").replace("*", "."),
                    ha='center', color=cor_texto, fontweight='bold', fontsize=11)

        # Grade horizontal
        ax.grid(axis='y', linestyle='--', alpha=0.3, color=cor_texto)

        # Ajusta limite do eixo Y
        ax.set_ylim(0, max(valores) * 1.15)

        self.canvas.draw()

    def voltar(self):
        if self.voltar_callback:
            self.voltar_callback()

    # Formatação em tempo real para Meta Mensal (moeda brasileira)
    def on_meta_changed(self, text):
        if self._formatting:
            return
        try:
            self._formatting = True
            digits = re.sub(r"\D", "", text)
            if digits == "":
                self.input_meta.blockSignals(True)
                self.input_meta.setText("")
                self.input_meta.blockSignals(False)
            else:
                # interpreta últimos dois dígitos como centavos
                value = int(digits) / 100.0
                formatted = f"{value:,.2f}"
                # converte para formato BR: 1.234,56
                formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
                self.input_meta.blockSignals(True)
                self.input_meta.setText(formatted)
                self.input_meta.blockSignals(False)
        finally:
            self._formatting = False

    # Formatação em tempo real para Margem (percentual)
    def on_margem_changed(self, text):
        if self._formatting:
            return
        try:
            self._formatting = True
            s = re.sub(r'[^0-9,\.]', '', text)
            s = s.replace(',', '.')
            if s == '' or s == '.':
                display = ''
            else:
                try:
                    val = float(s)
                    # remove zeros desnecessários
                    disp = ('{:.2f}'.format(val)).rstrip('0').rstrip('.')
                    display = f"{disp}"
                except Exception:
                    display = text

            self.input_margem.blockSignals(True)
            self.input_margem.setText(display)
            self.input_margem.blockSignals(False)
        finally:
            self._formatting = False
