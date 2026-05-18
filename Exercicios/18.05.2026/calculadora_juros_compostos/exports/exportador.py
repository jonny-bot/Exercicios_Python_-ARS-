import pandas as pd


def exportar_csv(
    historico,
    caminho="simulacao.csv"
):

    df = pd.DataFrame(historico)

    df.to_csv(
        caminho,
        index=False,
        sep=";"
    )


def exportar_excel(
    historico,
    caminho="simulacao.xlsx"
):

    df = pd.DataFrame(historico)

    df.to_excel(
        caminho,
        index=False
    )


def exportar_json(
    historico,
    caminho="simulacao.json"
):

    df = pd.DataFrame(historico)

    df.to_json(
        caminho,
        orient="records",
        indent=4
    )
    