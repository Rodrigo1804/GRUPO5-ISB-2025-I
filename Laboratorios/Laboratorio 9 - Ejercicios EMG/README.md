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
