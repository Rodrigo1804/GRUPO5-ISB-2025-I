import os
import sys
import glob
import numpy as np
import pandas as pd
import pywt

# 1) Parámetros generales
fs = 1000  # Hz

# 2) Función ADC → mV
def ADC_to_mV(adc, n_bits=10, Vcc=3.3):
    volts = (((adc / (2 ** n_bits)) - 0.5) * Vcc) / 1009
    return volts * 1000  # en mV

# 3) Umbralización mejorada (misma de antes)
def funcion_umbral_mejorada(x, lmbda, mu=0.91, delta=0.01):
    x = np.asarray(x)
    res = np.zeros_like(x)
    mask_zero = np.abs(x) <= lmbda
    res[mask_zero] = 0
    mask_pos = x > lmbda
    x_pos    = x[mask_pos]
    term1 = (np.exp(delta*(lmbda-x_pos))*(lmbda**2) /
             np.sqrt(x_pos**2 - 2*x_pos*np.exp(mu)*(np.exp(lmbda-x_pos)-1)))
    term2 = ((1-np.exp(delta*(lmbda-x_pos)))*
             (lmbda**2)/(x_pos*np.exp(delta*(x_pos-lmbda))))
    res[mask_pos] = x_pos - (term1 + term2)
    mask_neg = x < -lmbda
    x_neg    = x[mask_neg]
    term1 = (np.exp(delta*(lmbda+x_neg))*(lmbda**2) /
             np.sqrt(x_neg**2 + 2*x_neg*np.exp(mu)*(np.exp(lmbda+x_neg)-1)))
    term2 = ((1-np.exp(delta*(lmbda+x_neg)))*
             (lmbda**2)/(-x_neg*np.exp(-delta*(x_neg+ lmbda))))
    res[mask_neg] = x_neg + (term1 - term2)
    return res

def filtrar_emg_dwt(sig, wavelet='sym4', level=10):
    from scipy.signal import butter, filtfilt, iirnotch

    # 1) Band-pass 20–450 Hz
    b, a = butter(4, [20, 450], btype='band', fs=fs)
    sig_bp = filtfilt(b, a, sig)

    # 2) Notch 50 Hz
    b_n, a_n = iirnotch(50, Q=30, fs=fs)
    sig_clean = filtfilt(b_n, a_n, sig_bp)

    # 3) DWT + umbral
    coeffs = pywt.wavedec(sig_clean, wavelet=wavelet, level=level)
    N = len(sig)
    umbrales = []
    for j in range(1, level + 1):
        detail = coeffs[-j]
        sigma = np.median(np.abs(detail)) / 0.6745
        lam = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
        umbrales.insert(0, lam)

    coeffs_f = [coeffs[0]]
    for detail, lam in zip(coeffs[1:], umbrales):
        coeffs_f.append(funcion_umbral_mejorada(detail, lam))

    sig_f = pywt.waverec(coeffs_f, wavelet=wavelet)
    return sig_f[:N]

# 5) Mapeo de nombres
subject_map = {
    'Wen_':      'Sujeto1_',
    'Alejandro_':'Sujeto2_',
    'Aaron_':    'Sujeto3_',
    'Gaby_':     'Sujeto4_'
}

# 6) Rutas
# Ejecuta el script desde la carpeta que contiene "musculos_emg"
cwd = os.getcwd()
input_folder  = os.path.join(cwd, "musculos_emg")
output_root   = os.path.join(cwd, "musculos_emg_filtrado")
ext_folder    = os.path.join(output_root, "Extensor_Filtradas")
flex_folder   = os.path.join(output_root, "Flexor_Filtradas")
os.makedirs(ext_folder, exist_ok=True)
os.makedirs(flex_folder, exist_ok=True)

# 7) Procesamiento
files = glob.glob(os.path.join(input_folder, "*.csv"))
if not files:
    print("No encontré CSVs en", input_folder); sys.exit(1)

