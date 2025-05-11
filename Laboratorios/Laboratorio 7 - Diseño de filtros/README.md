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
## 3. Filtrado de señal ECG <a name="filtrado-de-señal-ecg"></a>
## 4. Filtrado de señal EMG <a name="filtrado-de-señal-emg"></a>

## Diseño de filtro IIR:
En el diseño de los filtros IIR se consideró el uso de dos tipos de filtros pasa banda: Butterworth y Chebyshev, ambos adecuados para filtrar las señales EMG dentro de un rango de frecuencias de interés (40-150 Hz). Se utilizó una frecuencia de muestreo de 1000 Hz y ambos filtros estan diseñados con un orden de 10.

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
| **Filtro Butterworth** |Se observa una amplitud considerable y ruido bajo, con atenuación de frecuencias fuera de este rango. La señal filtrada mantiene una transición suave en el rango de frecuencia establecido. | El ruido se reduce pero la señal sigue mostrando actividad importante. | Se preserva la actividad muscular relevante mientras que se elimina la mayor parte del ruido de movimiento. |
| **Filtro Chebyshev**  | A pesar de que la transición sea más rápida que el de Butterworth y una posible distorsión de la señal por la presencia de ripples, no se puede observar una diferencia significativa. |  Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observa una diferencia significativa |  La contracción fuerte se conserva muy bien. Se puede notar ligeramente cierta diferencia en la forma de la señal en algunas zonas y se puede deber a la presencia de ripples en la banda de paso. |
| **Señal Cruda (Biceps)** | (0 a 75 s aprox) | (75 a 115 s aprox.) | (115 a 175 s aprox.)  |
| **Filtro Butterworth** | La señal presenta una amplitud menor comparada con la cruda, con una transición más suave en las frecuencias. | La contracción leve muestra un buen filtrado, eliminando las frecuencias fuera del rango establecido y se puede notar la presencia de la respuesta muscular |  Se puede observar que el filtro permite una buena preservación de la contracción fuerte, aunque las frecuencias fuera de rango se atenúan progresivamente. |
| **Filtro Chebyshev**  | Se redujo el ruido pero no se puede apreciar una diferencia notable con el Butterworth | Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observa una diferencia significativa con el Butterworth | Se conserva la amplitud de la contracción fuerte , aunque los ripples en la banda de paso están afectando algunos picos altos en la señal. |
| **Señal Cruda (Hombro)** | (0 a 20 s aprox) | (20 a 50 s aprox)  |  (50 a 85 s aprox) |
| **Filtro Butterworth** | El ruido de redujo considerablemente  |  El ruido se reduce pero la señal sigue mostrando actividad importante. | Se conserva bien la actividad muscular de la contracción fuerte, aunque se debe considerar la lenta atenuación para 150 Hz. |
| **Filtro Chebyshev**  | El ruido de redujo considerablemente pero no se puede apreciar una diferencia notable con el Butterworth| Se mantiene la respuesta muscular, lo que indica una contracción leve. Sin embargo, no se observa una diferencia significativa con el Butterworth | Se conserva la amplitud de la contracción fuerte pero se puede notar cierta diferencia en la forma de la señal y puede deberser a los ripples o a la lenta atenuación del butterworth para la frecuencia de 150 Hz. |



### Diseño de filtro FIR:
En el diseño de los filtros FIR pasa banda, sse consideró el uso de dos tipos de ventanas: Hamming y Blackman, ambos utilizados para filtrar las señales EMG en el rango de 40-150 Hz. Se utilizó una frecuencia de muestreo de 1000 Hz y ambos filtros estan diseñados con un orden de 101 coeficientes.

![FIR](./Imágenes%20en%20el%20anexo/FIR.png)

### Triceps

![TricepsF](./Imágenes%20en%20el%20anexo/TricepsF.png)

### Biceps

###### ![BicepsF](./Imágenes%20en%20el%20anexo/BicepsF.png)

### Hombro 

![HombroF](./Imágenes%20en%20el%20anexo/HombroF.png)

# Tabla resumen para filtros FIR

| Tipo de Filtro        | Descanso           | Contracción leve   | Contracción fuerte  |
|-----------------------|--------------------|--------------------|---------------------|
| **Señal Cruda (Tríceps)** |  |  |   |
| **Filtro Hamming**  |   |   |   |
| **Filtro Blackman** |  |  |  
| **Señal Cruda (Bíceps)** |  |  |   |
| **Filtro Hamming**  |   |   |   |
| **Filtro Blackman** |  |  |  |
| **Señal Cruda (Hombro)** |  |  |   |
| **Filtro Hamming**  |   |   |   |
| **Filtro Blackman** |  |  |  |


## 5. Introducción <a name="introducción"></a>
## 6. Introducción <a name="introducción"></a>

