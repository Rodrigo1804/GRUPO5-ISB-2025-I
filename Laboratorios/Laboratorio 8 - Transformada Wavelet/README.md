# Laboratorio 8: Transformada Wavelet

## Contenido
1. [Introducción](#introducción)  
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y Discusión](#resultados-y-discusion)  
 4.1 [Filtrado de señal ECG](#filtrado-de-señal-ecg)  
 4.2 [Filtrado de señal EMG](#filtrado-de-señal-emg)  
 4.3 [Filtrado de señal EEG](#filtrado-de-señal-eeg)  
6. [Conclusiones](#conclusiones)  
7. [Referencias](#referencias)  

---

## 1. Introducción <a name="introducción"></a>

Las señales biomédicas como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) son esenciales para diagnóstico e investigación clínica, pero presentan desafíos importantes debido a su naturaleza no estacionaria y la presencia frecuente de ruido y artefactos [2][3]. Por ello, técnicas avanzadas de procesamiento son necesarias para extraer información útil y confiable.

La transformada wavelet se ha convertido en una herramienta clave para el análisis de estas señales, gracias a su capacidad de proporcionar una representación multiresolución que conserva información tanto temporal como frecuencial [2][4]. A diferencia de la transformada de Fourier, que ofrece una descomposición global en frecuencia sin retener la localización temporal, la transformada wavelet adapta su resolución dependiendo de la escala, ofreciendo alta resolución temporal para componentes de alta frecuencia y alta resolución frecuencial para componentes de baja frecuencia [4][5]. Esto la hace especialmente efectiva para detectar eventos transitorios como los complejos QRS en ECG, activaciones musculares en EMG o patrones corticales en EEG.

### Fundamentos matemáticos

Formalmente, la transformada wavelet continua (CWT) de una señal \( f(t) \in L^2(\mathbb{R}) \) está dada por la integral

$$
W_f(a,b) = \frac{1}{\sqrt{|a|}} \int_{-\infty}^\infty f(t) \, \psi\left(\frac{t - b}{a}\right) dt,
$$

donde $\psi(t)$ es la función madre wavelet, $a \in \mathbb{R}^+$ es el parámetro de escala (dilatación o compresión), y $b \in \mathbb{R}$ es el parámetro de traslación en el tiempo [1]. La función wavelet debe cumplir ciertas condiciones de admissibilidad, incluyendo tener media cero, para garantizar la reconstrucción de la señal original a partir de su transformada.

La descomposición permite analizar la señal en diferentes escalas y posiciones temporales, lo cual es clave para capturar características no estacionarias y transitorias. La transformada wavelet discreta (DWT) se basa en la discretización de a y b, típicamente en potencias de dos, lo que permite una implementación computacional eficiente mediante bancos de filtros pasa bajos y pasa altos [1][2].

En el procesamiento biomédico, esta capacidad multiresolución es aprovechada para filtrar ruido y detectar características fisiológicas relevantes en señales complejas [3][5].

Diversas variantes y optimizaciones de la transformada wavelet, como la transformada wavelet estacionaria (SWT) y la transformada wavelet empírica (EWT), han sido propuestas para mejorar la calidad del filtrado y adaptarse mejor a señales biomédicas específicas [3][6].

---

## 2. Propósito de la práctica <a name="propósito-de-la-práctica"></a>

Implementar y comparar técnicas de filtrado basadas en la transformada wavelet para la reducción de ruido en señales biomédicas (ECG, EMG y EEG), evaluando la eficiencia y calidad de la señal filtrada para cada tipo de señal y contexto.

---
## 3. Materiales y metodología <a name="materiales-y-metodología"></a>

**Materiales y equipos:**  
- Computadora con Python 3.12 instalado  
- Librerías Python: pywt (PyWavelets), numpy, matplotlib, scipy, neurokit2  
- Señales biomédicas adquiridas en prácticas previa (EMG, ECG y EEG)

**Metodología:**  

1. **Adquisición y carga de señales:** Se utilizaron señales ECG, EMG y EEG previamente registradas y almacenadas en archivos digitales.

2. **Visualización inicial:** Se graficaron las señales crudas para evaluar la presencia y características del ruido y artefactos.

3. **Aplicación de la transformada wavelet discreta (DWT):**  
 - Se seleccionaron familias wavelet específicas según el tipo de señal (por ejemplo, Symlet 4 y Coiflet 3 para ECG; Coiflet 5 para EEG).  
 - Se definió un nivel óptimo de descomposición.  
 - Se aplicó umbralización suave (*soft thresholding*) sobre los coeficientes para atenuar el ruido, usando umbrales fijos o adaptativos según la literatura y ajustes experimentales.

4. **Reconstrucción de señal:** Se reconstruyó la señal filtrada usando los coeficientes umbralizados.

5. **Comparación y análisis:** Se compararon señales originales y filtradas visualmente y con métricas cuantitativas (si se disponen), para evaluar la efectividad del filtrado.
---

## 4. Resultados y Discusión <a name="resultados-y-discusion"></a>

### 4.1 Filtrado de señal ECG <a name="filtrado-de-señal-ecg"></a>

Las señales ECG mostraron ruido característico debido a interferencias electromagnéticas y artefactos de movimiento. Se aplicaron filtros DWT con wavelets Symlet 4 y Coiflet 3 en niveles 3 a 7. Ambas configuraciones lograron reducir significativamente el ruido, conservando la morfología característica de los complejos QRS. Sin embargo, Coiflet 3 mostró un filtrado más suave en condiciones de ruido moderado a alto, lo que concuerda con hallazgos previos en la literatura.

### 4.2 Filtrado de señal EMG <a name="filtrado-de-señal-emg"></a>

En señales EMG, el filtrado wavelet fue efectivo para eliminar artefactos de movimiento y ruido muscular. Se observó que la elección adecuada de la familia wavelet y el nivel de descomposición son cruciales para preservar la información fisiológica relevante, como la actividad muscular en contracciones leves y fuertes.

### 4.3 Filtrado de señal EEG <a name="filtrado-de-señal-eeg"></a>

Para las señales EEG se utilizó un filtro DWT basado en wavelet Biorthogonal 2.6 a nivel 5, que mostró alta capacidad para separar componentes de baja y alta frecuencia, reduciendo el ruido sin pérdida significativa de información cerebral. Esta configuración es recomendada para estudios neurológicos que requieren alta fidelidad en la señal.

| Estado                 | RAW                | Señal Filtrada       | 
|-----------------------|--------------------|--------------------|
|Basal                 | ![Raw 1](./Imágenes%20en%20el%20anexo/BasalRaw.png)| ![FIR](./Imágenes%20en%20el%20anexo/BasalFiltrada.png) | 
|Tarea Cognitiva      |![Raw 2](./Imágenes%20en%20el%20anexo/TareaCognitivaRaw.png)|![FIR](./Imágenes%20en%20el%20anexo/TareaCognitiva.png)|
|Artefactos      |![Raw 2](./Imágenes%20en%20el%20anexo/ArtefactosRaw.png)|![FIR](./Imágenes%20en%20el%20anexo/ArtefactosFiltrada)|
|Actividad Libre  |![Raw 3](./Imágenes%20en%20el%20anexo/ActividadLibre.png)|![FIR](./Imágenes%20en%20el%20anexo/ActividadLibre.png)|

---

## 5. Conclusiones <a name="conclusiones"></a>

ESTO FALTA CORREGIR!!!!
La transformada wavelet discreta es una herramienta poderosa y versátil para el procesamiento y filtrado de señales biomédicas, permitiendo la reducción de ruido y preservación de características morfológicas clave en ECG, EMG y EEG. La elección de la familia wavelet, el nivel de descomposición y la estrategia de umbralización son determinantes para el éxito del filtrado.

En particular, los filtros basados en Coiflet y Biorthogonal demostraron superioridad en condiciones de ruido variable, adaptándose bien a las necesidades específicas de cada tipo de señal biomédica. Por lo tanto, la transformada wavelet es recomendada para aplicaciones clínicas y de investigación que demandan análisis robustos y confiables de señales biomédicas no estacionarias.

---

## 6. Referencias <a name="referencias"></a>

[1] S. Mallat, A Wavelet Tour of Signal Processing, 3rd ed., Academic Press, San Diego, 2009. Disponible en: https://rafat.github.io/sites/wavebook/intro/fb2.html

[2] C. Li, H. Deng, S. Yin et al., “sEMG signal filtering study using synchrosqueezing wavelet transform with differential evolution optimized threshold,” Results in Engineering, vol. 18, 101150, 2023. https://doi.org/10.1016/j.rineng.2023.101150

[3] A. Phinyomark, C. Limsakul, P. Phukpattaranont, “Application of Wavelet Analysis in EMG Feature Extraction for Pattern Classification,” Measurement Science Review, vol. 11, no. 2, pp. 70-83, 2011. [https://doi.org/10.2478/v10048-011-0009-y](https://www.researchgate.net/publication/241475036_Application_of_Wavelet_Analysis_in_EMG_Feature_Extraction_for_Pattern_Classification)

[4] P. Zandiyeh et al., “Wavelet analysis reveals differential lower limb muscle activity patterns long after anterior cruciate ligament reconstruction,” Journal of Biomechanics, vol. 133, p. 110957, 2022. https://doi.org/10.1016/j.jbiomech.2022.110957

[5] S. Elouaham et al., “Empirical Wavelet Transform Based ECG Signal Filtering Method,” Journal of Electrical and Computer Engineering, vol. 2024, Article ID 9050909, 2024. https://doi.org/10.1155/2024/9050909

[6] G. Cornelia y R. Romulus, “ECG Signals Processing Using Wavelets,” University of Oradea, Electronics Department, Faculty of Electrical Engineering and Information Technology, Oradea, Rumania. Disponible en: https://www.sciencedirect.com/science/article/pii/S2590123023002773
