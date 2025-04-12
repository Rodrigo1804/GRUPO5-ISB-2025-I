# Laboratorio 3: Uso de Bitalino para EMG y ECG:

## Contenido:
1. [Introducción](#introducción)
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y limitaciones](#resultados-y-limitaciones)  
5. [Referencias](#referencias)
 ## 1. Introducción: <a name="introducción"></a>
La electromiografía (EMG) es una técnica diagnóstica utilizada para evaluar la salud de los músculos y los nervios que los controlan. Esta prueba detecta la actividad eléctrica producida por las fibras musculares en respuesta a la estimulación nerviosa, lo cual permite identificar disfunciones musculares, trastornos neuromusculares o problemas de comunicación entre nervios y músculos. En contextos educativos y de investigación, la EMG también es clave para el análisis del esfuerzo físico, el diseño de interfaces mioeléctricas y la rehabilitación neuromuscular [1].
Para registrar estas señales de manera práctica y accesible, se utilizan plataformas como BITalino, un sistema portátil de adquisición de biopotenciales que incluye sensores de EMG y permite el análisis en tiempo real a través de herramientas como OpenSignals.
 ## 2. Propósito de la práctica: <a name="propósito-de-la-práctica"></a>
El propósito de esta práctica es adquirir señales de EMG utilizando el kit BITalino, evaluando su comportamiento bajo tres condiciones fisiológicas: reposo, contracción leve y contracción con carga. Además, se busca comprender el uso del software OpenSignals para la visualización de biopotenciales y realizar un análisis básico de las señales obtenidas.

 ## 3. Materiales y metodología: <a name="materiales-y-metodología"></a>
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
#### Tipos de electrodos usados: [1]
Colocamos los electrodos siguiendo el protocolo de electromiografía de superficie (sEMG) para captar la actividad muscular con presición, siguiendo los siguientes conceptos:

**- Rojo → Electrodo activo (+):** Se coloca sobre el vientre del músculo que se desea medir, justo donde se quiere recibir la actividad eléctrica. Es el que detecta los cambios de voltaje cuando el músculo se activa. 

**- Blanco → Electrodo de referencia (-):** Este también se coloca sobre el músculo, pero un poco más alejado del rojo, a lo largo de las fibras musculares. Trabaja en conjunto con el rojo para captar la diferencia de potencial eléctrico entre ambos puntos.

**- Negro → Electrodo de tierra (GND):** Este no mide señal, pero es fundamental para estabilizar el sistema y eliminar interferencias eléctricas. Se coloca sobre una zona eléctricamente neutra (por ejemplo, una parte ósea o alejada del músculo principal). 

#### Bíceps
![F1](./Imágenes%20en%20el%20anexo/CONEXIONES%20EN%20EL%20BÍCEPS.png)


#### Triceps

![F2](./Imágenes%20en%20el%20anexo/CONEXIONES%20EN%20EL%20TRÍCEPS.png)


#### Triceps

![F3](./Imágenes%20en%20el%20anexo/CONEXIONES%20EN%20EL%20HOMBRO.png)


3. Registrar señales bajo estas condiciones (1 min cada una): 
   - Reposo
   - Contracción leve (sin carga)
   - Contracción con carga (~2-3 kg)

4. Repetir 3 veces cada condición para mitigar ruido.
5. Guardar los datos y grabar video con señal + gesto.

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

<div align="center">

|  **Dedo en reposo**  | **Dedo sin oposición** | **Dedo con oposición** |
|:------------:|:---------------:|:------------:|
|<video src="https://files.catbox.moe/rlumto.mp4" controls></video>|<video src="https://user-images.githubusercontent.com/62686249/231337782-f487bdb1-d614-4010-8caa-26c267cba7f6.mp4"></video>|<video src= "https://user-images.githubusercontent.com/62686249/231337918-3db1b3f2-4e32-4e3c-bb6f-f8fb607a03d2.mp4"></video>|
</div>

---
 ## 4. Resultados y limitaciones: <a name="resultados-y-limitaciones"></a> 
Se realizaron las mediciones de forma continua, es decir, mientras el músculo estaba en reposo, en contracción leve y una contracción moderada (con carga). Por ello, se muestran las señales de los músculos evaluados, tanto la señal original, filtrada y junto a su representación en el dominio de la frecuecia (FFT):

### Bíceps:
![Bíceps](./Imágenes%20en%20el%20anexo/Señal_Biceps.png)

### Tríceps:
![Tríceps](./Imágenes%20en%20el%20anexo/Señal_Triceps.png)

### Hombro:
![Hombro](./Imágenes%20en%20el%20anexo/Señal_Hombro.png)

 
 ## 5. Referencias: <a name="referencias"></a> 
[1] Manual del usuario del sensor de electromiografía (EMG) biosignalsplux [Internet]. Manuals+. 2021 [citado el 12 de abril de 2025]. Disponible en: https://manuals.plus/es/biosignalsplux/electromyography-emg-sensor-manual 

[2]

[1] Johns Hopkins Medicine, “Electromyography (EMG),” [En línea]. Disponible en: https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/electromyography-emg
 
