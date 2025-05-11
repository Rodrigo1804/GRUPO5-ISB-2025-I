# Laboratorio 7: diseño de filtros

## Contenido:
1. [Introducción](#introducción)
2. [Propósito de la práctica](#propósito-de-la-práctica)
3. [Filtrado de señal ECG](#filtrado-de-señal-ecg) 
4. [Filtrado de señal EMG](#filtrado-de-señal-emg)
5. [Filtrado de señal EEG](#filtrado-de-señal-eeg) 
6. [Resultados y limitaciones](#resultados-y-limitaciones)  
7. [Referencias](#referencias)


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
![IIR](./Imágenes%20en%20el%20anexo/IIR.png)

### Triceps

![TricepsR](./Imágenes%20en%20el%20anexo/TricepsR.png)

### Biceps

![BicepsR](./Imágenes%20en%20el%20anexo/BicepsR.png)

### Hombro 

![HombroR](./Imágenes%20en%20el%20anexo/HombroR.png)

### Tabla resumen para filtros IIR

# Tabla para filtros IIR (Butterworth y Chebyshev)

| Tipo de señal       | Descanso           | Contracción leve   | Contracción fuerte  |
|-----------------------|--------------------|--------------------|---------------------|
| **Señal Cruda (Tríceps)** |   |  |   |
| **Filtro Butterworth (IIR)** | |  |  |
| **Filtro Chebyshev (IIR)**  |  |   |   |
| **Señal Cruda (Biceps)** |  |  |   |
| **Filtro Butterworth (IIR)** |  | |  |
| **Filtro Chebyshev (IIR)**  |  |  |  |
| **Señal Cruda (Hombro)** |  |   |  |
| **Filtro Butterworth (IIR)** |  |  |  |
| **Filtro Chebyshev (IIR)**  |  |   |  |



### Diseño de filtro FIR:
![FIR](./Imágenes%20en%20el%20anexo/FIR.png)

### Triceps

![TricepsF](./Imágenes%20en%20el%20anexo/TricepsF.png)

### Biceps

###### ![BicepsF](./Imágenes%20en%20el%20anexo/BicepsF.png)

### Hombro 

![HombroF](./Imágenes%20en%20el%20anexo/HombroF.png)

# Tabla resumen para filtros FIR



## 5. Introducción <a name="introducción"></a>
## 6. Introducción <a name="introducción"></a>
## 7. Introducción <a name="introducción"></a>
