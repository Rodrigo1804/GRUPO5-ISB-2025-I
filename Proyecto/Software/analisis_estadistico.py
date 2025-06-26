#!/usr/bin/env python3
# analisis_estadistico.py

import glob
import pandas as pd
from scipy.stats import shapiro, levene, f_oneway, friedmanchisquare

# --- Configuración de salida ---
LOGFILE = "analisis_estadistico.txt"
log = open(LOGFILE, "w")

def say(msg="", end="\n"):
    print(msg, end=end)
    log.write(msg + end)

# --- Configuración ---
FEATURE_FILES = sorted(glob.glob("features_*.csv"))
FEATURE_LIST  = ["RMS", "MAV", "WL", "ZC", "SSC", "WAMP", "MNF", "MDF", "Power"]
CONDICIONES   = ["Reposo", "Moderado", "Intenso"]

if __name__ == "__main__":
    for feat_file in FEATURE_FILES:
        df = pd.read_csv(feat_file)
        muscle = feat_file.replace("features_", "").replace(".csv", "")
        say("\n" + "="*30)
        say(f"Análisis estadístico — {muscle.capitalize()}")
        say("="*30)

        for feat in FEATURE_LIST:
            # Pivot y agrupación
            pivot = (
                df.groupby(["sujeto", "condicion"])[feat]
                  .mean()
                  .unstack("condicion")
                  .reindex(columns=CONDICIONES)
                  .dropna()
            )
            if pivot.empty:
                say(f"\n▶ {feat}: datos incompletos, salto.")
                continue
            data = [pivot[c].values for c in CONDICIONES]

            # Normalidad
            say(f"\n▶ {feat}:")
            normal = True
            for cond, arr in zip(CONDICIONES, data):
                stat, p = shapiro(arr)
                say(f"    Shapiro {cond}: p = {p:.3f}")
                if p < 0.05:
                    normal = False

            # Homocedasticidad
            stat, p = levene(*data)
            homo = (p >= 0.05)
            say(f"    Levene homoced.: p = {p:.3f}")

            # Prueba inferencial
            if normal and homo:
                stat, p = f_oneway(*data)
                say(f"    ANOVA: F = {stat:.3f}, p = {p:.3f}")
            else:
                stat, p = friedmanchisquare(*data)
                say(f"    Friedman: χ² = {stat:.3f}, p = {p:.3f}")

    # mensaje final antes de cerrar el log
    say("\n¡Análisis completado! (detalle en " + LOGFILE + ")")
    log.close()