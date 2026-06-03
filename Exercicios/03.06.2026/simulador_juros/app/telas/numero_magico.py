from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QFrame, QCheckBox
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
import requests
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

    def showEvent(self, event):
        super().showEvent(event)
        self._apply_palette()

    def atualizar_tema(self, dark_mode):
        self.dark_mode = dark_mode
        self._apply_theme()
        self._apply_palette()

    def _apply_theme(self):
        self.setStyleSheet(self._dark_stylesheet if self.dark_mode else self._light_stylesheet)

    def _apply_palette(self):
        palette_readonly = QPalette()
        if self.dark_mode:
            palette_readonly.setColor(QPalette.Base, QColor("#2E2E2E"))
            palette_readonly.setColor(QPalette.Text, QColor("#AAAAAA"))
        else:
            palette_readonly.setColor(QPalette.Base, QColor("#E0E0E0"))
            palette_readonly.setColor(QPalette.Text, QColor("#666666"))

        self.input_inflacao.setPalette(palette_readonly)
        self.input_taxa_saque.setPalette(palette_readonly)

    def _setup_ui(self):
        self.setWindowTitle("Número Mágico")
        self.resize(950, 700)

        self.inflacao_atual = get_inflacao_anual()
        self.taxa_saque_atual = 4

        self._dark_stylesheet = """
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
                border: none;
            }
            QPushButton#calcular {
                background-color: #2563EB;
                color: white;
            }
            QPushButton#calcular:hover {
                background-color: #1E40AF;
            }
            QPushButton#voltar {
                background-color: #4B5563;
                color: white;
            }
            QPushButton#voltar:hover {
                background-color: #333333;
            }
        """
        self._light_stylesheet = """
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
                border: none;
            }
            QPushButton#calcular {
                background-color: #2563EB;
                color: white;
            }
            QPushButton#calcular:hover {
                background-color: #1E40AF;
            }
            QPushButton#voltar {
                background-color: #4B5563;
                color: white;
            }
            QPushButton#voltar:hover {
                background-color: #333333;
            }
        """
        self._apply_theme()

        main_layout = QVBoxLayout(self)

        titulo = QLabel("🎩 Número Mágico 🎩")
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

        self.input_inflacao = QLineEdit(self._format_percent_value(self.inflacao_atual) + "%")
        self.input_inflacao.setReadOnly(True)
        self.input_inflacao.textEdited.connect(self.on_valor_percentual_editado)
        form_layout.addRow("Inflação Anual:", self.input_inflacao)

        self.input_taxa_saque = QLineEdit(self._format_percent_value(self.taxa_saque_atual) + "%")
        self.input_taxa_saque.setReadOnly(True)
        self.input_taxa_saque.textEdited.connect(self.on_valor_percentual_editado)
        form_layout.addRow("Taxa de Saque Anual:", self.input_taxa_saque)

        # >>> AQUI entra a configuração inicial de cinza <<<
        if self.dark_mode:
            palette_readonly = QPalette()
            palette_readonly.setColor(QPalette.Base, QColor("#2E2E2E"))
            palette_readonly.setColor(QPalette.Text, QColor("#AAAAAA"))
        else:
            palette_readonly = QPalette()
            palette_readonly.setColor(QPalette.Base, QColor("#E0E0E0"))
            palette_readonly.setColor(QPalette.Text, QColor("#666666"))

        self.input_inflacao.setPalette(palette_readonly)
        self.input_taxa_saque.setPalette(palette_readonly)

        self.manual_toggle = QCheckBox("Editar inflação e taxa de saque manualmente")
        self.manual_toggle.setChecked(False)
        self.manual_toggle.stateChanged.connect(self.on_manual_toggle)
        form_layout.addRow("", self.manual_toggle)

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

        btn_calcular = QPushButton("Calcular")
        btn_calcular.setObjectName("calcular")
        btn_calcular.setFixedHeight(40)
        btn_calcular.setFixedWidth(240)
        btn_calcular.clicked.connect(self.calcular)
        main_layout.addWidget(btn_calcular, alignment=Qt.AlignCenter)

        btn_voltar = QPushButton("Voltar ao Menu")
        btn_voltar.setObjectName("voltar")
        btn_voltar.setFixedHeight(40)
        btn_voltar.setFixedWidth(240)
        btn_voltar.clicked.connect(self.voltar)
        main_layout.addWidget(btn_voltar, alignment=Qt.AlignCenter)

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

        except ValueError:
            self.label_resultado_fluxo.setText("Erro nos valores")
            self.label_resultado_trinity.setText("Erro nos valores")
    def voltar(self):
        if self.voltar_callback:
            self.voltar_callback()

    def on_manual_toggle(self, state):
        manual = state == Qt.Checked
        self.input_inflacao.setReadOnly(not manual)
        self.input_taxa_saque.setReadOnly(not manual)

        # Define estilos conforme tema e estado
        if self.dark_mode:
            editable_style = """
                QLineEdit {
                    background-color: #000000 !important;
                    color: #FFFFFF !important;
                    border: 1px solid #333333;
                }
            """
            readonly_style = """
                QLineEdit {
                    background-color: #2E2E2E !important;
                    color: #AAAAAA !important;
                    border: 1px solid #333333;
                }
            """
        else:
            editable_style = """
                QLineEdit {
                    background-color: #FFFFFF !important;
                    color: #000000 !important;
                    border: 1px solid #CCCCCC;
                }
            """
            readonly_style = """
                QLineEdit {
                    background-color: #E0E0E0 !important;
                    color: #666666 !important;
                    border: 1px solid #CCCCCC;
                }
            """

        # Aplica estilo conforme estado
        if manual:
            self.input_inflacao.setStyleSheet(editable_style)
            self.input_taxa_saque.setStyleSheet(editable_style)
            inflacao_formatada = self._format_percent_value(self.inflacao_atual)
            taxa_formatada = self._format_percent_value(self.taxa_saque_atual)
            self.input_inflacao.setText(f"{inflacao_formatada}%")
            self.input_taxa_saque.setText(f"{taxa_formatada}%")
            self.label_explicacao_trinity.setText(
                f"Baseado em saque anual de {taxa_formatada}%, preservando o principal."
            )
        else:
            self.input_inflacao.setStyleSheet(readonly_style)
            self.input_taxa_saque.setStyleSheet(readonly_style)
            inflacao_formatada = self._format_percent_value(self.inflacao_atual)
            taxa_formatada = self._format_percent_value(self.taxa_saque_atual)
            self.input_inflacao.setText(f"{inflacao_formatada}%")
            self.input_taxa_saque.setText(f"{taxa_formatada}%")
            self.label_explicacao_trinity.setText(
                "Baseado em saque anual de 4%, preservando o principal."
            )

        # Força atualização visual imediata
        self.input_inflacao.repaint()
        self.input_taxa_saque.repaint()

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
            # Mantém apenas números e vírgula/ponto
            s = re.sub(r'[^0-9,\.]', '', text)
            s = s.replace(',', '.')
            if s == '' or s == '.':
                display = ''
            else:
                # Permite até 10 dígitos antes do ponto
                try:
                    val = float(s)
                    disp = ('{:.10f}'.format(val)).rstrip('0').rstrip('.')
                    disp = disp.replace('.', ',')
                    display = disp
                except Exception:
                    display = text

            self.input_margem.blockSignals(True)
            self.input_margem.setText(display)
            self.input_margem.blockSignals(False)
        finally:
            self._formatting = False

    def _format_percent_value(self, value):
        text = str(value)
        # Remove zeros após o ponto decimal, mas mantém números inteiros
        if '.' in text:
            text = text.rstrip('0').rstrip('.')
        return text.replace('.', ',')

    def on_valor_percentual_editado(self):
        sender = self.sender()
        text = sender.text()

        if self._formatting:
            return

        try:
            self._formatting = True

            # Mantém apenas números, vírgula e ponto
            s = re.sub(r'[^0-9,\.]', '', text).replace(',', '.')

            if not s or s in {'.', '0'}:
                display = ''
            else:
                # Remove zeros apenas após o ponto decimal
                if '.' in s:
                    s = s.rstrip('0').rstrip('.')

                # Remove zeros à esquerda (mas mantém "0,x" válido)
                if s.startswith('0') and len(s) > 1 and s[1] != '.':
                    s = s.lstrip('0')

                display = s.replace('.', ',') + '%'

            sender.blockSignals(True)
            sender.setText(display)
            sender.blockSignals(False)

            # Atualiza explicação se for o campo de taxa de saque
            if sender == self.input_taxa_saque:
                self.label_explicacao_trinity.setText(
                    f"Baseado em saque anual de {display}, preservando o principal."
                )

        finally:
            self._formatting = False

    # Formatação automática de porcentagem para Inflação e Taxa de Saque (legado)
    def on_porcentagem_changed(self, text, widget):
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
                    disp = ('{:.2f}'.format(val)).rstrip('0').rstrip('.')
                    disp = disp.replace('.', ',')
                    display = f"{disp}%"
                except Exception:
                    display = text

            widget.blockSignals(True)
            widget.setText(display)
            widget.blockSignals(False)
        finally:
            self._formatting = False
