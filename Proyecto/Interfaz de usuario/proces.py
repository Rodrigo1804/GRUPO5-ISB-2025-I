import pandas as pd
import requests
from io import StringIO
from analisis_est import realizar_analisis

def procesar_archivos(feat_files):
    df = df = pd.read_csv(feat_files)
    if df is not None:
        resultados_totales = []

        # Iterar sobre las características (Features)
        for feature in ["RMS", "MAV", "WL", "ZC", "SSC", "WAMP", "MNF", "MDF", "Power"]:
            resultados = realizar_analisis(df, feature)
            if resultados:
                resultados_totales.append(resultados)
        
        # Convertir los resultados en un DataFrame para facilitar su uso
        resultados_df = pd.DataFrame(resultados_totales)
        return resultados_df
    else:
        return None