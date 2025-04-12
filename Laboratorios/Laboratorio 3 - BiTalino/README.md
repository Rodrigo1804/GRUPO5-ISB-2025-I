# Laboratorio 3: Uso de Bitalino para EMG y ECG:

## Contenido:
1. [Introducción](#introducción)  
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y limitaciones](#resultados-y-limitaciones)  
5. [Referencias](#referencias)
 ## 1. Introducción:
La electromiografía (EMG) es una técnica diagnóstica utilizada para evaluar la salud de los músculos y los nervios que los controlan. Esta prueba detecta la actividad eléctrica producida por las fibras musculares en respuesta a la estimulación nerviosa, lo cual permite identificar disfunciones musculares, trastornos neuromusculares o problemas de comunicación entre nervios y músculos. En contextos educativos y de investigación, la EMG también es clave para el análisis del esfuerzo físico, el diseño de interfaces mioeléctricas y la rehabilitación neuromuscular [1].
Para registrar estas señales de manera práctica y accesible, se utilizan plataformas como BITalino, un sistema portátil de adquisición de biopotenciales que incluye sensores de EMG y permite el análisis en tiempo real a través de herramientas como OpenSignals.
 ## 2. Propósito de la práctica:
El propósito de esta práctica es adquirir señales de EMG utilizando el kit BITalino, evaluando su comportamiento bajo tres condiciones fisiológicas: reposo, contracción leve y contracción con carga. Además, se busca comprender el uso del software OpenSignals para la visualización de biopotenciales y realizar un análisis básico de las señales obtenidas.

 ## 3. Materiales y metodología:
 ### Materiales:
 | Cantidad | Descripción                         |
|----------|-------------------------------------|
| 1        | KIT BITalino (r)evolution           |
| 1        | Laptop con Bluetooth                |
| 1        | Software OpenSignals (r)evolution   |
| 5        | Electrodos de superficie            |
| 1        | Cable de 3 conductores (para EMG)   |
| 1        | Batería LiPo 3.7V                   |

### Procedimiento:

1. Encender la placa BITalino y emparejarla vía Bluetooth (PIN: 1234).
2. Colocar electrodos sobre los músculos (bíceps, tríceps, deltoides).

#### Triceps

![F1](./Imágenes%20en%20el%20anexo/F1.png)

 EXPLICAR CONEXIONES, ELECTRODO DE REFERENCIA Y ESO}
 
4. Registrar señales bajo estas condiciones (1 min cada una):
   - Reposo
   - Contracción leve (sin carga)
   - Contracción con carga (~2-3 kg)

5. Repetir 3 veces cada condición para mitigar ruido.
6. Guardar los datos y grabar video con señal + gesto.

```python
import numpy as np
import matplotlib.pyplot as plt

# Cargar señal desde archivo
emg = np.loadtxt('../datos/biceps_raw.txt')

# Frecuencia de muestreo (Hz)
fs = 1000  
t = np.arange(0, len(emg)) / fs

# Graficar señal EMG cruda
plt.figure(figsize=(10, 4))
plt.plot(t, emg, label='EMG cruda')
plt.title('Señal EMG cruda – Bíceps')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('../figuras/biceps_raw_plot.png')
plt.show()
```

### Registro audiovisual:

Aca poner videos

---
 ## 4. Resultados y limitaciones:
 interpretar basado en evidencia

### Bíceps:
![Bíceps](./Imágenes%20en%20el%20anexo/Biceps.png)

### Tríceps:
![Tríceps](./Imágenes%20en%20el%20anexo/Triceps.png)

### Hombro:
![Hombro](./Imágenes%20en%20el%20anexo/Hombro.png)

 
 ## 5. Referencias:
[1] Johns Hopkins Medicine, “Electromyography (EMG),” [En línea]. Disponible en: https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/electromyography-emg
 
