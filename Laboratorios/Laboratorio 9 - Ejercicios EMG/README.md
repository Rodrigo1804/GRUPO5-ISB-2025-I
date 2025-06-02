# Laboratorio de EMG 

# Ejercicio A: Simulación de distintos grados de asimetría

## Objetivo de la práctica
Estudiar cómo varía el *Symmetry Ratio* al alterar la amplitud relativa de la señal EMG del músculo izquierdo. El objetivo es observar el impacto de distintos niveles de desbalance en la simetría muscular, un aspecto clave en contextos clínicos como la rehabilitación neuromuscular.

## Metodología
1. Se simuló una señal EMG base con las siguientes consideraciones:
   - Duración: 10 segundos
   - Frecuencia de muestreo: 1000 Hz
   - Número de ráfagas musculares (bursts): 10
   - Ruido blanco: 0.01

Para realizar esto primero debimos importar las librerías correspondientes al neurokit2, que nos permite ismular señales 
```
!pip install neurokit2
## Importamos librerías necesarias
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, integrate
```

Luego se generó la señal base y se crearon 5 pares de señales:
```
# Parámetros de simulación
fs = 1000  # Frecuencia de muestreo (Hz)
duration = 15  # Duración de la señal (segundos)
burst_number = 10  # Número de ráfagas musculares
noise = 0.01  # Nivel de ruido blanco
scales = [0.2, 0.4, 0.6, 0.8, 1.0]  # Escalas de amplitud del segundo canal

# Generar señal EMG base
emg_base = nk.emg_simulate(duration=duration, burst_number=burst_number, noise=noise, sampling_rate=fs)

# Crear los pares de señales escaladas
pares = []
for factor in scales:
    canal1 = emg_base.copy()
    canal2 = signal.resample(emg_base * factor, len(emg_base))  # misma longitud, escalado
    pares.append((canal1, canal2))
```

2. Visualización de las señales simuladas
```
# Graficar los pares de señales simuladas
plt.figure(figsize=(14, 10))
for i, (canal1, canal2) in enumerate(pares):
    plt.subplot(5, 1, i + 1)
    plt.plot(canal1, label="Canal 1 (100%)", alpha=0.7)
    plt.plot(canal2, label=f"Canal 2 ({int(scales[i]*100)}%)", alpha=0.7)
    plt.title(f"Par {i+1}: Escalado al {int(scales[i]*100)}%")
    plt.legend()
    plt.grid(True)
plt.tight_layout()
plt.show()
```
En esta imagen podemos apreciar las señales correspondientes a las diferentes amplitudes y su comparación con la original

![Señales EMG](./Imágenes%20en%20el%20anexo/Senales_EMG.png)

3. Cálculo del **Symmetry Ratio* para cada par de señales:

Para cada par de señales:
- Se limpiaron con nk.emg_clean().
- Se extrajo la envolvente con nk.emg_amplitude().
- Se calculó el área bajo la curva usando la regla de Simpson.
- Finalmente, se calculó el Symmetry Ratio:

```
symmetry_ratios = []

for factor in scales:
    # Canales
    canal1 = emg_base.copy()
    canal2 = emg_base * factor

    # Limpiar señales con NeuroKit
    clean1 = nk.emg_clean(canal1, sampling_rate=fs)
    clean2 = nk.emg_clean(canal2, sampling_rate=fs)

    # Obtener envolvente (amplitud instantánea) SIN sampling_rate
    amp1 = nk.emg_amplitude(clean1)
    amp2 = nk.emg_amplitude(clean2)

    # Calcular área bajo la curva de la envolvente (Simpson)
    area1 = integrate.simpson(amp1, dx=1/fs)
    area2 = integrate.simpson(amp2, dx=1/fs)

    # Calcular Symmetry Ratio
    symmetry_ratio = area2 / area1 if area1 != 0 else np.nan
    symmetry_ratios.append(symmetry_ratio)

for i, ratio in enumerate(symmetry_ratios):
    print(f"Par {i+1} ({int(scales[i]*100)}%): Symmetry Ratio = {ratio:.3f}")
```
4. Graficamos la diferencia de resultados
```
# Gráfico de Symmetry Ratio vs escala
plt.figure(figsize=(8, 5))
plt.bar([f"{int(s*100)}%" for s in scales], symmetry_ratios, color='skyblue')
plt.axhline(0.8, color='red', linestyle='--', label='Umbral aceptable (80%)')
plt.title("Symmetry Ratio vs Porcentaje de Escala del Canal 2")
plt.xlabel("Porcentaje de Escala del Canal 2")
plt.ylabel("Symmetry Ratio")
plt.ylim(0, 1.1)
plt.grid(True, axis='y')
plt.legend()
plt.tight_layout()
plt.show()
```
![Gráfico de comparación](./Imágenes%20en%20el%20anexo/Comparacion.png)

