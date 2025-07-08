import streamlit as st
import pandas as pd
import requests
import glob
from proces import procesar_archivos 

st.title("Evaluación electromiográfica de la fatiga muscular del miembro superior durante el uso del smartphone")
st.write("Esta es una interfaz básica para mostrar los datos EMG recolectados para el proyecto del curso de Introducción a Señales Biomédicas.")

st.title("Visualización de EMG")

archivos = {
    "Sujeto1": {
        "Extensor Radial Largo del Carpo (ECRL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto1_Reposo_Extensor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto1_Intenso_Extensor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto1_Moderado_Extensor.csv"
        },
        "Flexor Largo del Dedo Pulgar (FPL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto1_Reposo_Flexor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto1_Intenso_Flexor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto1_Moderado_Flexor.csv"
        },
    },
    "Sujeto2": {
        "Extensor Radial Largo del Carpo (ECRL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto2_Reposo_Extensor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto2_Intenso_Extensor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto2_Moderado_Extensor.csv"
        },
        "Flexor Largo del Dedo Pulgar (FPL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto2_Reposo_Flexor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto2_Intenso_Flexor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto2_Moderado_Flexor.csv"
        },
    },
    "Sujeto3": {
        "Extensor Radial Largo del Carpo (ECRL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto3_Reposo_Extensor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto3_Intenso_Extensor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto3_Moderado_Extensor.csv"
        },
        "Flexor Largo del Dedo Pulgar (FPL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto3_Reposo_Flexor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto3_Intenso_Flexor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto3_Moderado_Flexor.csv"
        },
    },
    "Sujeto4": {
        "Extensor Radial Largo del Carpo (ECRL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto4_Reposo_Extensor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto4_Intenso_Extensor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Extensor/Sujeto4_Moderado_Extensor.csv"
        },
        "Flexor Largo del Dedo Pulgar (FPL)": {
            "Reposo": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto4_Reposo_Flexor.csv",
            "Intenso": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto4_Intenso_Flexor.csv",
            "Moderado": "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/Se%C3%B1ales/EMG_Flexor/Sujeto4_Moderado_Flexor.csv"
        },
    },
}


# Cargar archivos CSV desde GitHub (extensor y flexor)
flex_csv = "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/features_flexor.csv"
ext_csv = "https://raw.githubusercontent.com/Rodrigo1804/GRUPO5-ISB-2025-I/refs/heads/main/Proyecto/Software/features_extensor.csv"



# Procesar los archivos
resultados_ext = procesar_archivos(ext_csv)
resultados_flex = procesar_archivos(flex_csv)


# Características a analizar
FEATURE_LIST = ["RMS", "MAV", "WL", "ZC", "SSC", "WAMP", "MNF", "MDF", "Power"]
CONDICIONES = ["Moderado", "Intenso"]

# Crear columnas
col1, col2 = st.columns(2)
# Columna 1: Selección de opciones
with col1:
    # Selección de sujeto
    seleccion_sujeto = st.selectbox("Selecciona un sujeto:", list(archivos.keys()))

    # Selección de músculo
    músculos = list(archivos[seleccion_sujeto].keys())
    seleccion_musculo = st.selectbox("Selecciona un músculo:", músculos)

    # Selección de etapa
    etapas = list(archivos[seleccion_sujeto][seleccion_musculo].keys())
    seleccion_etapa = st.selectbox("Selecciona la etapa:", etapas)

    # Cargar archivo correspondiente
    url = archivos[seleccion_sujeto][seleccion_musculo][seleccion_etapa]
    df = pd.read_csv(url)

    # Selección de columna para graficar
    columna = st.selectbox("Selecciona la columna para graficar:", ['EMG_mV_raw', 'EMG_mV_filtrado'])


    st.title("Análisis estadístico")

    # --- Análisis para el músculo Extensor ---
    st.subheader("Análisis de características para el músculo Extensor")
    # Mostrar los resultados en una tabla
    st.write(resultados_ext)

     # --- Clasificación por RMS medio ---
    st.subheader("Clasificación por RMS medio")
    rms_data = {
        "Sujeto": ["Sujeto2", "Sujeto3", "Sujeto4", "Sujeto1"],
        "Moderado": [0.01103, 0.01262, 0.01395, 0.01609],
        "Intenso": [0.00622, 0.01666, 0.01896, 0.02297],
        "avg_MI": [0.00862, 0.01464, 0.01646, 0.01953],
        "Grupo": ["Uso Regular", "Uso Regular", "Uso Ocasional", "Uso Ocasional"]
    }

    rms_df = pd.DataFrame(rms_data)
    st.write(rms_df)

# Columna 2: Mostrar las gráficas
with col2:
    # Graficar la señal EMG seleccionada
    st.subheader(f"Gráfico de {columna} para {seleccion_sujeto} - {seleccion_musculo} - {seleccion_etapa}")
    st.line_chart(df.set_index('Tiempo')[columna])
    # --- Análisis para el músculo Flexor ---
    st.subheader("Análisis de características para el músculo Flexor")
    st.write(resultados_flex)

    # --- Resultados SAS-SV ---
    st.subheader("Resultados SAS-SV")
    sas_data = {
        "Participante": ["Sujeto4", "Sujeto1", "Sujeto2", "Sujeto3"],
        "Sexo": ["Mujer", "Mujer", "Hombre", "Hombre"],
        "Puntaje SAS-SV": [26, 24, 37, 36],
        "Clasificación": ["Ocasional", "Ocasional", "Intensivo", "Intensivo"]
    }

    sas_df = pd.DataFrame(sas_data)
    st.write(sas_df)