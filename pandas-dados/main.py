import pandas as pd

from src.limpeza import limpar
from src.features import criar_features
from src.analise import analise_turma
from src.merge import merge_professores
from src.reshape import reshape_long
from src.temporal import analise_temporal


def main():
    df = pd.read_csv("dados_escolares.csv")
    prof = pd.read_csv("professores.csv")

    df = limpar(df)
    df = criar_features(df)

    print("\n=== ANÁLISE POR TURMA ===")
    print(analise_turma(df))

    print("\n=== MERGE ===")
    merged, sem_prof, media_prof = merge_professores(df, prof)
    print("Turmas sem professor:", sem_prof)
    print(media_prof)

    print("\n=== RESHAPE ===")
    df_long, media_prova, media_turma_prova = reshape_long(df)
    print(media_prova)
    print(media_turma_prova)

    print("\n=== TEMPORAL ===")
    nasc_mes, idade_turma, corr = analise_temporal(df)
    print(nasc_mes)
    print(idade_turma)
    print("Correlação idade x média:", corr)


if __name__ == "__main__":
    main()