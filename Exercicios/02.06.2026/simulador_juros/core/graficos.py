import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, MaxNLocator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def grafico_evolucao(meses, saldos, juros, dark_mode=False):
    """
    Gera gráfico de linha mostrando evolução do saldo e dos juros.
    """
    fig = Figure(figsize=(8, 3))
    ax = fig.add_subplot(111)

    # Detecta se a série de X contém objetos de data
    try:
        is_date = hasattr(meses[0], 'year') if meses else False
    except Exception:
        is_date = False

    # Dados presentes?
    has_data = bool(meses and (saldos or juros))

    if is_date and has_data:
        ax.plot(meses, saldos, label="Saldo", color="#2563EB", linewidth=2)
        if juros:
            ax.plot(meses, juros, label="Juros", color="#059669", linewidth=2)
        locator = mdates.AutoDateLocator(minticks=3, maxticks=8)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
    elif has_data:
        ax.plot(meses, saldos, label="Saldo", color="#2563EB", linewidth=2)
        if juros:
            ax.plot(meses, juros, label="Juros", color="#059669", linewidth=2)
        # limita número de ticks e força inteiros para meses
        ax.xaxis.set_major_locator(MaxNLocator(nbins=8, integer=True, prune='both'))
        ax.margins(x=0.02, y=0.05)

    # Títulos e labels
    ax.set_title("Evolução do Investimento", fontsize=14, pad=22)
    ax.set_xlabel("Data" if is_date else "Mês", fontsize=10, labelpad=8)
    ax.set_ylabel("Valor (R$)", fontsize=10)
    def brl_formatter(x, pos):
        try:
            s = f"{x:,.2f}"
        except Exception:
            s = "0.00"
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {s}"

    ax.yaxis.set_major_formatter(FuncFormatter(brl_formatter))

    if not has_data:
        ax.text(
            0.5,
            0.55,
            "Sem dados para plotar",
            ha="center",
            va="center",
            fontsize=12,
            color="#6B7280",
            transform=ax.transAxes,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
    else:
        ax.grid(True, linestyle="--", alpha=0.4)
        if meses and (saldos or juros):
            ax.legend()

    # Tema claro/escuro
    if dark_mode:
        fig.patch.set_facecolor("#1F2937")
        ax.set_facecolor("#111827")
        ax.tick_params(colors="#F9FAFB")
        ax.yaxis.label.set_color("#F9FAFB")
        ax.xaxis.label.set_color("#F9FAFB")
        ax.title.set_color("#F9FAFB")
    else:
        fig.patch.set_facecolor("#F3F4F6")
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(colors="#111827")
        ax.yaxis.label.set_color("#111827")
        ax.xaxis.label.set_color("#111827")
        ax.title.set_color("#111827")

    # formata ticks do eixo X e ajusta margem inferior conforme necessidade
    if is_date:
        fig.autofmt_xdate(rotation=30)
        bottom_margin = 0.22 if len(meses) > 6 else 0.12
    else:
        # para números inteiros, rotaciona pouco
        for label in ax.get_xticklabels():
            label.set_rotation(30)
        bottom_margin = 0.12
    try:
        fig.tight_layout()
        fig.subplots_adjust(top=0.90, bottom=bottom_margin)
    except Exception:
        fig.subplots_adjust(top=0.94, bottom=0.25, left=0.27, right=0.95)
    return FigureCanvas(fig)


def grafico_composicao(aportes, rendimento, dark_mode=False):
    """
    Gera gráfico de pizza mostrando composição entre aportes e rendimento.
    """
    fig = Figure(figsize=(4, 3))
    ax = fig.add_subplot(111)

    if aportes == 0 and rendimento == 0:
        valores = [1]
        labels = ["Sem dados"]
        cores = ["#D1D5DB"]
    else:
        valores = [aportes, rendimento]
        labels = ["Aportes", "Rendimento"]
        cores = ["#2563EB", "#059669"]

    ax.pie(valores, labels=labels, autopct="%1.1f%%", colors=cores, startangle=90)
    ax.set_title("Composição do Montante", fontsize=13, pad=20)

    # Tema claro/escuro
    if dark_mode:
        fig.patch.set_facecolor("#1F2937")
        ax.set_facecolor("#111827")
        ax.title.set_color("#F9FAFB")
    else:
        fig.patch.set_facecolor("#F3F4F6")
        ax.set_facecolor("#FFFFFF")
        ax.title.set_color("#111827")

    try:
        fig.tight_layout()
        fig.subplots_adjust(top=0.90)
    except Exception:
        fig.subplots_adjust(top=0.94, bottom=0.15, left=0.05, right=0.95)
    return FigureCanvas(fig)
