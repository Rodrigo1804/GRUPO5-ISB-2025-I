import numpy as np
import matplotlib.pyplot as plt
import pywt
import os
from scipy.optimize import minimize_scalar

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

# ------------------------ 2. DWT ------------------------
niveles = 6
wavelet = 'coif5'
coeficientes = pywt.wavedec(senal_segmento, wavelet, level=niveles)

# ------------------------ 3. SURE Thresholding Real ------------------------
def sure_function(detail_coeffs, sigma, lam):
    n = len(detail_coeffs)
    term1 = n * sigma**2
    term2 = np.sum(np.minimum(detail_coeffs**2, lam**2))
    term3 = 2 * sigma**2 * np.sum(np.abs(detail_coeffs) < lam)
    return term1 + term2 - term3

def compute_sure_threshold(detail_coeffs):
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    result = minimize_scalar(
        lambda lam: sure_function(detail_coeffs, sigma, lam),
        bounds=(0, np.max(np.abs(detail_coeffs))),
        method='bounded'
    )
    return result.x  # umbral óptimo

# ------------------------ 4. Umbralización nivel por nivel ------------------------
thresholded_coeffs = [coeficientes[0]]  # conservar la aproximación (A6)
for i in range(1, len(coeficientes)):
    th = compute_sure_threshold(coeficientes[i])
    coeffs_thresh = pywt.threshold(coeficientes[i], th, mode='soft')
    thresholded_coeffs.append(coeffs_thresh)

# ------------------------ 5. Reconstrucción ------------------------
sig_filtered = pywt.waverec(thresholded_coeffs, wavelet)

# ------------------------ 6. Visualización ------------------------
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tiempo, senal_segmento, label='Original')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.xlim(tiempo[0], tiempo[-1])
plt.title("Señal Original - Tarea Cognitiva")

plt.subplot(2, 1, 2)
plt.plot(tiempo[:len(sig_filtered)], sig_filtered[:len(tiempo)], label='Filtrada (DWT + SURE)', linewidth=2)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal Filtrada - Actividad Libre (escuchar distintos tipos de música)")
plt.xlim(tiempo[0], tiempo[-1])
plt.grid(ls=':')
plt.tight_layout()
plt.show()
