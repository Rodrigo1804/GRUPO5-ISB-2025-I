import numpy as np
import matplotlib.pyplot as plt
import pywt
import os

# ------------------------ CONFIGURACIÓN ------------------------
ruta_archivo = r"C:\Users\user\OneDrive\Desktop\Universidad\2025-1\ISB\LAB WAVELET\Actividad libre - primeros 4min.txt"
fs = 1000  # Frecuencia de muestreo

# Intervalo de análisis (en segundos)
t_inicio = 0
t_fin = 275
i_inicio = int(t_inicio * fs)
i_fin = int(t_fin * fs)

# ------------------------ 1. SEÑAL RAW (RECORTADA) ------------------------
datos = np.loadtxt(ruta_archivo)
senal = datos[:, 5]  # Canal EEG
senal_segmento = senal[i_inicio:i_fin]
tiempo = np.arange(len(senal_segmento)) / fs + t_inicio  # Tiempo ajustado al segmento

# Aplicar la DWT
niveles = 6
coeficientes = pywt.wavedec(senal_segmento, 'coif5', level=niveles)

# 3. Umbral SURE para cada conjunto de coeficientes de detalle
def sure_threshold(detail_coeffs):
    N = len(detail_coeffs)
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(N))
    return threshold

# 4. Aplicar soft-thresholding con SURE
thresholded_coeffs = [coeficientes[0]]  # mantener coeficientes de aproximación
for i in range(1, len(coeficientes)):
    th = sure_threshold(coeficientes[i])
    coeffs_thresh = pywt.threshold(coeficientes[i], th, mode='soft')
    thresholded_coeffs.append(coeffs_thresh)

# 5. Reconstruir la señal
sig_filtered = pywt.waverec(thresholded_coeffs, 'coif5')

# 6. Visualización
plt.subplot(2,1,1)
plt.plot(tiempo, senal_segmento, label='Original')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.xlim(tiempo[0], tiempo[-1])
plt.title("Señal Original - Tarea Cognitiva")


plt.subplot(2,1,2)
plt.plot(tiempo[:len(sig_filtered)], sig_filtered[:len(tiempo)], label='Filtrada (DWT + SURE)', linewidth=2)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal Filtrada - Actividad Libre (escuchar distintos tipos de música)")
plt.xlim(tiempo[0], tiempo[-1])
plt.grid(ls=':')
plt.tight_layout()
plt.show()
