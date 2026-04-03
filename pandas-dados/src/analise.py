import pandas as pd

def analise_turma(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("turma")
        .agg(
            media_turma=("media", "mean"),
            std_turma=("media", "std"),
            total=("id", "count"),
            aprovados=("aprovado", "sum")
        )
        .assign(
            taxa_aprov=lambda d: (d["aprovados"] / d["total"]) * 100
        )
        .sort_values(by="taxa_aprov", ascending=False)
    )