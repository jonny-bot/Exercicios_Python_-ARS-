# funcoes.py
import csv
from PyQt5.QtWidgets import QTableWidgetItem
from graficos import grafico_evolucao, grafico_composicao

def calcular_juros(self):
    """
    Calcula juros compostos mês a mês e atualiza tabela, totais e gráficos.
    """
    try:
        capital = float(self.capital_inicial.text())
        aporte = float(self.aporte_mensal.text())
        taxa = float(self.taxa_juros.text())
        tempo = int(self.tempo.text())

        # Ajusta tempo
        if self.tipo_tempo.currentText() == "Anos":
            tempo = tempo * 12

        # Ajusta taxa
        if self.tipo_taxa.currentText() == "Anual":
            taxa = (1 + taxa/100) ** (1/12) * 100 - 100

        saldo = capital
        meses = []
        saldos = []
        juros_acumulados = []

        total_investido = capital
        total_juros = 0

        self.tabela.setRowCount(0)

        for mes in range(1, tempo + 1):
            base_calculo = saldo
            rendimento_bruto = base_calculo * (taxa / 100)
            ir = rendimento_bruto * 0.15  # IR fixo de 15%
            rendimento_liquido = rendimento_bruto - ir
            saldo_final = saldo + rendimento_liquido + aporte

            meses.append(mes)
            saldos.append(saldo_final)
            total_investido += aporte
            total_juros += rendimento_liquido
            juros_acumulados.append(total_juros)

            # Preenche tabela
            self.tabela.insertRow(self.tabela.rowCount())
            self.tabela.setItem(self.tabela.rowCount()-1, 0, criar_item(str(mes)))
            self.tabela.setItem(self.tabela.rowCount()-1, 1, criar_item(f"R$ {saldo:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 2, criar_item(f"R$ {base_calculo:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 3, criar_item(f"R$ {rendimento_bruto:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 4, criar_item("15%"))
            self.tabela.setItem(self.tabela.rowCount()-1, 5, criar_item(f"R$ {rendimento_liquido:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 6, criar_item(f"R$ {saldo_final:,.2f}"))

            saldo = saldo_final

        # Atualiza totais
        self.total_juros.setText(f"R$ {total_juros:,.2f}")
        self.total_investido.setText(f"R$ {total_investido:,.2f}")
        self.total_final.setText(f"R$ {saldos[-1]:,.2f}")

        # Atualiza gráficos
        for i in reversed(range(self.layout_graficos.count())):
            self.layout_graficos.itemAt(i).widget().setParent(None)

        grafico1 = grafico_evolucao(meses, saldos, juros_acumulados)
        grafico2 = grafico_composicao(total_investido, total_juros)
        grafico1.setMaximumHeight(250)
        grafico2.setMaximumHeight(250)
        self.layout_graficos.addWidget(grafico1)
        self.layout_graficos.addWidget(grafico2)

    except Exception as e:
        print("Erro no cálculo de juros:", e)


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


def exportar_dados(self):
    """Exporta os dados da tabela para CSV."""
    try:
        with open("dados_exportados.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            headers = [self.tabela.horizontalHeaderItem(i).text() for i in range(self.tabela.columnCount())]
            writer.writerow(headers)
            for row in range(self.tabela.rowCount()):
                linha = []
                for col in range(self.tabela.columnCount()):
                    item = self.tabela.item(row, col)
                    linha.append(item.text() if item else "")
                writer.writerow(linha)
        print("Dados exportados para dados_exportados.csv")
    except Exception as e:
        print("Erro ao exportar dados:", e)


def criar_item(texto):
    """Cria item de tabela alinhado à direita."""
    item = QTableWidgetItem(texto)
    item.setTextAlignment(0x0004 | 0x0080)  # Qt.AlignRight | Qt.AlignVCenter
    return item
