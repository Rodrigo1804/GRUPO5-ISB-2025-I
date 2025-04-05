import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#Parámetros para dominio del tiempo
durationn = 10
sampling_rate = 1000
tiempo = np.linspace(0,durationn,durationn*sampling_rate)

#Simular señales ECG
ecg_simple_80 = nk.ecg_simulate(duration=durationn, heart_rate=80, method="simple")
ecg_simple_120 = nk.ecg_simulate(duration=durationn, heart_rate=120, method="simple")
ecg_complex_80 = nk.ecg_simulate(duration=durationn, heart_rate=80, method="ecgsyn")
ecg_complex_120 = nk.ecg_simulate(duration=durationn, heart_rate=120, method="ecgsyn")

#Calcular FFT
frequencies = np.fft.fftfreq(len(tiempo), d=1/sampling_rate)

fft_simple_80 = np.abs(np.fft.fft(ecg_simple_80))
fft_simple_120 = np.abs(np.fft.fft(ecg_simple_120))
fft_complex_80 = np.abs(np.fft.fft(ecg_complex_80))
fft_complex_120 = np.abs(np.fft.fft(ecg_complex_120))

#Visualizar con índice de tiempo en segundos
ecg_df = pd.DataFrame({"ECG_Simple_80bpm": ecg_simple_80,
                       "ECG_Simple_120bpm": ecg_simple_120,
                       "ECG_Complex_80bpm": ecg_complex_80,
                       "ECG_Complex_120bpm": ecg_complex_120}, index=tiempo)

#Visualizar en dominio de la frecuencia
fft_df = pd.DataFrame({"ECG_Simple_80bpm": fft_simple_80,
                       "ECG_Simple_120bpm": fft_simple_120,
                       "ECG_Complex_80bpm": fft_complex_80,
                       "ECG_Complex_120bpm": fft_complex_120}, index=frequencies)

#Ordenar el índice para que vaya de -f a +f
fft_df = fft_df.sort_index()
#Graficar
nk.signal_plot(ecg_df,subplots=True)
plt.suptitle("Comparación de Señales ECG Simuladas (Dominio del tiempo)", fontsize=16)
plt.xlabel("Tiempo (s)")
plt.tight_layout(rect=[0, 0, 1, 0.96]) #Para organizar cada gráfica con sus etiquetas
plt.show()

nk.signal_plot(fft_df,subplots=True)
plt.suptitle("Comparación de Señales ECG Simuladas (Dominio de la frecuencia)", fontsize=16)
plt.xlabel("Frecuencia (Hz)")
plt.tight_layout(rect=[0, 0, 1, 0.96]) 
plt.show()

