import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
ruta = "musculos_emg_filtrado/Extensor_Filtradas/Sujeto1_Moderado_Extensor.csv"

# Leer el archivo CSV
df = pd.read_csv(ruta)

# Crear la figura con 2 subplots (2 filas, 1 columna)
fig, axs = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# Subplot 1: señal EMG cruda
axs[0].plot(df['Tiempo'], df['EMG_mV_raw'], label='EMG Raw', color='red')
axs[0].set_title('Señal EMG Cruda')
axs[0].set_ylabel('mV')
axs[0].grid(True)

# Subplot 2: señal EMG filtrada
axs[1].plot(df['Tiempo'], df['EMG_mV_filtrado'], label='EMG Filtrada', color='blue')
axs[1].set_title('Señal EMG Filtrada')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_ylabel('mV')
axs[1].grid(True)

# Ajustar el espacio entre subplots
plt.tight_layout()
plt.show()
