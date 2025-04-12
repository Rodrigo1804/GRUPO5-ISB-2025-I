import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from scipy.signal import butter, filtfilt, lfilter, iirnotch

# Archivos enlistados :)
archivos = {
    "Bíceps": "EMG_Bicep.txt",
    "Tríceps": "EMG_Triceps.txt",
    "Hombro": "EMG_Hombro.txt"
}

# Funciones 

# Para leer las señales de OpenSignals y separar cabecera de datos 
def leer_senal_opensignals(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    # Buscar JSON con metadatos
    for linea in lineas:
        if linea.startswith('# {'):
            json_data = json.loads(linea[2:])
            break

    device_key = list(json_data.keys())[0]
    fs = json_data[device_key]["sampling rate"]
    titulo = json_data[device_key]["label"]

    # Encontrar línea de inicio de datos
    inicio_datos = 0
    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break

    # Leer datos como DataFrame
    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)
    tiempo = np.arange(len(data)) / fs
    senal = data.iloc[:, -1]  # Suponiendo que A1 está al final

    return tiempo, senal, fs, titulo

#Pasar de ADC a voltios y centrar en 0
def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC / (2**n)) - 0.5) * VCC) / 1009
    return volts * 1000

# Crear filtros 
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    return butter(order, [low, high], btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    return lfilter(b, a, data)


def graficar_senal(tiempo, senal, fs, titulo):
    signalmV = ADCtomV(senal)
    pre_pro_signal = signalmV - np.mean(signalmV)

    # Filtro pasa banda 100–300 Hz
    low_cutoff = 100.0
    high_cutoff = 300.0
    smooth_signal = butter_bandpass_filter(pre_pro_signal, low_cutoff, high_cutoff, fs)

    # Filtro notch 60 Hz
    b_notch, a_notch = iirnotch(60.0, 30.0, fs)
    smooth_signal = filtfilt(b_notch, a_notch, smooth_signal)

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(tiempo, signalmV, label='Señal original')
    plt.title(f'Señal EMG - {titulo}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (mV)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(tiempo, smooth_signal, label='Señal filtrada', color='red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud filtrada (mV)')
    plt.grid(True)
    plt.legend()

    # FFT
    n = len(smooth_signal)
    fft = np.fft.fft(smooth_signal)
    fft_magnitud = np.abs(fft)[:n//2]
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    fft_db = 20 * np.log10(fft_magnitud + 1e-6)  # evitar log(0)

    plt.subplot(3, 1, 3)
    plt.plot(freqs, fft_db, label='FFT', color='black')
    plt.title("FFT de la Señal Filtrada")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Para que suceda todo automaticamente 
for etiqueta, archivo in archivos.items():
    tiempo, senal, fs, titulo = leer_senal_opensignals(archivo)
    graficar_senal(tiempo, senal, fs, titulo)