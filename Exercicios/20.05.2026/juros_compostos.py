import sys, csv, json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox, QComboBox, QFrame, QTableWidget, QTableWidgetItem, QFileDialog
)
from PyQt5.QtGui import QFont, QColor, QPalette
from datetime import datetime
from openpyxl import Workbook   # para exportar Excel

class SimuladorJuros(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador de Juros Compostos")
        self.setGeometry(200, 100, 1200, 700)

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
        self.data_inicio = QLineEdit()
        self.data_inicio.setPlaceholderText("dd/mm/aaaa (ou deixe em branco para hoje)")

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
        layout_inputs.addWidget(QLabel("Data de Início"), 0, 6)
        layout_inputs.addWidget(self.data_inicio, 1, 6)

        layout_principal.addLayout(layout_inputs)

        # Botões
        layout_botoes = QHBoxLayout()
        btn_limpar = QPushButton("LIMPAR")
        btn_calcular = QPushButton("CALCULAR")
        btn_exportar = QPushButton("EXPORTAR")

        btn_limpar.setStyleSheet("background:#fff; border:1px solid #ccc; padding:10px;")
        btn_calcular.setStyleSheet("background:#111827; color:#fff; padding:10px;")
        btn_exportar.setStyleSheet("background:#059669; color:#fff; padding:10px;")

        btn_limpar.clicked.connect(self.limpar)
        btn_calcular.clicked.connect(self.calcular)
        btn_exportar.clicked.connect(self.exportar)

        layout_botoes.addWidget(btn_limpar)
        layout_botoes.addWidget(btn_calcular)
        layout_botoes.addWidget(btn_exportar)
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

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "Mês", "Saldo", "Base de Cálculo", "Rendimento Bruto",
            "IR (%)", "Rendimento Líquido", "Saldo Final"
        ])
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(160)
        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)

    def criar_card(self, titulo, cor):
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

    def limpar(self):
        self.valor_inicial.clear()
        self.aporte_mensal.clear()
        self.taxa_juros.clear()
        self.tempo.clear()
        self.data_inicio.clear()
        self.card_juros.valor_label.setText("R$ 0,00")
        self.card_investido.valor_label.setText("R$ 0,00")
        self.card_final.valor_label.setText("R$ 0,00")
        self.tabela.setRowCount(0)

    def exportar(self):
        formatos = ["Excel (*.xlsx)", "CSV (*.csv)", "JSON (*.json)"]
        caminho, tipo = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", ";;".join(formatos))
        if not caminho:
            return

        dados = []
        for i in range(self.tabela.rowCount()):
            linha = []
            for j in range(self.tabela.columnCount()):
                item = self.tabela.item(i, j)
                linha.append(item.text() if item else "")
            dados.append(linha)

        if tipo.startswith("Excel"):
            wb = Workbook()
            ws = wb.active
            ws.append([self.tabela.horizontalHeaderItem(j).text() for j in range(self.tabela.columnCount())])
            for linha in dados:
                ws.append(linha)
            wb.save(caminho)

        elif tipo.startswith("CSV"):
            with open(caminho, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([self.tabela.horizontalHeaderItem(j).text() for j in range(self.tabela.columnCount())])
                writer.writerows(dados)

        elif tipo.startswith("JSON"):
            colunas = [self.tabela.horizontalHeaderItem(j).text() for j in range(self.tabela.columnCount())]
            lista_dict = [dict(zip(colunas, linha)) for linha in dados]
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(lista_dict, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "Exportação concluída", f"Arquivo salvo em:\n{caminho}")

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

            if self.data_inicio.text():
                data_inicio = datetime.strptime(self.data_inicio.text(), "%d/%m/%Y")
            else:
                data_inicio = datetime.now()

            saldo = valor_inicial
            total_investido = valor_inicial
            total_juros = 0

            self.tabela.setRowCount(tempo)

            ano = data_inicio.year
            mes = data_inicio.month

            for i in range(tempo):
                base_calculo = saldo + aporte_mensal
                rendimento_bruto = base_calculo * taxa

                # IR regressivo conforme prazo
                dias = (i+1) * 30
                if dias <= 180:
                    aliquota = 0.225
                elif dias <= 360:
                    aliquota = 0.20
                elif dias <= 720:
                    aliquota = 0.175
                else:
                    aliquota = 0.15

                ir = rendimento_bruto * aliquota
                rendimento_liquido = rendimento_bruto - ir
                saldo_final = base_calculo + rendimento_liquido

                total_investido += aporte_mensal
                total_juros += rendimento_liquido

                # Incremento correto de meses
                mes_label = datetime(ano, mes, 1).strftime("%b/%Y")
                mes += 1
                if mes > 12:
                    mes = 1
                    ano += 1

                dados = [
                    mes_label,
                    f"R$ {saldo:,.2f}",
                    f"R$ {base_calculo:,.2f}",
                    f"R$ {rendimento_bruto:,.2f}",
                    f"{aliquota*100:.1f}%",
                    f"R$ {rendimento_liquido:,.2f}",
                    f"R$ {saldo_final:,.2f}"
                ]

                for j, valor in enumerate(dados):
                    self.tabela.setItem(i, j, QTableWidgetItem(valor))

                saldo = saldo_final

            # Atualiza os cards
            self.card_juros.valor_label.setText(f"R$ {total_juros:,.2f}")
            self.card_investido.valor_label.setText(f"R$ {total_investido:,.2f}")
            self.card_final.valor_label.setText(f"R$ {saldo:,.2f}")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SimuladorJuros()
    janela.show()
    sys.exit(app.exec_())
