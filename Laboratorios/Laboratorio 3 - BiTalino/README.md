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
| ![bit1](./Imágenes%20en%20el%20anexo/bit1.png) | ![app](./Imágenes%20en%20el%20anexo/app.png) |
|:--:|:--:|
| Bitalino encendido | App en emparejamiento |


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


#### Deltoides

![F3](./Imágenes%20en%20el%20anexo/CONEXIONES%20EN%20EL%20HOMBRO.png)


3. Registrar señales bajo estas condiciones (1 min cada una): 
   - Reposo
   - Contracción leve (sin carga)
   - Contracción con carga (~2-3 kg)

4. Repetir 3 veces cada condición para mitigar ruido.
5. Grabar video de cada gesto mientras se visualiza la señal en OpenSignals, para luego contrastar el gesto con la actividad EMG.
6. Exportar los arhivos txt desde OpenSignals.


## Procesamiento de la señal EMG con Python
Los archivos exportados desde OpenSignals en formato .txt contienen encabezados con metadatos y una tabla de muestras, un orden y una forma de registrar los datos clásicos de BiTalino con OpenSignals. Para poder trabajar con esa data y analizarla adecuadamente, primero debemos procesarla. A continuación, se presenta el código completo utilizado para transformar estos datos en gráficas procesadas.

### 1. Importamos las librerías que utilizaremos
Estas librerías permiten manejar arrays numéricos, leer archivos, graficar resultados y aplicar filtros digitales.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from scipy.signal import butter, filtfilt, lfilter, iirnotch
```
### 2. Definimos los archivos a procesar
En este paso se define un diccionario que asocia cada músculo con su archivo .txt correspondiente, previamente cortamos los archivos para evitar tener medidas vacias de cuando se estuvo moviendo los electrodos.
```python
archivos = {
    "Bíceps": "EMG_Bicep.txt",
    "Tríceps": "EMG_Triceps.txt",
    "Hombro": "EMG_Hombro.txt"
}
```
### 3. Leemos los archivos exportados desde OpenSignals
Esta función se encarga de extraer la frecuencia de muestreo desde el encabezado JSON y cargar la señal registrada.
```python
def leer_senal_opensignals(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    for linea in lineas:
        if linea.startswith('# {'):
            json_data = json.loads(linea[2:])
            break

    device_key = list(json_data.keys())[0]
    fs = json_data[device_key]["sampling rate"]
    titulo = json_data[device_key]["label"]

    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break

    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)
    tiempo = np.arange(len(data)) / fs
    senal = data.iloc[:, -1]

    return tiempo, senal, fs, titulo
```

### 4. Convertimos los valores ADC a milivoltios
Esta función transforma los valores crudos del ADC a una escala de milivoltios, centrando la señal en 0.

```python
def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC / (2**n)) - 0.5) * VCC) / 1009
    return volts * 1000
