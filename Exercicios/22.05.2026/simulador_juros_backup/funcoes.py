# funcoes.py
import csv
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
from graficos import grafico_evolucao, grafico_composicao

def aliquota_ir_por_duracao(tempo_meses):
    """Retorna a alíquota de IR (%) com base no prazo total em meses."""
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

    O método atualiza a tabela de resultados, os totais exibidos e os gráficos.
    Recebe a tela atual (`self`) para acessar os campos de entrada e widgets.
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
        meses_plot = []
        saldos = []
        juros_acumulados = []

        total_investido = capital
        total_juros = 0

        self.tabela.setRowCount(0)

        # Data de início usada para calcular o rótulo de cada mês na tabela
        try:
            start_qdate = self.data_inicio.date()
        except Exception:
            start_qdate = QDate.currentDate()

        for mes in range(1, tempo + 1):
            base_calculo = saldo
            rendimento_bruto = base_calculo * (taxa / 100)
            aliquota_ir = aliquota_ir_por_duracao(mes)
            ir = rendimento_bruto * (aliquota_ir / 100)
            rendimento_liquido = rendimento_bruto - ir
            saldo_final = saldo + rendimento_liquido + aporte
            # data correspondente ao mês (começando em start_qdate)
            try:
                qdate_mes = start_qdate.addMonths(mes - 1)
                data_str = qdate_mes.toString("MM/yyyy")
                meses_plot.append(qdate_mes.toPyDate())
            except Exception:
                data_str = str(mes)
                meses_plot.append(mes)
            saldos.append(saldo_final)
            total_investido += aporte
            total_juros += rendimento_liquido
            juros_acumulados.append(total_juros)

            # Preenche tabela
            self.tabela.insertRow(self.tabela.rowCount())
            self.tabela.setItem(self.tabela.rowCount()-1, 0, criar_item(data_str))
            self.tabela.setItem(self.tabela.rowCount()-1, 1, criar_item(f"R$ {saldo:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 2, criar_item(f"R$ {base_calculo:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 3, criar_item(f"R$ {rendimento_bruto:,.2f}"))
            self.tabela.setItem(self.tabela.rowCount()-1, 4, criar_item(f"{aliquota_ir:.1f}%"))
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

        grafico1 = grafico_evolucao(meses_plot, saldos, juros_acumulados)
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
