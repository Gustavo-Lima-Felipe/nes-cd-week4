import pandas as pd

from src.limpeza import limpar
from src.features import criar_features
from src.analise import analise_turma
from src.merge import merge_professores
from src.reshape import reshape_long
from src.temporal import analise_temporal


def main():
    # carregar dados
    df = pd.read_csv("dados_escolares.csv")
    prof = pd.read_csv("professores.csv")

    print("=== DADOS BRUTOS ===")
    print(df.info())
    print(df.isna().sum())

    # pipeline principal
    df = limpar(df)
    df = criar_features(df)

    print("\n=== APÓS LIMPEZA ===")
    print(df.head())

    # Parte 3
    print("\n=== ANÁLISE POR TURMA ===")
    print(analise_turma(df))

    # Parte 4
    print("\n=== MERGE COM PROFESSORES ===")
    merged, sem_prof, media_prof = merge_professores(df, prof)

    print("\nTurmas sem professor:")
    print(sem_prof)

    print("\nMédia por professor:")
    print(media_prof)

    # Parte 5
    print("\n=== FORMATO LONGO ===")
    df_long, media_prova, media_turma_prova = reshape_long(df)

    print("\nExemplo do formato longo:")
    print(df_long.head())

    print("\nMédia por prova:")
    print(media_prova)

    print("\nMédia por turma x prova:")
    print(media_turma_prova)

    # Parte 6
    print("\n=== ANÁLISE TEMPORAL ===")
    nasc_mes, idade_turma, corr = analise_temporal(df)

    print("\nNascimentos por mês:")
    print(nasc_mes)

    print("\nMédia de idade por turma:")
    print(idade_turma)

    print("\nCorrelação idade x média:")
    print(corr)


if __name__ == "__main__":
    main()