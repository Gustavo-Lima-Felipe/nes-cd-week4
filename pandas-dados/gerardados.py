"""
gerar_dados.py
Execute uma vez para criar dados_escolares.csv e professores.csv.
"""

import pandas as pd
import numpy as np

rng = np.random.default_rng(42)
n = 500

nomes = [
    "Naruto Uzumaki",
    "Sasuke Uchiha",
    "Sakura Haruno",
    "Hinata Hyuga",
    "Rock Lee",
    "Neji Hyuga",
    "Shikamaru Nara",
    "Choji Akimichi",
    "Kimimaro Kaguya",
    "Ino Yamanaka",
    "Kiba Inuzuka",
    "Asuma Sarutobi",
]

df = pd.DataFrame(
    {
        "id": range(1, n + 1),
        "nome": rng.choice(nomes, n),
        "turma": rng.choice(["A", "B", "  c", "D", " b"], n),
        "nota_p1": np.where(
            rng.random(n) < 0.08, np.nan, rng.uniform(0, 10, n).round(1)
        ),
        "nota_p2": np.where(
            rng.random(n) < 0.12, np.nan, rng.uniform(0, 10, n).round(1)
        ),
        "nota_p3": np.where(
            rng.random(n) < 0.06, np.nan, rng.uniform(0, 10, n).round(1)
        ),
        "data_nasc": pd.date_range("1998-01-01", periods=n, freq="7D").strftime(
            "%d/%m/%Y"
        ),
        "cidade": rng.choice(
            ["Rio de Janeiro", "Teresina", "Recife", "Maceió"], n
        ),
    }
)

# introduzir duplicatas propositais
df = pd.concat([df, df.sample(20, random_state=0)], ignore_index=True)

df.to_csv("dados_escolares.csv", index=False)
print(f"dados_escolares.csv gerado: {len(df)} linhas.")

# professores (turma D propositalmente ausente → NaN no merge)
professores = pd.DataFrame(
    {
        "turma": ["A", "B", "C"],
        "professor": ["Prof. Jiraya", "Profa. Tsunade", "Prof. Orochimaru"],
    }
)
professores.to_csv("professores.csv", index=False)
print("professores.csv gerado.")