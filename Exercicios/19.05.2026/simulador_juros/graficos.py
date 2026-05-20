import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Função para formatar valores em reais
def formatar_reais(valor, pos):
    return f"R$ {valor:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

def grafico_evolucao(meses, saldos, juros):
    fig, ax = plt.subplots(figsize=(5.5, 3))
    ax.plot(meses, saldos, label="Saldo Total", color="#2563EB", linewidth=2)
    ax.plot(meses, juros, label="Juros Acumulados", color="#059669", linewidth=2)

    # Título centralizado e espaço livre acima
    ax.set_title("Evolução Mensal do Investimento", fontsize=10, pad=15)
    ax.set_xlabel("Meses", fontsize=10, labelpad=10)
    ax.set_ylabel("Valor (R$)", fontsize=10, labelpad=10)
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.4)

    # Formatação dos valores em reais
    ax.yaxis.set_major_formatter(FuncFormatter(formatar_reais))

    # 🔢 Ajuste dos rótulos do eixo X
    # Mostra no máximo 10 rótulos bem espaçados
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.tick_params(axis="x", labelrotation=45, labelsize=8, pad=8)
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    # 🔧 Ajuste de margens para liberar o topo e dar espaço abaixo
    fig.subplots_adjust(top=0.85, bottom=0.28, left=0.12, right=0.95)

    return FigureCanvas(fig)

def grafico_composicao(total_investido, total_juros):
    fig, ax = plt.subplots(figsize=(2.8, 2.8))

    if total_investido == 0 and total_juros == 0:
        valores = [1]
        labels = ["Sem dados"]
        cores = ["#D1D5DB"]
    else:
        valores = [total_investido, total_juros]
        labels = ["Investido", "Juros"]
        cores = ["#059669", "#2563EB"]

    wedges, texts, autotexts = ax.pie(
        valores, labels=labels, autopct="%1.1f%%", colors=cores,
        startangle=90, textprops={"fontsize": 8}
    )
    ax.set_title("Composição do Patrimônio", fontsize=9, pad=10)
    fig.subplots_adjust(top=0.9, bottom=0.1)
    return FigureCanvas(fig)