### Reflexión

Se observa que el *Symmetry Ratio* cae por debajo del umbral aceptable del 80 % cuando la amplitud del canal 2 se reduce por debajo del 80 %. Esto indica que asimetrías mayores al 20 % en la activación muscular entre lados ya podrían representar un desbalance clínicamente relevante, lo cual puede ser útil para evaluar disfunciones motoras o en procesos de rehabilitación.

# Ejercicio B: Índices de fatiga – pendiente de RMS vs. pendiente de frecuencia

## Objetivo de la práctica
Comparar dos métricas clásicas de fatiga: la tasa de crecimiento de la amplitud (RMS) y la tasa de caída de la frecuencia mediana.

## Metodología

**1. Primero importaremos las librerías necesarias:**
```
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt
```

**2. Ahora generaremos la señal base de 30s con 3 segmentos de 10s considerando "burst_number" decreciente y "amplitud" creciente:**

```
duration = 10  
sampling_rate = 1000

# Simulamos 3 bloques con bursts decrecientes
emg_1 = nk.emg_simulate(duration=duration, sampling_rate=sampling_rate, burst_number=10, noise=0.01)
emg_2 = nk.emg_simulate(duration=duration, sampling_rate=sampling_rate, burst_number=6, noise=0.01)
emg_3 = nk.emg_simulate(duration=duration, sampling_rate=sampling_rate, burst_number=3, noise=0.01)

# Aplicamos amplitudes crecientes para simular "fatiga"
emg_1 *= 0.5
emg_2 *= 1.0
emg_3 *= 1.5

# Concatenamos las señales
emg_signal = np.concatenate([emg_1, emg_2, emg_3]) #Al concatenarlas obtenemos la señal completa de 30 segundos

#Creamos un vector de tiempo para plotear la señal completa en función del tiempo y no solo de "samples"
time = np.linspace(0, 30, 30 * sampling_rate)

#Ploteamos la señal raw con fatiga (Amplitud vs samples)
fig = nk.signal_plot(emg_signal)

#Ploteamos la señal raw con fatiga (Amplitud vs tiempo)
plt.figure(figsize=(12, 4))
plt.plot(time, emg_signal, color='red')
plt.title("Señal EMG simulada con fatiga")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
```
![Raw EMG Amplitude vs Samples](./Imágenes%20en%20el%20anexo/raw_emg_samples.png)
![Raw EMG Amplitude vs Time](./Imágenes%20en%20el%20anexo/raw_emg_time.png)

**3. Limpiamos la señal:**
```
emg_cleaned = nk.emg_clean(emg_signal, sampling_rate=sampling_rate)

signals = pd.DataFrame({"EMG_Raw": emg_signal, "EMG_Cleaned":nk.emg_clean(emg_signal, sampling_rate=sampling_rate)})

#Ploteamos las dos señales (raw ecg y cleaned ecg) superpuestas:
fig2 = signals.plot()
```
![Raw EMG vs Cleaned EMG](./Imágenes%20en%20el%20anexo/raw_emg_vs_cleaned_emg.png)

**4. Extraemos la envolvente:**
```
amplitude = nk.emg_amplitude(emg_cleaned)

#Ploteamos las dos señales (raw ecg y la amplitud/envolvente de la clean ecg)
fig3 = pd.DataFrame({"EMG": emg_signal, "Amplitude": amplitude}).plot(subplots=True)
```
![Raw EMG and Cleaned EMG Amplitude/Envelope](./Imágenes%20en%20el%20anexo/raw_emg_and_cleaned_emg_amplitude.png)

