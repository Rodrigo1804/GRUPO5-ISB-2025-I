# Laboratorio 8: Transformada Wavelet

## Contenido
1. [Introducción](#introducción)  
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y Discusión]
 4.1 [Filtrado de señal ECG](#filtrado-de-señal-ecg)  
 4.2 [Filtrado de señal EMG](#filtrado-de-señal-emg)  
 4.3 [Filtrado de señal EEG](#filtrado-de-señal-eeg)  
5. [Conclusiones](#conclusiones)  
6. [Referencias](#referencias)  

---

## 1. Introducción <a name="introducción"></a>

En la ingeniería biomédica, el análisis y procesamiento de señales como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) es fundamental para el diagnóstico y monitoreo clínico. Estas señales son inherentemente no estacionarias y suelen contener ruido y artefactos que dificultan su interpretación directa.

La transformada wavelet ha surgido como una herramienta matemática eficaz para el procesamiento de señales biomédicas, permitiendo una representación multiresolución que conserva la información temporal y frecuencial simultáneamente. A diferencia de la transformada de Fourier, que ofrece sólo información global de frecuencia, la transformada wavelet adapta su resolución en función de la escala, proporcionando alta resolución temporal para frecuencias altas y alta resolución en frecuencia para componentes de baja frecuencia. Esta característica la hace especialmente útil para detectar eventos transitorios relevantes en señales biomédicas, como complejos QRS en ECG, artefactos de movimiento en EMG y ondas anómalas en EEG.

Existen principalmente dos tipos de transformadas wavelet: continua (CWT) y discreta (DWT). La DWT es la más utilizada en sistemas digitales debido a su eficiencia computacional y capacidad para descomponer señales mediante filtros pasaaltos y pasabajos en niveles jerárquicos de detalle y aproximación. Además, la elección de la familia wavelet (por ejemplo, Haar, Daubechies, Symlets, Coiflets, Biorthogonales) influye en la calidad del filtrado y reconstrucción.

---

## 2. Propósito de la práctica <a name="propósito-de-la-práctica"></a>

Implementar y comparar técnicas de filtrado basadas en la transformada wavelet para la reducción de ruido en señales biomédicas (ECG, EMG y EEG), evaluando la eficiencia y calidad de la señal filtrada para cada tipo de señal y contexto.

---
## 3. Materiales y metodología <a name="materiales-y-metodología"></a>

**Materiales y equipos:**  
- Computadora con Python 3.12 instalado  
- Librerías Python: pywt (PyWavelets), numpy, matplotlib, scipy, neurokit2  
- Señales biomédicas adquiridas en prácticas previas (archivos .csv o formatos compatibles)  

**Metodología:**  

1. **Adquisición y carga de señales:** Se utilizaron señales ECG, EMG y EEG previamente registradas y almacenadas en archivos digitales.

2. **Visualización inicial:** Se graficaron las señales crudas para evaluar la presencia y características del ruido y artefactos.

3. **Aplicación de la transformada wavelet discreta (DWT):**  
 - Se seleccionaron familias wavelet específicas según el tipo de señal (por ejemplo, Symlet 4 y Coiflet 3 para ECG; Biorthogonal para EEG).  
 - Se definió un nivel óptimo de descomposición.  
 - Se aplicó umbralización suave (*soft thresholding*) sobre los coeficientes para atenuar el ruido, usando umbrales fijos o adaptativos según la literatura y ajustes experimentales.

4. **Reconstrucción de señal:** Se reconstruyó la señal filtrada usando los coeficientes umbralizados.

5. **Comparación y análisis:** Se compararon señales originales y filtradas visualmente y con métricas cuantitativas (si se disponen), para evaluar la efectividad del filtrado.
---

## 4. Resultados y Discusión

### 4.1 Filtrado de señal ECG <a name="filtrado-de-señal-ecg"></a>

Las señales ECG mostraron ruido característico debido a interferencias electromagnéticas y artefactos de movimiento. Se aplicaron filtros DWT con wavelets Symlet 4 y Coiflet 3 en niveles 3 a 7. Ambas configuraciones lograron reducir significativamente el ruido, conservando la morfología característica de los complejos QRS. Sin embargo, Coiflet 3 mostró un filtrado más suave en condiciones de ruido moderado a alto, lo que concuerda con hallazgos previos en la literatura.

### 4.2 Filtrado de señal EMG <a name="filtrado-de-señal-emg"></a>

En señales EMG, el filtrado wavelet fue efectivo para eliminar artefactos de movimiento y ruido muscular. Se observó que la elección adecuada de la familia wavelet y el nivel de descomposición son cruciales para preservar la información fisiológica relevante, como la actividad muscular en contracciones leves y fuertes.

### 4.3 Filtrado de señal EEG <a name="filtrado-de-señal-eeg"></a>

Para las señales EEG se utilizó un filtro DWT basado en wavelet Biorthogonal 2.6 a nivel 5, que mostró alta capacidad para separar componentes de baja y alta frecuencia, reduciendo el ruido sin pérdida significativa de información cerebral. Esta configuración es recomendada para estudios neurológicos que requieren alta fidelidad en la señal.

---

## 5. Conclusiones <a name="conclusiones"></a>

ESTO ES FLORO DE CHAT!!!!
La transformada wavelet discreta es una herramienta poderosa y versátil para el procesamiento y filtrado de señales biomédicas, permitiendo la reducción de ruido y preservación de características morfológicas clave en ECG, EMG y EEG. La elección de la familia wavelet, el nivel de descomposición y la estrategia de umbralización son determinantes para el éxito del filtrado.

En particular, los filtros basados en Coiflet y Biorthogonal demostraron superioridad en condiciones de ruido variable, adaptándose bien a las necesidades específicas de cada tipo de señal biomédica. Por lo tanto, la transformada wavelet es recomendada para aplicaciones clínicas y de investigación que demandan análisis robustos y confiables de señales biomédicas no estacionarias.

---

## 6. Referencias <a name="referencias"></a>

[1] xd
[2] Tx
[3] P. Z
