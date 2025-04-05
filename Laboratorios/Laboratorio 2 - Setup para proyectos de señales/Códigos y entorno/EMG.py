import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros para dominio del tiempo
duration = 10
sampling_rate = 1000
tiempo = np.linspace(0, duration, duration * sampling_rate)

# Simular señales EMG (forzando conversión a array)
emg3 = np.asarray(nk.emg_simulate(duration=duration, burst_number=3, burst_duration=1.0))
emg4_long = np.asarray(nk.emg_simulate(duration=duration, burst_number=4, burst_duration=1.5))
emg5 = np.asarray(nk.emg_simulate(duration=duration, burst_number=5, burst_duration=1.0))
emg6_short = np.asarray(nk.emg_simulate(duration=duration, burst_number=6, burst_duration=0.5))

# Crear DataFrame con índice de tiempo
emg_df = pd.DataFrame({
    "EMG_3bursts": emg3,
    "EMG_4bursts_long": emg4_long,
    "EMG_5bursts": emg5,
    "EMG_6bursts_short": emg6_short
}, index=tiempo)

# Graficar
nk.signal_plot(emg_df, subplots=True)
plt.suptitle("Comparación de Señales EMG Simuladas (Dominio del Tiempo)", fontsize=16)
plt.xlabel("Tiempo (s)")
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
