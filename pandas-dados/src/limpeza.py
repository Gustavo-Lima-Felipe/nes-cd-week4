import pandas as pd

def limpar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = df.columns.str.strip()

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    df["turma"] = df["turma"].str.upper().str.strip()

    df["data_nasc"] = pd.to_datetime(
        df["data_nasc"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    df = df.drop_duplicates()

    return df