for path in files:
    fname = os.path.basename(path)
    # Decidir carpeta de salida
    if "Extensor" in fname:
        out_dir = ext_folder
    elif "Flexor" in fname:
        out_dir = flex_folder
    else:
        print("Omitido (sin extensor/flexor):", fname)
        continue

    # Renombrar sujeto al vuelo
    new_name = fname
    for key,val in subject_map.items():
        if fname.startswith(key):
            new_name = fname.replace(key, val, 1)
            break

    # Leer CSV
    df = pd.read_csv(path, header=0)
    n = len(df)
    # 8) Columna Tiempo estándar
    t = np.arange(n) / fs

    # 9) Columna ADC → mV
    adc   = df.iloc[:, 5].astype(float).to_numpy()
    emg_mV = ADC_to_mV(adc)

    # 10) Filtrar
    emg_mV_filt = filtrar_emg_dwt(emg_mV)

    # 11) Crear y guardar CSV
    out_df = pd.DataFrame({
        "Tiempo": t,
        "EMG_mV_raw": emg_mV,
        "EMG_mV_filtrado": emg_mV_filt
    })
    out_path = os.path.join(out_dir, new_name)
    out_df.to_csv(out_path, index=False)
    print("Guardado →", out_path)

print("¡Proceso completado!")    

