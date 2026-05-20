from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from graficos import grafico_evolucao, grafico_composicao

def calcular_juros(widget):
    try:
        valor_inicial = float(widget.valor_inicial.text())
        aporte_mensal = float(widget.aporte_mensal.text())
        taxa = float(widget.taxa_juros.text()) / 100
        tipo_taxa = widget.tipo_taxa.currentText()
        tempo = int(widget.tempo.text())
        tipo_tempo = widget.tipo_tempo.currentText()

        if tipo_taxa == "Anual":
            taxa /= 12
        if tipo_tempo == "Anos":
            tempo *= 12

        if widget.data_inicio.text():
            data_inicio = datetime.strptime(widget.data_inicio.text(), "%d/%m/%Y")
        else:
            data_inicio = datetime.now()

        saldo = valor_inicial
        total_investido = valor_inicial
        total_juros = 0

        widget.tabela.setRowCount(tempo)

        ano = data_inicio.year
        mes = data_inicio.month

        lista_meses = []
        lista_saldos = []
        lista_juros = []

        for i in range(tempo):
            base_calculo = saldo + aporte_mensal
            rendimento_bruto = base_calculo * taxa

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
                widget.tabela.setItem(i, j, QTableWidgetItem(valor))

            saldo = saldo_final

            lista_meses.append(mes_label)
            lista_saldos.append(saldo_final)
            lista_juros.append(total_juros)

        widget.card_juros.valor_label.setText(f"R$ {total_juros:,.2f}")
        widget.card_investido.valor_label.setText(f"R$ {total_investido:,.2f}")
        widget.card_final.valor_label.setText(f"R$ {saldo:,.2f}")

        # Limpa gráficos antigos
        while widget.layout_graficos.count():
            item = widget.layout_graficos.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Adiciona novos gráficos
        widget.layout_graficos.addWidget(grafico_evolucao(lista_meses, lista_saldos, lista_juros))
        widget.layout_graficos.addWidget(grafico_composicao(total_investido, total_juros))

    except ValueError:
        QMessageBox.warning(widget, "Erro", "Por favor, insira valores válidos.")