**5. Ahora dividiremos la envolvente en ventanas de 1 s:**
```
ventanas = []
window_size = sampling_rate
num_windows = len(amplitude) // window_size

for i in range(num_windows):
  ventana = amplitude[i * window_size : (i + 1) * window_size]
  ventanas.append(ventana)

print(f"Número de ventanas de 1s: {len(ventanas)}")
```
**Resultados:**
```
Número de ventanas de 1s: 30 #Al dividir la envolvente en ventanas de 1s, la señal al tener 30s totales, nos da 30 ventanas.
```

**6. Calculamos el RMS (media de la envolvente) para cada ventana:**
```
rms_list = []

for ventana in ventanas:
    rms = np.sqrt(np.mean(ventana ** 2))
    rms_list.append(rms)

print("RMS por ventana:")
rms_list = [float(rms) for rms in rms_list]
print(rms_list)
```
**Resultados:**
```
RMS por ventana:
[0.06643054762146344, 0.06266698516280708, 0.06778442480609854, 0.06790678432032599, 0.06465474640027785, 0.06357099723797328, 0.0660004768207711, 0.06299511170204732, 0.07155472735497813, 0.06583303710848377, 0.15380846037487828, 0.14473464383367712, 0.22524894763364187, 0.16727767137669886, 0.18888219301400216, 0.1783766342433106, 0.16507413113592437, 0.20812080509919528, 0.14545762851389693, 0.15693566529179062, 0.001699459365889213, 0.3151183954707196, 0.5340333568190462, 0.0018171058717712052, 0.41047007887318837, 0.44524805963033803, 0.001850513319438513, 0.5280817797164201, 0.2986196255491269, 0.0017467285567558315]
```

**7. Ahora calculamos la frecuencia mediana vía Welch:**
```
from scipy.signal import welch

freq_median_list = []

for ventana in ventanas:
    freqs, psd = welch(ventana, fs=sampling_rate, nperseg=len(ventana))

    cumulative_power = np.cumsum(psd)
    total_power = cumulative_power[-1]
    
    freq_median = freqs[np.where(cumulative_power >= total_power / 2)[0][0]]
    freq_median_list.append(freq_median)

freq_median_list = [float(f) for f in freq_median_list]

print("Frecuencia mediana por ventana:")
print(freq_median_list)
```
**Resultados:**
```
Frecuencia mediana por ventana:
[6.0, 3.0, 3.0, 2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 4.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 3.0, 2.0, 1.0, 5.0, 1.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0, 1.0, 2.0]
```

**8. Ajustamos una recta (regresión lineal) al RMS vs. tiempo:**
```
from scipy.stats import linregress

tiempo2 = np.arange(len(rms_list))  # 0 a 29

slope_rms, intercept, r_value, p_value, std_err = linregress(tiempo2, rms_list)

rms_fit = slope_rms * tiempo2 + intercept

plt.figure(figsize=(10, 5))
plt.plot(tiempo2, rms_list, 'o', label='RMS real')
plt.plot(tiempo2, rms_fit, '-', label=f'Regresión lineal\nPendiente = {slope_rms:.4f}', color='orange')
plt.title("RMS vs. Tiempo (Indicador de fatiga)")
plt.xlabel("Tiempo (s)")
plt.ylabel("RMS")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```
![RMS vs Time](./Imágenes%20en%20el%20anexo/RMS_vs_Time.png)

**9. Ajustamos una recta (regresión lineal) al RMS vs. tiempo:**
```
tiempo = np.arange(len(freq_median_list))

slope_freq, intercept, r_value, p_value, std_err = linregress(tiempo, freq_median_list)

freq_fit = slope_freq * tiempo + intercept

plt.figure(figsize=(10, 5))
plt.plot(tiempo, freq_median_list, 'o', label='Frecuencia mediana real')
plt.plot(tiempo, freq_fit, '-', color='green', label=f'Regresión lineal\nPendiente = {slope_freq:.4f}')
plt.title("Frecuencia mediana vs. Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia mediana (Hz)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```
![Frecuencia mediana vs Time](./Imágenes%20en%20el%20anexo/Frecuencia_mediana_vs_Time.png)

