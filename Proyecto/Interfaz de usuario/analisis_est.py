import pandas as pd
from scipy.stats import shapiro, levene, f_oneway, friedmanchisquare

# --- Función para realizar el análisis estadístico ---
def realizar_analisis(df, feature, condiciones=["Reposo", "Moderado", "Intenso"]):
    # Limpiar los nombres de las columnas para evitar espacios extra
    df.columns = df.columns.str.strip()

    # Verificar si la columna `feature` existe en el DataFrame
    if feature not in df.columns:
        return None

    # Pivot y agrupación por sujeto y condición
    pivot = (
        df.groupby(["sujeto", "condicion"])[feature]
        .mean()
        .unstack("condicion")
        .reindex(columns=condiciones)
        .dropna()
    )
    
    if pivot.empty:
        return None  # Si no hay datos, devuelve None

    # Datos para la prueba
    data = [pivot[c].values for c in condiciones]
    
    # Evaluación de normalidad (Shapiro)
    normal = True
    for cond, arr in zip(condiciones, data):
        stat, p = shapiro(arr)
        if p < 0.05:
            normal = False  # Si al menos uno es no normal, cambiar a False
    
    # Evaluación de homocedasticidad (Levene)
    stat_levene, p_levene = levene(*data)
    homocedasticidad = (p_levene >= 0.05)
    
    # Decidir la prueba a usar: ANOVA o Friedman
    if normal and homocedasticidad:
        # Usamos ANOVA
        stat_prueba, p_prueba = f_oneway(*data)
        prueba = "ANOVA"
        estadistico = f"F = {stat_prueba:.3f}"
    else:
        # Usamos Friedman
        stat_prueba, p_prueba = friedmanchisquare(*data)
        prueba = "Friedman"
        estadistico = f"χ² = {stat_prueba:.3f}"

    # Determinar Significancia
    if p_prueba < 0.05:
        significancia = "Significativa"
    elif p_prueba >= 0.05 and p_prueba < 0.1:
        significancia = "Tendencia (p ≈ 0.06)"
    else:
        significancia = "No significativa"
    
    # Crear un diccionario con los resultados
    resultados = {
        "Feature": feature,
        "Prueba": prueba,
        "Estadístico": estadistico,
        "p-valor": p_prueba,
        "Significancia": significancia
    }
    
    return resultados

