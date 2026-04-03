import pandas as pd

def reshape_long(df: pd.DataFrame):
    df_long = pd.melt(
        df,
        id_vars=["id", "nome", "turma"],
        value_vars=["nota_p1", "nota_p2", "nota_p3"],
        var_name="prova",
        value_name="nota"
    )

    df_long["prova"] = df_long["prova"].str.replace("nota_", "")

    media_prova = df_long.groupby("prova")["nota"].mean()

    media_turma_prova = (
        df_long.groupby(["turma", "prova"])["nota"]
        .mean()
        .unstack()
    )

    return df_long, media_prova, media_turma_prova