'''

# Función para convertir de ADC a milivoltios (mV)
def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC / (2 ** n)) - (1 / 2)) * VCC) / 1009
    return volts * 1000  # Convertir a milivoltios

# Columnas
columnas = ["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG"]
fs = 1000

# Procesamiento general
def procesar_emg_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo, header=None, names=columnas)
    df = df[pd.to_numeric(df["EMG"], errors="coerce").notnull()].copy()
    df["EMG"] = pd.to_numeric(df["EMG"], errors="coerce")
    df["Tiempo"] = np.arange(len(df)) / fs
    df["EMG_mV"] = ADCtomV(df["EMG"])
    return df

# Procesar cada señal
df_Aaron_Reposo_Extensor = procesar_emg_csv("Aaron_Reposo_Extensor.csv")
df_Aaron_Moderado_Extensor = procesar_emg_csv("Aaron_Moderado_Extensor.csv")
df_Aaron_Intenso_Extensor = procesar_emg_csv("Aaron_Intenso_Extensor.csv")

# Mostrar como en la imagen
print("Aaron_Reposo_Extensor:")
print(df_Aaron_Reposo_Extensor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head(), "\n")

print("Aaron_Moderado_Extensor:")
print(df_Aaron_Moderado_Extensor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head(), "\n")

print("Aaron_Intenso_Extensor:")
print(df_Aaron_Intenso_Extensor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head())

df_Aaron_Reposo_Extensor.plot(x="Tiempo", y="EMG")
df_Aaron_Moderado_Extensor.plot(x="Tiempo", y="EMG")
df_Aaron_Intenso_Extensor.plot(x="Tiempo", y="EMG")

"""# Filtrado por DWT"""

# Señal y descomposición DWT ya definidas para extensor Gaby reposo
sig = df_Aaron_Reposo_Extensor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Reposo_Extensor= pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Reposo_Extensor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Reposo_Extensor[-j]  # D1 está al final, D10 al inicio de los detalles
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Reposo_Extensor.insert(0, lambda_j)  # para mantener el orden: D10 → D1

# 4. Función de umbralización mejorada (artículo, ecuación 8)

def funcion_umbral_mejorada(x, lmbda, mu=0.91, delta=0.01):
    x = np.asarray(x)
    res = np.zeros_like(x)

    # |x| <= λ → 0
    mask_zero = np.abs(x) <= lmbda
    res[mask_zero] = 0

    # x > λ
    mask_pos = x > lmbda
    x_pos = x[mask_pos]
    term1 = np.exp(delta * (lmbda - x_pos)) * (lmbda**2) / np.sqrt(x_pos**2 - 2 * x_pos * np.exp(mu) * (np.exp(lmbda - x_pos) - 1))
    term2 = (1 - np.exp(delta * (lmbda - x_pos))) * (lmbda**2) / (x_pos * np.exp(delta * (x_pos - lmbda)))
    res[mask_pos] = x_pos - (term1 + term2)

    # x < -λ
    mask_neg = x < -lmbda
    x_neg = x[mask_neg]
    term1 = np.exp(delta * (lmbda + x_neg)) * (lmbda**2) / np.sqrt(x_neg**2 + 2 * x_neg * np.exp(mu) * (np.exp(lmbda + x_neg) - 1))
    term2 = (1 - np.exp(delta * (lmbda + x_neg))) * (lmbda**2) / (-x_neg * np.exp(-delta * (x_neg + lmbda)))
    res[mask_neg] = x_neg + (term1 - term2)

    return res

# -------------------------------
# 5. Aplicar umbral mejorado a cada nivel de detalle

coeffs_filtrados = [coeffs_df_Aaron_Reposo_Extensor[0]]  # mantener aproximación A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

t = df_Aaron_Reposo_Extensor["Tiempo"].to_numpy()
for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Reposo_Extensor[i]
    lmbda = umbrales_df_Aaron_Reposo_Extensor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# -------------------------------
# 6. Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# -------------------------------
# 7. Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Reposo Extensor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Reposo Extensor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Reposo Extensor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Señal y descomposición DWT para Gaby Moderado Extensor
sig = df_Aaron_Moderado_Extensor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Moderado_Extensor = pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Moderado_Extensor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Moderado_Extensor[-j]  # D1 está al final, D10 al inicio
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Moderado_Extensor.insert(0, lambda_j)  # orden: D10 → D1

# Función de umbralización mejorada (la misma que ya definiste antes)

# Aplicar umbral mejorado a cada nivel (y graficar coeficientes)
coeffs_filtrados = [coeffs_df_Aaron_Moderado_Extensor[0]]  # mantener A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Gaby Moderado Extensor - Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

# Tiempo  para df_Gaby_Moderado_Extensor
t = df_Aaron_Moderado_Extensor["Tiempo"].to_numpy()

# Aplicar función de umbralización mejorada a cada nivel
coeffs_filtrados = [coeffs_df_Aaron_Moderado_Extensor[0]]  # mantener A10

for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Moderado_Extensor[i]
    lmbda = umbrales_df_Aaron_Moderado_Extensor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Moderado Extensor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Moderado Extensor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Moderado Extensor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# df_gaby_Intenso_Extensor
sig = df_Aaron_Intenso_Extensor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Intenso_Extensor = pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Intenso_Extensor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Intenso_Extensor[-j]  # D1 está al final, D10 al inicio
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Intenso_Extensor.insert(0, lambda_j)  # orden: D10 → D1

# Función de umbralización mejorada (la misma que ya definiste antes)

# Aplicar umbral mejorado a cada nivel (y graficar coeficientes)
coeffs_filtrados = [coeffs_df_Aaron_Intenso_Extensor[0]]  # mantener A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Gaby Intenso Extensor - Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

# Tiempo intenso gaby
t = df_Aaron_Intenso_Extensor["Tiempo"].to_numpy()

# Aplicar función de umbralización mejorada a cada nivel
coeffs_filtrados = [coeffs_df_Aaron_Intenso_Extensor[0]]  # mantener A10

for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Intenso_Extensor[i]
    lmbda = umbrales_df_Aaron_Intenso_Extensor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Intenso Extensor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Intenso Extensor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Intenso Extensor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#FLEXOR SUPERFIAL DE LOS DEDOS:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Función para convertir de ADC a milivoltios (mV)
def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC / (2 ** n)) - (1 / 2)) * VCC) / 1009
    return volts * 1000  # Convertir a milivoltios

# Columnas
columnas = ["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG"]
fs = 1000

# Procesamiento general
def procesar_emg_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo, header=None, names=columnas)
    df = df[pd.to_numeric(df["EMG"], errors="coerce").notnull()].copy()
    df["EMG"] = pd.to_numeric(df["EMG"], errors="coerce")
    df["Tiempo"] = np.arange(len(df)) / fs
    df["EMG_mV"] = ADCtomV(df["EMG"])
    return df

# Procesar cada señal
df_Aaron_Reposo_Flexor = procesar_emg_csv("Aaron_Reposo_Flexor.csv")
df_Aaron_Moderado_Flexor = procesar_emg_csv("Aaron_Moderado_Flexor.csv")
df_Aaron_Intensivo_Flexor = procesar_emg_csv("Aaron_Intensivo_Flexor.csv")

# Mostrar como en la imagen
print("Aaron_Reposo_Flexor:")
print(df_Aaron_Reposo_Flexor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head(), "\n")

print("Aaron_Moderado_Flexor:")
print(df_Aaron_Moderado_Flexor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head(), "\n")

print("Aaron_Intensivo_Extensor:")
print(df_Aaron_Intensivo_Flexor[["Tiempo", "0.1", "0.2", "0.3", "0.4", "EMG", "EMG_mV"]].head())

df_Aaron_Reposo_Flexor.plot(x="Tiempo", y="EMG")
df_Aaron_Moderado_Flexor.plot(x="Tiempo", y="EMG")
df_Aaron_Intensivo_Flexor.plot(x="Tiempo", y="EMG")

# Señal y descomposición DWT ya definidas para extensor Gaby reposo
sig = df_Aaron_Reposo_Flexor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Reposo_Flexor= pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Reposo_Flexor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Reposo_Flexor[-j]  # D1 está al final, D10 al inicio de los detalles
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Reposo_Flexor.insert(0, lambda_j)  # para mantener el orden: D10 → D1

# 4. Función de umbralización mejorada (artículo, ecuación 8)

def funcion_umbral_mejorada(x, lmbda, mu=0.91, delta=0.01):
    x = np.asarray(x)
    res = np.zeros_like(x)

    # |x| <= λ → 0
    mask_zero = np.abs(x) <= lmbda
    res[mask_zero] = 0

    # x > λ
    mask_pos = x > lmbda
    x_pos = x[mask_pos]
    term1 = np.exp(delta * (lmbda - x_pos)) * (lmbda**2) / np.sqrt(x_pos**2 - 2 * x_pos * np.exp(mu) * (np.exp(lmbda - x_pos) - 1))
    term2 = (1 - np.exp(delta * (lmbda - x_pos))) * (lmbda**2) / (x_pos * np.exp(delta * (x_pos - lmbda)))
    res[mask_pos] = x_pos - (term1 + term2)

    # x < -λ
    mask_neg = x < -lmbda
    x_neg = x[mask_neg]
    term1 = np.exp(delta * (lmbda + x_neg)) * (lmbda**2) / np.sqrt(x_neg**2 + 2 * x_neg * np.exp(mu) * (np.exp(lmbda + x_neg) - 1))
    term2 = (1 - np.exp(delta * (lmbda + x_neg))) * (lmbda**2) / (-x_neg * np.exp(-delta * (x_neg + lmbda)))
    res[mask_neg] = x_neg + (term1 - term2)

    return res

# -------------------------------
# 5. Aplicar umbral mejorado a cada nivel de detalle

coeffs_filtrados = [coeffs_df_Aaron_Reposo_Flexor[0]]  # mantener aproximación A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

t = df_Aaron_Reposo_Flexor["Tiempo"].to_numpy()
for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Reposo_Flexor[i]
    lmbda = umbrales_df_Aaron_Reposo_Flexor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# -------------------------------
# 6. Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# -------------------------------
# 7. Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Reposo Flexor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Reposo Flexor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Reposo Flexor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Señal y descomposición DWT ya definidas para extensor Gaby reposo
sig = df_Aaron_Moderado_Flexor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Moderado_Flexor= pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Moderado_Flexor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Moderado_Flexor[-j]  # D1 está al final, D10 al inicio de los detalles
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Moderado_Flexor.insert(0, lambda_j)  # para mantener el orden: D10 → D1

# 4. Función de umbralización mejorada (artículo, ecuación 8)

def funcion_umbral_mejorada(x, lmbda, mu=0.91, delta=0.01):
    x = np.asarray(x)
    res = np.zeros_like(x)

    # |x| <= λ → 0
    mask_zero = np.abs(x) <= lmbda
    res[mask_zero] = 0

    # x > λ
    mask_pos = x > lmbda
    x_pos = x[mask_pos]
    term1 = np.exp(delta * (lmbda - x_pos)) * (lmbda**2) / np.sqrt(x_pos**2 - 2 * x_pos * np.exp(mu) * (np.exp(lmbda - x_pos) - 1))
    term2 = (1 - np.exp(delta * (lmbda - x_pos))) * (lmbda**2) / (x_pos * np.exp(delta * (x_pos - lmbda)))
    res[mask_pos] = x_pos - (term1 + term2)

    # x < -λ
    mask_neg = x < -lmbda
    x_neg = x[mask_neg]
    term1 = np.exp(delta * (lmbda + x_neg)) * (lmbda**2) / np.sqrt(x_neg**2 + 2 * x_neg * np.exp(mu) * (np.exp(lmbda + x_neg) - 1))
    term2 = (1 - np.exp(delta * (lmbda + x_neg))) * (lmbda**2) / (-x_neg * np.exp(-delta * (x_neg + lmbda)))
    res[mask_neg] = x_neg + (term1 - term2)

    return res

# -------------------------------
# 5. Aplicar umbral mejorado a cada nivel de detalle

coeffs_filtrados = [coeffs_df_Aaron_Moderado_Flexor[0]]  # mantener aproximación A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

t = df_Aaron_Moderado_Flexor["Tiempo"].to_numpy()
for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Moderado_Flexor[i]
    lmbda = umbrales_df_Aaron_Moderado_Flexor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# -------------------------------
# 6. Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# -------------------------------
# 7. Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Moderado Flexor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Moderado Flexor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Moderado Flexor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Señal y descomposición DWT ya definidas para extensor Gaby reposo
sig = df_Aaron_Intensivo_Flexor["EMG"].to_numpy()
wavelet = 'sym4'
level = 10
coeffs_df_Aaron_Intensivo_Flexor= pywt.wavedec(sig, wavelet, level=level)

# Número total de muestras
N = len(sig)

# Calcular umbrales adaptativos por nivel (D10, D9, ..., D1)
umbrales_df_Aaron_Intensivo_Flexor = []
for j in range(1, level + 1):
    detail_coeffs = coeffs_df_Aaron_Intensivo_Flexor[-j]  # D1 está al final, D10 al inicio de los detalles
    sigma = np.median(np.abs(detail_coeffs)) / 0.6745
    lambda_j = (sigma * np.sqrt(2 * np.log(N))) / np.log(j + 1)
    umbrales_df_Aaron_Intensivo_Flexor.insert(0, lambda_j)  # para mantener el orden: D10 → D1

# 4. Función de umbralización mejorada (artículo, ecuación 8)

def funcion_umbral_mejorada(x, lmbda, mu=0.91, delta=0.01):
    x = np.asarray(x)
    res = np.zeros_like(x)

    # |x| <= λ → 0
    mask_zero = np.abs(x) <= lmbda
    res[mask_zero] = 0

    # x > λ
    mask_pos = x > lmbda
    x_pos = x[mask_pos]
    term1 = np.exp(delta * (lmbda - x_pos)) * (lmbda**2) / np.sqrt(x_pos**2 - 2 * x_pos * np.exp(mu) * (np.exp(lmbda - x_pos) - 1))
    term2 = (1 - np.exp(delta * (lmbda - x_pos))) * (lmbda**2) / (x_pos * np.exp(delta * (x_pos - lmbda)))
    res[mask_pos] = x_pos - (term1 + term2)

    # x < -λ
    mask_neg = x < -lmbda
    x_neg = x[mask_neg]
    term1 = np.exp(delta * (lmbda + x_neg)) * (lmbda**2) / np.sqrt(x_neg**2 + 2 * x_neg * np.exp(mu) * (np.exp(lmbda + x_neg) - 1))
    term2 = (1 - np.exp(delta * (lmbda + x_neg))) * (lmbda**2) / (-x_neg * np.exp(-delta * (x_neg + lmbda)))
    res[mask_neg] = x_neg + (term1 - term2)

    return res

# -------------------------------
# 5. Aplicar umbral mejorado a cada nivel de detalle

coeffs_filtrados = [coeffs_df_Aaron_Intensivo_Flexor[0]]  # mantener aproximación A10

for i, c in enumerate(pywt.wavedec(sig, wavelet, level=level)):
    plt.figure()
    plt.plot(c)
    plt.title(f"Coeficientes del nivel {i} - {'A' if i==0 else 'D'+str(len(coeffs_filtrados)-i)}")

t = df_Aaron_Intensivo_Flexor["Tiempo"].to_numpy()
for i in range(1, level + 1):  # i = 1 → D10, ..., i = 10 → D1
    d = coeffs_df_Aaron_Intensivo_Flexor[i]
    lmbda = umbrales_df_Aaron_Intensivo_Flexor[i - 1]
    d_filtrado = funcion_umbral_mejorada(d, lmbda)
    coeffs_filtrados.append(d_filtrado)

# -------------------------------
# 6. Reconstrucción de la señal filtrada
sig_filtrada = pywt.waverec(coeffs_filtrados, wavelet)

# -------------------------------
# 7. Gráfico comparativo
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:len(sig)], sig, color='blue')
plt.title('Aaron Intensivo Flexor - Señal EMG Original')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], color='green')
plt.title('Aaron Intensivo Flexor - Señal EMG Filtrada (Umbral Mejorado)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:len(sig)], sig, label='Original', alpha=0.7)
plt.plot(t[:len(sig_filtrada)], sig_filtrada[:len(t)], label='Filtrada', alpha=0.7)
plt.title('Aaron Intensivo Flexor - Superposición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
'''
