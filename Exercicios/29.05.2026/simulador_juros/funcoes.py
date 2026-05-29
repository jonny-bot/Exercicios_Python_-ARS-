import csv
import json
import os
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import QDate
from graficos import grafico_evolucao, grafico_composicao


def aliquota_ir_por_duracao(tempo_meses):
    """Retorna a alíquota de IR conforme a duração em meses.

    Mantido em nível de módulo para permitir reuso (ex.: debug/testes).
    """
    if tempo_meses <= 6:
        return 22.5
    elif tempo_meses <= 12:
        return 20.0
    elif tempo_meses <= 24:
        return 17.5
    else:
        return 15.0


def calcular_juros(self):
    """
    Calcula o fluxo de juros compostos mês a mês.
    Atualiza a tabela de resultados, os totais exibidos e os gráficos.
    """

    try:
        capital = float(self.capital_inicial.text())
        aporte = float(self.aporte_mensal.text())
        taxa = float(self.taxa_juros.text())
        tempo = int(self.tempo.text())

        if self.tipo_tempo.currentText() == "Anos":
            tempo *= 12
        if self.tipo_taxa.currentText() == "Anual":
            taxa = (1 + taxa / 100) ** (1 / 12) * 100 - 100

        saldo = capital
        meses_plot, saldos, juros_acumulados = [], [], []
        total_investido, total_juros = capital, 0
        self.tabela.setRowCount(0)

        # 🔧 Ajustes visuais para compactar a tabela
        self.tabela.verticalHeader().setDefaultSectionSize(22)   # altura das linhas
        self.tabela.horizontalHeader().setDefaultSectionSize(90) # largura das colunas
        self.tabela.setStyleSheet("""
            QTableWidget::item {
                padding: 2px;  /* reduz espaço interno das células */
            }
            QHeaderView::section {
                padding: 2px;  /* reduz espaço nos cabeçalhos */
            }
        """)
        self.tabela.setContentsMargins(0, 0, 0, 0)  # remove margens externas

        start_qdate = getattr(self.data_inicio, "date", lambda: QDate.currentDate())()

        for mes in range(1, tempo + 1):
            saldo_inicial = saldo
            aporte_mes = aporte
            base_calculo = saldo_inicial + aporte_mes
            rendimento_bruto = base_calculo * (taxa / 100)
            aliquota_ir = aliquota_ir_por_duracao(mes)
            ir = rendimento_bruto * (aliquota_ir / 100)
            rendimento_liquido = rendimento_bruto - ir
            saldo_final = saldo_inicial + aporte_mes + rendimento_liquido

            try:
                qdate_mes = start_qdate.addMonths(mes - 1)
                data_str = qdate_mes.toString("MM/yyyy")
                meses_plot.append(qdate_mes.toPyDate())
            except Exception:
                data_str = str(mes)
                meses_plot.append(mes)

            saldos.append(saldo_final)
            total_investido += aporte_mes
            total_juros += rendimento_liquido
            juros_acumulados.append(total_juros)

            self.tabela.insertRow(self.tabela.rowCount())
            self.tabela.setItem(self.tabela.rowCount()-1, 0, criar_item(data_str))
            self.tabela.setItem(self.tabela.rowCount()-1, 1, criar_item(format_currency(saldo_inicial)))
            self.tabela.setItem(self.tabela.rowCount()-1, 2, criar_item(format_currency(aporte_mes)))
            self.tabela.setItem(self.tabela.rowCount()-1, 3, criar_item(format_currency(base_calculo)))
            self.tabela.setItem(self.tabela.rowCount()-1, 4, criar_item(format_currency(rendimento_bruto)))
            self.tabela.setItem(self.tabela.rowCount()-1, 5, criar_item(f"{aliquota_ir:.1f}%"))
            self.tabela.setItem(self.tabela.rowCount()-1, 6, criar_item(format_currency(rendimento_liquido)))
            self.tabela.setItem(self.tabela.rowCount()-1, 7, criar_item(format_currency(saldo_final)))

            saldo = saldo_final

        self.total_juros.setText(format_currency(total_juros))
        self.total_investido.setText(format_currency(total_investido))
        self.total_final.setText(format_currency(saldos[-1]))

        for i in reversed(range(self.layout_graficos.count())):
            self.layout_graficos.itemAt(i).widget().setParent(None)

        grafico1 = grafico_evolucao(meses_plot, saldos, juros_acumulados, dark_mode=self.dark_mode)
        grafico2 = grafico_composicao(total_investido, total_juros, dark_mode=self.dark_mode)
        grafico1.setMaximumHeight(250)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)

    except Exception as e:
        print("Erro no cálculo de juros:", e)

def format_currency(value):
    """Formata número em padrão brasileiro: separador de milhares '.' e decimal ',' com prefixo R$."""
    try:
        s = f"{value:,.2f}"
    except Exception:
        s = "0.00"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

