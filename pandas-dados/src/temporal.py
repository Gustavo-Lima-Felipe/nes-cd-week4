import pandas as pd

def analise_temporal(df: pd.DataFrame):
    df = df.copy()

    df["mes_nasc"] = df["data_nasc"].dt.month

    nascimentos_mes = df["mes_nasc"].value_counts().sort_index()

    idade_turma = (
        df.groupby("turma")["idade"]
        .mean()
        .sort_values(ascending=False)
    )

    correlacao = df["idade"].corr(df["media"])

    return nascimentos_mes, idade_turma, correlacao