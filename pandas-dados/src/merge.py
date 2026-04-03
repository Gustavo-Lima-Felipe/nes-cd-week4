import pandas as pd

def merge_professores(df_alunos: pd.DataFrame, df_prof: pd.DataFrame):
    df_merged = pd.merge(df_alunos, df_prof, on="turma", how="left")

    sem_prof = df_merged[df_merged["professor"].isna()]["turma"].unique()

    media_prof = (
        df_merged.dropna(subset=["professor"])
        .groupby("professor")
        .agg(media=("media", "mean"))
        .sort_values(by="media", ascending=False)
    )

    return df_merged, sem_prof, media_prof