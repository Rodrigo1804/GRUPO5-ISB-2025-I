import pandas as pd

# 1) Cargo el CSV de flexores
df = pd.read_csv("features_flexor.csv")

# 2) Pivot: sujeto × condición con la media de RMS
pivot = (
    df
    .groupby(["sujeto", "condicion"])["RMS"]
    .mean()
    .unstack("condicion")
)

# 3) Calculo el promedio de Moderado e Intenso
pivot["avg_MI"] = pivot[["Moderado", "Intenso"]].mean(axis=1)

# 4) Ordeno de menor a mayor
pivot_sorted = pivot.sort_values("avg_MI")

# 5) Imprimo y guardo en un TXT
print(pivot_sorted)

with open("rms_promedio_por_sujeto.txt", "w") as f:
    f.write(pivot_sorted.to_string())