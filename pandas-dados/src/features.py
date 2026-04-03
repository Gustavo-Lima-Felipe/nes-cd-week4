import pandas as pd
import numpy as np

def criar_features(df: pd.DataFrame) -> pd.DataFrame:
    hoje = pd.Timestamp.today()

    return (
        df.copy()
        .assign(
            media=lambda d: d[["nota_p1", "nota_p2", "nota_p3"]].mean(axis=1),

            aprovado=lambda d: (
                (d["media"] >= 6.0) &
                d[["nota_p1", "nota_p2", "nota_p3"]].notna().all(axis=1)
            ),

            idade=lambda d: ((hoje - d["data_nasc"]).dt.days // 365),

            faixa_etaria=lambda d: pd.cut(
                d["idade"],
                bins=[0, 18, 25, float("inf")],
                labels=["jovem", "adulto", "sênior"],
                right=False
            )
        )
    )