def limpar_campos(self):
    """Limpa os campos e a tabela."""
    try:
        self.capital_inicial.clear()
        self.aporte_mensal.clear()
        self.taxa_juros.clear()
        self.tempo.clear()
        self.tabela.setRowCount(0)
        self.total_juros.setText("R$ 0.00")
        self.total_investido.setText("R$ 0.00")
        self.total_final.setText("R$ 0.00")
    except Exception as e:
        print("Erro ao limpar campos:", e)


def _get_table_data(self):
    headers = [
        (self.tabela.horizontalHeaderItem(i).text() if self.tabela.horizontalHeaderItem(i) else "")
        for i in range(self.tabela.columnCount())
    ]
    rows = []
    for row in range(self.tabela.rowCount()):
        linha = []
        for col in range(self.tabela.columnCount()):
            item = self.tabela.item(row, col)
            linha.append(item.text() if item else "")
        rows.append(linha)
    return headers, rows


def _save_csv(filename, headers, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def _save_json(filename, headers, rows):
    data = [dict(zip(headers, row)) for row in rows]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _save_excel_html(filename, headers, rows):
    html = """
    <html>
      <head>
        <meta charset='utf-8'>
      </head>
      <body>
        <table border='1' cellspacing='0' cellpadding='4'>
    """
    html += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    for row in rows:
        html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    html += "</table></body></html>"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


def _save_pdf(self, filename, headers, rows):
    summary_items = []
    if hasattr(self, "capital_inicial"):
        summary_items.append(("Capital inicial", self.capital_inicial.text()))
    if hasattr(self, "aporte_mensal"):
        summary_items.append(("Aporte mensal", self.aporte_mensal.text()))
    if hasattr(self, "taxa_juros"):
        summary_items.append(("Taxa", self.taxa_juros.text() + (f" {self.tipo_taxa.currentText()}" if hasattr(self, "tipo_taxa") else "")))
    if hasattr(self, "tempo"):
        tempo_text = self.tempo.text()
        if hasattr(self, "tipo_tempo"):
            tempo_text += f" {self.tipo_tempo.currentText()}"
        summary_items.append(("Tempo", tempo_text))

    summary_html = ""
    if summary_items:
        summary_html = "<div style='margin-bottom:12px;'>"
        summary_html += "<h2>Resumo</h2>"
        summary_html += "<ul style='list-style:none; padding:0;'>"
        for label, value in summary_items:
            summary_html += f"<li><strong>{label}:</strong> {value}</li>"
        summary_html += "</ul></div>"

    html = f"""
    <html>
      <head>
        <meta charset='utf-8'>
        <style>
          body {{ font-family: Arial, sans-serif; font-size: 10pt; }}
          table {{ border-collapse: collapse; width: 100%; }}
          th, td {{ border: 1px solid #444; padding: 4px; }}
          th {{ background: #ddd; }}
          ul {{ margin: 0 0 12px 0; padding: 0; }}
          li {{ margin-bottom: 4px; }}
        </style>
      </head>
      <body>
        {summary_html}
        <table>
    """
    html += "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    for row in rows:
        html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    html += "</table></body></html>"
    document = QTextDocument()
    document.setHtml(html)
    printer = QPrinter(QPrinter.HighResolution)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(filename)
    document.print_(printer)

def exportar_dados(self):
    """Exporta os dados da tabela para CSV, JSON, Excel ou PDF."""
    try:
        # Caminho da pasta Downloads (compatível com Windows, macOS e Linux)
        pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

        options = QFileDialog.Options()
        filename, filtro = QFileDialog.getSaveFileName(
            self,
            "Salvar exportação",
            os.path.join(pasta_downloads, "dados_exportados.csv"),  # sugestão inicial
            "CSV (*.csv);;JSON (*.json);;Excel (*.xls *.xlsx);;PDF (*.pdf);;Todos os arquivos (*)",
            options=options
        )
        if not filename:
            return

        headers, rows = _get_table_data(self)
        selected_filter = (filtro or "").lower()
        ext = os.path.splitext(filename)[1].lower()

        formats = {
            "csv": {"exts": [".csv"], "default": ".csv", "func": _save_csv},
            "json": {"exts": [".json"], "default": ".json", "func": _save_json},
            "excel": {"exts": [".xls", ".xlsx"], "default": ".xls", "func": _save_excel_html},
            "pdf": {"exts": [".pdf"], "default": ".pdf", "func": lambda f, h, r: _save_pdf(self, f, h, r)},
        }

        for key, cfg in formats.items():
            if key in selected_filter or ext in cfg["exts"]:
                if ext not in cfg["exts"]:
                    filename += cfg["default"]
                cfg["func"](filename, headers, rows)
                break
        else:
            if ext not in formats["csv"]["exts"]:
                filename += formats["csv"]["default"]
            formats["csv"]["func"](filename, headers, rows)

        QMessageBox.information(self, "Exportação concluída", f"Dados exportados para:\n{filename}")

    except Exception as e:
        QMessageBox.warning(self, "Erro ao exportar", f"Não foi possível exportar os dados:\n{e}")

def criar_item(texto):
    item = QTableWidgetItem(texto)
    item.setTextAlignment(0x0004 | 0x0080)  # Qt.AlignRight | Qt.AlignVCenter
    return item
