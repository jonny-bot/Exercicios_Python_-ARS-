# graficos.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def grafico_evolucao(meses, saldos, juros):
    """
    Gera gráfico de linha mostrando evolução do saldo e dos juros.
    """
    fig, ax = plt.subplots(figsize=(5, 3))

    if meses and saldos:
        ax.plot(meses, saldos, label="Saldo", color="#2563EB", linewidth=2)
    if meses and juros:
        ax.plot(meses, juros, label="Juros", color="#059669", linewidth=2)

    ax.set_title("Evolução do Investimento", fontsize=12, pad=15)
    ax.set_xlabel("Meses", fontsize=10)
    ax.set_ylabel("Valor (R$)", fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.4)
    if meses and (saldos or juros):
        ax.legend()

    fig.subplots_adjust(top=0.85, bottom=0.25, left=0.12, right=0.95)
    return FigureCanvas(fig)


def grafico_composicao(aportes, rendimento):
    """
    Gera gráfico de pizza mostrando composição entre aportes e rendimento.
    Se ambos forem zero, mostra um gráfico vazio.
    """
    fig, ax = plt.subplots(figsize=(4, 3))

    if aportes == 0 and rendimento == 0:
        # Caso inicial sem dados
        valores = [1]
        labels = ["Sem dados"]
        cores = ["#D1D5DB"]
    else:
        valores = [aportes, rendimento]
        labels = ["Aportes", "Rendimento"]
        cores = ["#2563EB", "#059669"]

    ax.pie(valores, labels=labels, autopct="%1.1f%%", colors=cores, startangle=90)
    ax.set_title("Composição do Montante", fontsize=12, pad=15)

    fig.subplots_adjust(top=0.85, bottom=0.15, left=0.05, right=0.95)
    return FigureCanvas(fig)