```
### 5. Definimos y aplicamos el filtro pasa banda
Se utilizan dos funciones: una para generar el filtro y otra para aplicarlo sobre la señal. El rango seleccionado (100–300 Hz) abarca las componentes más significativas del EMG.
```python
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    return butter(order, [low, high], btype='band')

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    return lfilter(b, a, data)
```

### 6. Visualizamos la señal procesada
Esta función convierte la señal a mV, aplica los filtros, calcula la FFT, y muestra los tres resultados: señal cruda, filtrada y su espectro.

```python
def graficar_senal(tiempo, senal, fs, titulo):
    signalmV = ADCtomV(senal)
    pre_pro_signal = signalmV - np.mean(signalmV)

    low_cutoff = 100.0
    high_cutoff = 300.0
    smooth_signal = butter_bandpass_filter(pre_pro_signal, low_cutoff, high_cutoff, fs)

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

    n = len(smooth_signal)
    fft = np.fft.fft(smooth_signal)
    fft_magnitud = np.abs(fft)[:n//2]
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    fft_db = 20 * np.log10(fft_magnitud + 1e-6)

    plt.subplot(3, 1, 3)
    plt.plot(freqs, fft_db, label='FFT', color='black')
    plt.title("FFT de la Señal Filtrada")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
```

### 7. Procesamiento automático de los tres músculos
Finalmente, se recorre automáticamente cada archivo para generar sus respectivas gráficas de forma secuencial.

```python
for etiqueta, archivo in archivos.items():
    try:
        tiempo, senal, fs, titulo = leer_senal_opensignals(archivo)
        graficar_senal(tiempo, senal, fs, titulo)
```

### Registro audiovisual:

Videos de la colocación y distribución de los electrodos en el músculo de interés:
<div align="center">
 
|  **Mediciones del Bíceps**  | **Mediciones del Tríceps** | **Mediciones del Deltoides** |
|:------------:|:---------------:|:------------:|
|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/5TDMhRSWPMc)</div>|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/nDC6Fyjp32k)</div>|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/0aj-eqk9wSc)</div>|
</div>

Videos de las señales obtenidas en tiempo real de los músculos de interés:

|  **Señal - Bíceps**  | **Señal - Tríceps** | **Señal - Deltoides** |
|:------------:|:---------------:|:------------:|
|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/b1Xp7OAcqYE)</div>|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/z6KlnRIPieA)</div>|<div align="center">[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://youtube.com/shorts/fNS4MszYhyU)</div>|


---
 ## 4. Resultados y limitaciones: <a name="resultados-y-limitaciones"></a> 
Se realizaron las mediciones de forma continua, es decir, mientras el músculo estaba en reposo, en contracción leve y una contracción moderada (con carga). Por ello, se muestran las señales de los músculos evaluados, tanto la señal original, filtrada y junto a su representación en el dominio de la frecuecia (FFT):

### Bíceps:
![Bíceps](./Imágenes%20en%20el%20anexo/Señal_Biceps.png)

A partir de la señal registrada EMG para el bíceps braquial podemos interpretar para cada tramo y respecto con la bibliografía:

a. Condición de reposo (30 a 60 s aprox.): En este tramo se puede obervar que la señal tiene una amplitud muy baja, correspondiente al estado de reposo del músculo. Esto nos indica que en ausencia de la contracción o extensión activa del biceps braquial no se registra una actividad significativa [2]. En cuanto a la señal filtrada, podemos observar una señal más limpia pero sigue teniendo cierto ruido que podria provenir de ruido de interferencia, artefactos de interferencias y ruido de la piel-electrodo [3].

b. Condición de contracción leve sin carga (80 a 120 s aprox.): En este tramo se evidencia un aumento en la amplitud de la señal EMG, lo que indica la activación del bíceps durante el movimiento de contracción. Asimismo, la corta duración del movimiento y la falta de carga no genera una fatiga en el músculo [2].

c. Condición de contracción con carga (120 a 175 s aprox.): En este tramo muestra un incremento considerable en amplitud de la señal. Esto nos indica en un mayor reclutamiento de unidades motoras para vencer la carga [2]. Comparando la contracción con carga y sin carga se puede notar que mientras va transcurriendo el tiempo la amplitud de la señal va disminuyendo, lo cual podría indicar fatíga; sin embargo, la carga usada no es constante lo que podria resultar en variación de la amplitud de la señal. 

Con respecto al dominio de la frecuencia corresponiente al biceps braquial, se puede observar que la mayor magnitud entre 60 y 120 Hz. Este rango es típico de contracciones musculares activas [4]. Esta característica nos puede indicar si hubo fatiga en el movimiento con carga; por los tanto, en caso de fatiga, la mayor amplitud del espectro EMG deberia concentrarse en zonas por debajo del rango típico. Con esta información, se puede resaltar la ausencia de fatiga en las 3 mediciones realizadas.

### Tríceps:
![Tríceps](./Imágenes%20en%20el%20anexo/Señal_Triceps.png)

### Deltoides:
![Hombro](./Imágenes%20en%20el%20anexo/Señal_Hombro.png)

A partir de la señal EMG filtrada, podemos establecer las 3 condiciones de la persona durante la toma de datos. De igual manera, podemos interpretar cada tramo acorde a lo encontrado en la bibliografía:
 
a. Condición de reposo (0 a 20 s aprox.): aquí se puede ver que la señal no tiene amplitudes con variabilidad significativa sino más bien la amplitud es muy pequeña, casi cercana a cero. Este resultado es carcterístico de un músculo en estado de reposo ya que las unidades motoras no están realizando ningún tipo de contracción sino que están relajadas. La baja señal registrada puede darse debido a la presencia de artefactos o hasta de actividad mínima involuntaria de la persona [i].

b. Condición de contracción leve sin carga (20 a 40 s aprox.): se visualiza una amplitud significativa de la señal. Esta señal obtenida indica que hay unidades motoras activas para mantener una contracción leve. Además, debido a que no existe una carga aplicada al movimiento del músculo y solo se está moviendo lateralmente el brazo, tanto la amplitud de la actividad como su duración no son tan grandes por lo que tampoco se evidenciará fatiga muscular [ii]. 

c. Condición de contracción con carga (45 a 85 s aprox.): en este tramo de tiempo, se visualiza un aumento significativo en la amplitud de la señal con presencia de picos más frecuentes. Esto es el resultado de una mayor cantidad de unidades motoras activas puesto que se está realizando la respuesta a una carga externa aplicada (en este caso es una carga de entre 2 a 3 kg) [i]. En este tipo de condiciones, es en donde suele iniciarse la fatiga muscular la cual puede llegar a dañar el músculo si se mantiene dicha carga de forma repetitiva y sin realizar pausas [ii].

En cuanto al dominio de la frecuencia, se vio que hay una mayor magnitud entre los 50 a 200 Hz aproximadamente y después hay una disminución en la misma. De acuerdo a la información encontrada, esto es un resultado típico en músculos superficiales sanos como lo es, en este caso, Deltoides [ii].
 
 ## 5. Referencias: <a name="referencias"></a> 
[1] Manual del usuario del sensor de electromiografía (EMG) biosignalsplux [Internet]. Manuals+. 2021 [citado el 12 de abril de 2025]. Disponible en: https://manuals.plus/es/biosignalsplux/electromyography-emg-sensor-manual 

[2] Latfi MAK, Nordin NHD, Jasni F. Identification of active human upper limb muscle for intention detection activity. PERINTIS eJournal. 2024;14(1):67–78.

[3] Ebied A. Biceps brachii muscle fatigue assessment through EMG median frequency analysis. Int Conf Electr Eng. 2014 May. DOI: 10.21608/iceeng.2014.30468

[4] Aguirre R, Castillo S, Rojas E, Giraldo E. Acquisition and processing of EMG signals from BITalino for hand movement classification. Rev Fac Ing Univ Antioquia. 2020;(96):11–9. doi:10.17533/udea.redin.20200256

[i] Romero Mirete, C. (2023). Análisis de fatiga muscular usando HD-EMG y herramientas de procesamiento de señales. Universidad de Alicante.
[ii] González, J. A., & García, M. L. (2023). Análisis tiempo-frecuencia de parámetros de fatiga en la señal de electromiografía de superficie. Universidad Politécnica de Valencia.

[1] Johns Hopkins Medicine, “Electromyography (EMG),” [En línea]. Disponible en: https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/electromyography-emg
 
