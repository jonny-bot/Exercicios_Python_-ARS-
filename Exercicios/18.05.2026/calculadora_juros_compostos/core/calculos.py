def obter_aliquota_ir(meses):

    if meses <= 6:
        return 0.225

    elif meses <= 12:
        return 0.20

    elif meses <= 24:
        return 0.175

    return 0.15


def converter_taxa_mensal(
    taxa,
    tipo
):

    if tipo == "mensal":
        return taxa / 100

    return (
        (1 + taxa / 100)
        ** (1 / 12)
    ) - 1


def calcular_simulacao(
    valor_inicial,
    aporte,
    rendimento,
    tipo_taxa,
    tempo,
    tipo_tempo
):

    if tipo_tempo == "anos":
        meses = tempo * 12

    else:
        meses = tempo

    taxa_mensal = converter_taxa_mensal(
        rendimento,
        tipo_taxa
    )

    aliquota = obter_aliquota_ir(
        meses
    )

    saldo = valor_inicial

    total_ir = 0
    total_juros = 0

    historico = []

    for mes in range(1, meses + 1):

        saldo_inicial = saldo

        base = saldo + aporte

        bruto = (
            base * taxa_mensal
        )

        ir = bruto * aliquota

        liquido = bruto - ir

        saldo = (
            base + liquido
        )

        total_ir += ir
        total_juros += liquido

        historico.append({

            "mes": mes,

            "saldo_inicial":
                round(saldo_inicial, 2),

            "base_calculo":
                round(base, 2),

            "rendimento_bruto":
                round(bruto, 2),

            "ir":
                round(ir, 2),

            "rendimento_liquido":
                round(liquido, 2),

            "saldo_final":
                round(saldo, 2)
        })

    total_investido = (
        valor_inicial +
        (aporte * meses)
    )

    ultimo_rendimento = historico[-1][
        "rendimento_liquido"
]

    return {

        "saldo_final": saldo,

        "total_investido":
            total_investido,

        "total_juros":
            total_juros,

        "total_ir":
            total_ir,

        "ultimo_rendimento":
            ultimo_rendimento,

        "historico":
            historico
    }
    