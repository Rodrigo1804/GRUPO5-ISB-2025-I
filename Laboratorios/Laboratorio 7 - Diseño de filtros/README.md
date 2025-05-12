# Laboratorio 7: diseño de filtros

## Contenido:
1. [Introducción](#introducción)
2. [Propósito de la práctica](#propósito-de-la-práctica)
3. [Filtrado de señal ECG](#filtrado-de-señal-ecg) 
4. [Filtrado de señal EMG](#filtrado-de-señal-emg)
5. [Filtrado de señal EEG](#filtrado-de-señal-eeg) 
6. [Referencias](#referencias)


## 1. Introducción <a name="introducción"></a>
En este laboratorio, se tiene como objetivo el diseño y la aplicación de filtros digitales para señales biomédicas, específicamente para señales de ECG (Electrocardiograma), EMG (Electromiograma) y EEG (Electroencefalograma). Las señales biomédicas suelen estar contaminadas con diferentes tipos de ruido de diversas frecuencias, por lo que es fundamental el uso de filtros para mejorar la calidad de las señales y facilitar su análisis.

**¿Qué es un filtro?**
Un filtro es un sistema que procesa señales para mejorar su calidad o extraer información especifica, existen 2 tipos de filtros: Analógicos y Digitales

**Filtros Analógicos**
Los filtros analógicos son dispositivos electrónicos diseñados para modificar señales continuas. Estos filtros utilizan componentes pasivos como resistencias, inductores y capacitores, o componentes activos como amplificadores operacionales. Si bien los filtros analógicos son eficientes y fáciles de implementar, en sistemas más complejos con señales digitales, su diseño y ajuste pueden volverse complicados[1].

**Filtros Digitales**
Los filtros digitales son algoritmos que operan sobre señales discretas, representadas por secuencias de números en tiempos específicos. Los filtros digitales se dividen principalmente en dos categorías: Filtros IIR (Infinite Impulse Response) y FIR (Finite Impulse Response).

	•	Filtros IIR: Son filtros recursivos que utilizan tanto las entradas actuales como las pasadas, así como las salidas pasadas. Estos filtros son efectivos y requieren menos coeficientes en comparación con los FIR, pero pueden introducir no linealidades en la fase [2].
	•	Filtros FIR: Son filtros no recursivos que solo dependen de las entradas pasadas, lo que los hace más estables, pero suelen requerir más coeficientes para lograr un rendimiento similar al de los filtros IIR [3].

## 2. Propósito de la práctica <a name="propósito-de-la-práctica"></a>
Aplicar conocimientos teóricos para el diseño e implementación de filtros digitales FIR e IIR que puedan ser implementados para el procesamiento de señales biomédicas como ECG, EEG y EMG. Además, se busca comparar los efectos de los distintos tipos de filtros y evaluar el impacto de los mismos en la calidad de las señales. Estos filtros se diseñarán haciendo uso de herramientas como Google Collab.

## 3. Filtrado de señal ECG <a name="filtrado-de-señal-ecg"></a>
Para el diseño de los **filtros FIR** se utilizaron ventanas de Hamming y Bartlett. La ventana de Hamming brinda buen equilibrio entre el atenuando en la banda de detención y el ripple de la de paso. Por otro lado, la ventana de Bartlett tiene una menor atenuación fuera de banda [2]. 

En el diseño de los **filtros IIR** se utilizaron Butterworth y Chebyshev Tipo I por la eficiencia en función del orden del filtro requerido para una respuesta adecuada. Butterworth tiene una respuesta de magnitud decreciente, sin rizado en la banda de detención y de paso lo que lo hace ideal para preservar la forma de la señal. Por otro lado, Chebyshev tipo I introduce un rizado en la banda de paso, pero a pesar de ello permite una transición más abrupta con orden menor haciéndolo una opción útil [3].

### Primera Derivada
| Campo                 | RAW                | Filtros FIR        | Filtros IIR          |
|-----------------------|--------------------|--------------------|----------------------|
|Reposo                 | ![Raw 1](./Imágenes%20en%20el%20anexo/Reposo1raDerivRaw.jpg)| ![FIR](./Imágenes%20en%20el%20anexo/Reposo1raDerivFiltradaFIR.jpg) | ![IIR](./Imágenes%20en%20el%20anexo/Reposo1raDerivFiltradaIIR.jpg) |
|Actividad Física       |![Raw 2](./Imágenes%20en%20el%20anexo/ActividadFisicaRaw1raDeriv.jpg)|![FIR](./Imágenes%20en%20el%20anexo/ActividadFisica1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/ActividadFisica1raDerivFiltradaIIR.jpg)|
|Post Actividad Física  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad1raDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaIIR.jpg)|

  
### Segunda Derivada

| Campo                 | RAW                | Filtros FIR        | Filtros IIR          |
|-----------------------|--------------------|--------------------|----------------------|
|Reposo                 | ![Raw 1](./Imágenes%20en%20el%20anexo/Reposo2daDerivRaw.jpg)| ![FIR](./Imágenes%20en%20el%20anexo/Reposo2daDerivFiltradaFIR.jpg) | ![IIR](./Imágenes%20en%20el%20anexo/Reposo2daDerivFiltradaIIR.jpg) |
|Actividad Física       |![Raw 2](./Imágenes%20en%20el%20anexo/ActividadFisicaRaw2daDeriv.jpg)|![FIR](./Imágenes%20en%20el%20anexo/ActividadFisica2daDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/ActividadFisica2daDerivFiltradaIIR.jpg)|
|Post Actividad Física  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad2daDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad2daDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad2daDerivFiltradaIIR.jpg)|


### Tercera Derivada

| Campo                 | RAW                | Filtros FIR        | Filtros IIR          |
|-----------------------|--------------------|--------------------|----------------------|
|Reposo                 | ![Raw 1](./Imágenes%20en%20el%20anexo/Reposo3raDerivRaw.jpg)| ![FIR](./Imágenes%20en%20el%20anexo/Reposo3raDerivFiltradaFIR.jpg) | ![IIR](./Imágenes%20en%20el%20anexo/Reposo3raDerivFiltradaIIR.jpg) |
|Actividad Física       |![Raw 2](./Imágenes%20en%20el%20anexo/ActividadFisicaRaw3raDeriv.jpg)|![FIR](./Imágenes%20en%20el%20anexo/ActividadFisica3raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/ActividadFisica3raDerivFiltradaIIR.jpg)|
|Post Actividad Física  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad3raDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad3raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad3raDerivFiltradaIIR.jpg)|

Evaluamos a partir de los resultados obtenidos cuál de los filtros para cada caso (FIR e IIR) nos dio una señal más limpia como resultado, es decir, la que mejor preserva la forma de la señal y suaviza el ruido de alta frecuencia sin afectar componentes importantes.

* Conclusión Filtros FIR: el filtro con ventana de Hamming nos dio una mejor calidad de filtrado. Para las señales obtenidas vemos que la ventana de Hamming nos da señales más suaves y preserva de mejor manera la forma de QRS sin ruidos en las regiones interlatido. Por otro lado, Bartlett muestra oscilaciones, aunque son muy pequeñas, pero ello puede interpretarse como la retención de ruido residual. 

* Conclusión Filtros IIR: aquí a diferencia de los filtros FIR, hay diferencias más notorias. Vemos que el filtro Butterworth ofrece una mejor calidad de filtrado en las señales ya que preserva de mejor manera el complejo QRS y tiene una linea base más estable. Por otro lado, Chebyshev nos da más variaciones de amplitud y un rizado que es notorio a simple vista.
  
## 4. Filtrado de señal EMG <a name="filtrado-de-señal-emg"></a>

## Diseño de filtro IIR:
En el diseño de los filtros IIR se consideró el uso de dos tipos de filtros pasa banda: Butterworth y Chebyshev, ambos adecuados para filtrar las señales EMG dentro de un rango de frecuencias de interés (40-150 Hz) [4]. Se utilizó una frecuencia de muestreo de 1000 Hz y ambos filtros estan diseñados con un orden de 10.

![IIR](./Imágenes%20en%20el%20anexo/IIR.png)

### Triceps

![TricepsR](./Imágenes%20en%20el%20anexo/TricepsR.png)

### Biceps

![BicepsR](./Imágenes%20en%20el%20anexo/BicepsR.png)

### Hombro 

![HombroR](./Imágenes%20en%20el%20anexo/HombroR.png)

### Tabla resumen para filtros IIR

| Tipo de señal       | Descanso           | Contracción leve   | Contracción fuerte  |
|-----------------------|--------------------|--------------------|---------------------|
| **Señal Cruda (Tríceps)** | (0 a 40 s aprox)  | (40 a 60 s aprox) |  (70 a 120 s aprox) |
| **Filtro Butterworth** |Se observa una amplitud considerable y ruido bajo, con atenuación de frecuencias fuera de este rango.| El ruido se reduce pero la señal sigue mostrando actividad importante. | Se preserva la actividad muscular relevante mientras que se elimina la mayor parte del ruido de movimiento. |
| **Filtro Chebyshev**  | A pesar de que la transición sea más rápida que el de Butterworth y una posible distorsión de la señal por la presencia de ripples, no se puede observar una diferencia significativa. |  Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observar una diferencia significativa. |  La contracción fuerte se conserva muy bien. Se puede notar ligeramente cierta diferencia en la forma de la señal en algunas zonas y se puede deber a la presencia de ripples en la banda de paso. |
| **Señal Cruda (Biceps)** | (0 a 75 s aprox) | (75 a 115 s aprox.) | (115 a 175 s aprox.)  |
| **Filtro Butterworth** | La señal presenta una amplitud menor comparada con la cruda, con una transición más suave en las frecuencias. | La contracción leve muestra un buen filtrado, eliminando las frecuencias fuera del rango establecido y se puede notar la presencia de la respuesta muscular. |  Se puede observar que el filtro permite una buena preservación de la contracción fuerte, aunque las frecuencias fuera de rango se atenúan progresivamente. |
| **Filtro Chebyshev**  | Se redujo el ruido pero no se puede apreciar una diferencia notable con el Butterworth | Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observa una diferencia significativa con el Butterworth. | Se conserva la amplitud de la contracción fuerte , aunque los ripples en la banda de paso están afectando algunos picos altos en la señal. |
| **Señal Cruda (Hombro)** | (0 a 20 s aprox) | (20 a 50 s aprox)  |  (50 a 85 s aprox) |
| **Filtro Butterworth** | El ruido de redujo considerablemente.  |  El ruido se reduce pero la señal sigue mostrando actividad importante. | Se conserva bien la actividad muscular de la contracción fuerte, aunque se debe considerar la lenta atenuación para 150 Hz. |
| **Filtro Chebyshev**  | El ruido de redujo considerablemente pero no se puede apreciar una diferencia notable con el Butterworth| Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observa una diferencia significativa con el Butterworth. | Se conserva la amplitud de la contracción fuerte pero se puede notar cierta diferencia en la forma de la señal y puede deberser a los ripples o a la lenta atenuación del butterworth para la frecuencia de 150 Hz. |



### Diseño de filtro FIR:
En el diseño de los filtros FIR pasa banda, sse consideró el uso de dos tipos de ventanas: Hamming y Blackman, ambos utilizados para filtrar las señales EMG en el rango de 40-150 Hz. Se utilizó una frecuencia de muestreo de 1000 Hz y ambos filtros estan diseñados con un orden de 101 coeficientes.

![FIR](./Imágenes%20en%20el%20anexo/FIR.png)

### Triceps

![TricepsF](./Imágenes%20en%20el%20anexo/TricepsF.png)

### Biceps

###### ![BicepsF](./Imágenes%20en%20el%20anexo/BicepsF.png)

### Hombro 

![HombroF](./Imágenes%20en%20el%20anexo/HombroF.png)

### Tabla resumen para filtros FIR

| Tipo de señal         | Descanso           | Contracción leve   | Contracción fuerte  |
|-----------------------|--------------------|--------------------|---------------------|
| **Señal Cruda (Tríceps)** | (0 a 40 s aprox)  | (40 a 60 s aprox) | (70 a 120 s aprox) |
| **Filtro Hamming** | La señal es más suave, con menos picos de ruido en comparación con la señal cruda. | En la contracción leve, la señal muestra una actividad muscular, sin demasiadas distorsiones. | La señal filtrada mantiene la respuesta de contracción fuerte sin pérdidas importantes de la actividad muscular.|
| **Filtro Blackman** | Similar al filtro Hamming. | La contracción leve muestra un filtrado eficaz Y sigue siendo representativa de la actividad muscular. | Se preserva muy bien la actividad muscular de la contracción fuerte. Sin embargo, no se puede observar una diferencia significativa. |
| **Señal Cruda (Bíceps)** | (0 a 75 s aprox) | (75 a 115 s aprox.) | (115 a 175 s aprox.)  |
| **Filtro Hamming** | La señal se suaviza y se reduce el ruido | El filtro preserva bien la respuesta muscular, especialmente en contracciones de baja intensidad. | En la contracción fuerte, la actividad muscular se conserva y el filtro Hamming elimina las frecuencias altas.|
| **Filtro Blackman** | Similar al filtro Hamming. | La respuesta muscular en la contracción leve sigue presente. Los artefactos son eliminados de manera efectiva, pero el filtro Blackman puede hacer que algunos picos pequeños sean menos evidentes. | La contracción fuerte es bien representada y el filtro hace un buen trabajo atenuando el ruido de alta frecuencia pero no se puede apreciar una diferencia significativa con el filtro Hamming. |
| **Señal Cruda (Hombro)** | (0 a 20 s aprox) | (20 a 50 s aprox)  | (50 a 85 s aprox) |
| **Filtro Hamming** | Se reduce considerablemente la amplitud de los picos y el ruido | La contracción leve muestra la actividad muscular con buena resolución. | Se preserva bien la contracción fuerte, eliminando frecuencias no deseadas. |
| **Filtro Blackman** | Similar al filtro Hamming.|  La actividad muscular sigue siendo clara. | En la contracción fuerte se puede notar la actividad muscular pero no se puede apreciar una diferencia con el filtro hamming. |


## 5. Filtrado de señal EEG <a name="filtrado-de-señal-eeg"></a>

### Primera Derivada
| Campo                 | RAW                |	Filtro FIR - Hamming     |   Filtro FIR - Bartlett   |  Filtro IIR - Butterworth  |   Filtro IIR - Chebyshev    |
|-----------------------|--------------------|---------------------------|---------------------------|----------------------------| ----------------------------|
|Basal 1                | ![Basal 1 RAW](./Imágenes%20en%20el%20anexo/BASAL_1_RAW_SIGNAL.png)| ![Basal_1_FIR_Hamming](./Imágenes%20en%20el%20anexo/BASAL_1_RAW_SIGNAL.png) | ![Basal_1_FIR_Bartlett](./Imágenes%20en%20el%20anexo/BASAL_1_RAW_SIGNAL.png) | ![Basal_1_IIR_Butterworth](./Imágenes%20en%20el%20anexo/BASAL_1_RAW_SIGNAL.png) | ![Basal_1_IIR_Chebyshev](./Imágenes%20en%20el%20anexo/BASAL_1_RAW_SIGNAL.png)|
|Basal 2       |![Raw 2](./Imágenes%20en%20el%20anexo/ActividadFisicaRaw1raDeriv.jpg)|![FIR](./Imágenes%20en%20el%20anexo/ActividadFisica1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/ActividadFisica1raDerivFiltradaIIR.jpg)|
|Tarea Cognitiva  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad1raDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaIIR.jpg)|
|Artefactos  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad1raDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaIIR.jpg)|
|Actividad Libre  |![Raw 3](./Imágenes%20en%20el%20anexo/PostActividad1raDerivRaw.jpg)|![FIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaFIR.jpg)|![IIR](./Imágenes%20en%20el%20anexo/PostActividad1raDerivFiltradaIIR.jpg)|

## 6. Referencias <a name="referencias"></a>
[1]
[2] Y. Zigel, D. Litvak, and A. Cohen, "A new method for detection of peaks in ECG signals," IEEE Eng. Med. Biol. Mag., vol. 21, no. 1, pp. 119–123, Jan.-Feb. 2002, doi: 10.1109/51.993193.
[3] S. Patidar and R. Pachori, "An efficient method for detection of QRS complexes in electrocardiogram signal based on adaptive windowing," IEEE Sensors J., vol. 16, no. 20, pp. 7553–7561, 2016, doi: 10.1109/JSEN.2016.2599834.
[4] Zhao, Y., Jia, L., Liu, Z., & Lu, H. (2022). A Wearable, Multi-Frequency Device to Measure Muscle Activity Combining Simultaneous Electromyography and Electrical Impedance Myography. Sensors, 22(5), 1941. https://doi.org/10.3390/s22051941 

