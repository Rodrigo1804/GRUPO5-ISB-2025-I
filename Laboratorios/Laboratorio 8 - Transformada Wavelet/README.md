# Laboratorio 8: Transformada Wavelet

## Contenido
1. [Introducción](#introducción)  
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y Discusión](#resultados-y-discusion)  
 4.1 [Filtrado de señal ECG](#filtrado-de-señal-ecg)  
 4.2 [Filtrado de señal EMG](#filtrado-de-señal-emg)  
 4.3 [Filtrado de señal EEG](#filtrado-de-señal-eeg)
5. [Conclusiones](#conclusiones)  
 5.1 [Conclusiones ECG](#conclusiones-ecg)  
 5.2 [Conclusiones EMG](#conclusiones-emg)  
 5.3 [Conclusiones EEG](#conclusiones-eeg) 
6. [Referencias](#referencias)  

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

| Familia de funciones Wavelet | Nivel | Threshold utilizado                         | Tipo de Threshold           | Coeficiente de Aproximación | Coeficientes de Detalle                                                       |
|------------------------------|--------|----------------------------------------------|------------------------------|------------------------------|--------------------------------------------------------------------------------|
| Symlet 4 (`sym4`)            | 10     | Umbral adaptativo por nivel (`λ_j`)          | Función mejorada  | A10                         | D1, D2, D3, D4, D5, D6, D7, D8, D9, D10 (cada uno umbralizado con `f_i(x, λ_j)`) |

Para filtrar nuestras señales EMG, utilizamos los parámetros y metodología propuestos en la literatura encontrada para mejorar la relación entre eliminación de ruido y preservación de señal útil [y].  
Específicamente, se aplicó una descomposición por wavelet discreta (DWT) utilizando la función madre Symlet 4 (`sym4`), con un nivel de descomposición de 10. A cada conjunto de coeficientes de detalle se le aplicó un umbral adaptativo por nivel (λⱼ), seguido de una función de umbralización mejorada, la cual incorpora los parámetros de ajuste μ = 0.91 y δ = 0.01.  

| Músculo   | RAW | Señal Filtrada |
|----------|-----|----------------|
| **Bíceps**   | <img src="./Imágenes en el anexo/BicepsRaw.png" width="800"/>   | <img src="./Imágenes en el anexo/BicepsFiltrada.png" width="800"/> |
| **Tríceps**  | <img src="./Imágenes en el anexo/TricepsRaw.png" width="800"/>  | <img src="./Imágenes en el anexo/TricepsFiltrada.png" width="800"/> |
| **Hombro**   | <img src="./Imágenes en el anexo/HombroRaw.png" width="800"/>   | <img src="./Imágenes en el anexo/HombroFiltrada.png" width="800"/> |



### 4.3 Filtrado de señal EEG <a name="filtrado-de-señal-eeg"></a>

#### Parámetros utilizados para el filtrado
| Familia de funciones Wavelet| Nivel | Threshold utilizado | Tipo de Threshold |Coeficiente de Aproximación | Coeficientes de Detalle | 
|-----------------------------|-------|---------------------|-------------------|----------------------------|-----------------------------|
| Coiflet 5 (coif5)          | 6    |SURE (Stain's Unbiased Risk Estimate)   |  Soft Thresholding |  A5 | D1, D2, D3, D4, D5, D6 (cada uno umbralizado con SURE y Soft)  | 

Para filtrar nuestras señales EEG, nos basamos en los parámetros utilizados en la literatura encontrada [i]. Se utilizó Coiflet 5 debido a la buena resolución en tiempo y frecuencia, su preservación de la onda original y la reducción de la dispersión temporal de los coeficientes, esto último facilita localizar de manera efectiva los artefactos de la señal cruda. 

En cuanto al umbral, se utilizó el método de umbralización adaptativo, en este caso SURE, el cual minimiza el error cuadrático medio estimado (MSE) y es robusto ante los diferentes tipos de ruido como los artefactos musculares y oculares. En el artículo no se menciona de manera explícita la fórmula utilizada puesto que existen dos la general (1) y la simplificada (2); sin embargo, dentro de las referencias del mismo encontramos un artículo donde se utilizan las reglas de Donoho y Johnstone [ii] para el SURE thresholding. Dicha versión corresponde a la versión simplificada en donde se calcula, para cada nivel de detalle, un umbral óptimo. Para poder minimizar el MSE, se aplica el SURE mediante _soft thresholding_ a los coeficientes transformados para la cual se utiliza la fórmula simplificada (2).

$$
\text{SURE}(h) = \|\theta\|^2 + \|h(x)\|^2 + 2\sigma^2 \sum_{i=1}^{n} \frac{\partial h_i}{\partial x_i} - 2 \sum_{i=1}^{n} x_i h_i(x) ... (1)
$$

$$
\text{SURE}(\lambda) = n \cdot \sigma^2 + \sum_{i=1}^{n} \min(d_i^2, \lambda^2) - 2 \cdot \sigma^2 \cdot \vert \{ i : |d_i| < \lambda \} \vert  ...(2)
$$

donde 𝜎 es la desviación estándar estimada de los coeficientes de detalle, y λ es el valor de umbral buscado numéricamente para minimizar la expresión. Esta última ecuación es la que  utilizamos para el thresholding en nuestras señales.


| Estado                 | RAW                | Señal Filtrada       | 
|-----------------------|--------------------|--------------------|
| Basal                 | ![Raw 1](./Imágenes%20en%20el%20anexo/BasalRaw.png)| ![DWT1](./Imágenes%20en%20el%20anexo/BasalFiltrada.png) | 
| Tarea Cognitiva      |![Raw 2](./Imágenes%20en%20el%20anexo/TareaCognitivaRaw.png)|![DWT2](./Imágenes%20en%20el%20anexo/TareaCognitivaFiltrada.png)|
| Artefactos      |![Raw 3](./Imágenes%20en%20el%20anexo/ArtefactosRaw.png)|![DWT3](./Imágenes%20en%20el%20anexo/ArtefactosFiltrada.png)|
| Actividad Libre  |![Raw 4](./Imágenes%20en%20el%20anexo/ActividadLibreRaw.png)|![DWT4](./Imágenes%20en%20el%20anexo/ActividadLibreFiltrada.png)|

---

| Familia de funciones Wavelet| Nivel | Threshold utilizado | Tipo de Threshold |Coeficiente de Aproximación | Coeficientes de Detalle | 
|-----------------------------|-------|---------------------|-------------------|----------------------------|-----------------------------|
| Daubechies 4 (Db4)          | 5    | Tj = C · (σ_dj(n) / σ_nV(n))|  Soft Thresholding | No se umbraliza | d1, d2, d3, d4, d5 (cada uno con umbral óptimo para PRD mínimo) | 

Para filtrar nuestras señales ECG, nos basamos en los parámetros utilizados en la literatura encontrada [ii]. Se utilizó Daubechies 4 debido a la preservación de la resolución tanto  en tiempo y frecuencia y por su uso clásico como filtro adaptativo para preservar ondas clave P,QRS y T.

Sobre el umbral, se utilizó el método de umbralización adaptativo, en este caso Tj = C · (σ_dj(n) / σ_nV(n)) , el cual minimiza el error de Porcentaje de diferencia cuadrática media (PRD). Por otro lado, en el paper se explica la decisión de no aplicar umbralización a los coeficientes de aproximación ya que estos contienen las componentes de baja frecuencia de la señal, donde residen las ondas P y T del ECG, que son suaves y fácilmente distorsionables, por lo que al filtrarlos se perdería información sútil pero importante, en este caso para analizar la morfología de la señal.

| Estado                 | RAW                | Señal Filtrada       | 
|-----------------------|--------------------|--------------------|
| Reposo               | ![Raw 1](./Imágenes%20en%20el%20anexo/r-og.jpg)| ![DWT1](./Imágenes%20en%20el%20anexo/f-reposo.jpg) | 
| Inhalación 1     |![Raw 2](./Imágenes%20en%20el%20anexo/in1-og.jpg)|![DWT2](./Imágenes%20en%20el%20anexo/f-in1.jpg)|
| Actividad Física     |![Raw 3](./Imágenes%20en%20el%20anexo/og-af.jpg)|![DWT3](./Imágenes%20en%20el%20anexo/f-af.jpg)|
| Inhalación 2 |![Raw 4](./Imágenes%20en%20el%20anexo/in2-og.jpg)|![DWT4](./Imágenes%20en%20el%20anexo/in2-f.jpg)|

## 5. Conclusiones <a name="conclusiones"></a>

### 5.1 Conclusiones ECG <a name="conclusiones-ecg"></a>

### 5.2 Conclusiones EMG <a name="conclusiones-emg"></a>
El propósito de filtrar nuestra señal EMG con DWT fue mejorar la calidad de las señales de cada uno de los músculos evaluados, eliminando ruido sin comprometer los componentes fisiológicamente relevantes mediante el uso de umbral mejorado basada en wavelets. Los intervalos importantes a considerar para nuestro análisis son:
- Descanso: 0s - 40s
- Contracción leve: 40s - 60s
- Contracción fuerte: 70s - 120s

**Señal de Bíceps:**
  - Periodo de descanso: La señal "raw" presentaba una base levemente oscilante, con actividad probablemente inducida por el ruido de baja frecuencia o artefactos de movimiento, luego del filtrado, se estabilizó casi por completo. El umbral adaptativo aplicado a cada nivel de descomposición wavelet logró eliminar casi todo el ruido basal sin introducir distorsiones de borde ni "efectos de corte" típicos del hard thresholding [y].
    
  - Contracción leve: Aquí la señal mostraba una actividad muscular con amplitud moderada que a pesar de su bajo nivel de energía, la función de umbral mejorado con los parámetros que seleccionamos (μ = 0.91 y δ = 0.01) permitió conservar esta región. Esto se debe a que el algoritmo atenúa los coeficientes solo cuando son similares al umbral, evitando sobre-filtrado. [y]
    
  - Contracción fuerte: Luego de filtrar la señal vemos una mejora significativa ya que los picos altos se preservan con claridad, y la estructura general de la contracción se mantiene. Esto nos indica que el método no elimina componentes de alta energía relevantes.

Por lo tanto, esta señal nos muestra que el algoritmo respetó la morfología muscular durante contracción, sin comprometer los picos fisiológicos. El uso de Symlet 4 como base wavelet fue ideal para este tipo de señales que combinan secciones suaves con otras abruptas. [y]

**Señal de Tríceps:**
  - Periodo de descanso: Se evidenció (al principio) un mayor nivel de ruido, incluso con artefactos "impulsivos". La aplicación del método que escogimos logró limpiar eficazmente el ruido sin afectar la señal útil. Este resultado que obtuvimos valida que el umbral por nivel adapta su "agresividad" según el contexto espectral del detalle. [y]
    
  - Contracción leve y fuerte: Ambas fases de la señal se mantuvieron prácticamente intactas luego del filtrado. Lo "destacable" aquí es que el algoritmo suavizó los bordes transitorios sin eliminar los eventos fisiológicos. A diferencia de los métodos tradicionales que producen el fenómeno tipo Gibbs en los bordes, la función mejorada introduce continuidad en el filtrado, como también se evidenció en las simulaciones del artículo que usamos de base. [y]

El filtrado de esta señal del Tríceps sirve como un buen ejemplo de cómo es que el filtrado wavelet adaptativo no solo "limpia", sino que respeta la naturaleza no estacionaria y multicomponente de la señal EMG.

**Señal de Hombro:**
  - Periodo de descanso: La señal incialmente (señal "raw") tenía tuido basal oscilante y pequeños picos no fisiológicos. Luego del filtrado, estos desaparecen casi por completo, permitiéndonos identificar con claridad todo este periodo de inactividad (reposo). Esta capacidad es esencial para segmentar la fases que sí son activas y las que no lo son en señales EMG.
    
  - Contracción leve: Al igual que en la señal del Bíceps, esta fase fue preservada casi por completo, aunque con cierta atenuación. Esto fue esperable ya que los eventos de muy baja amplitud pueden acercarse al umbral de detección, pero gracias a los parámetros que escogimos (μ y δ), el sistema favoreció una transición suave y no "agresiva" hacia el filtrado.
    
  - Contracción fuerte: Las contracciones son evidentes, amplias y bien definidas luego del filtrado. El sistema conservó los picos de activación sin introducción de artefactos. Esto demuestra que la resolución temporal y frecuencial del algoritmo que utilizamos fue la adecuada para nuestra señal, la cual es ciertamente compleja por el contenido "mixto" de frecuencias que posee.

Esta señal valida la aplicación del método que escogimos a músculos con diferentes picos de activación, mostrando una muy buena versatilidad.

Finalmente, podemos concluir que el uso del umbral mejorado adaptativo ("función mejorada") que aplicamos sobre una descomposición wavelet multiescala no solo mejora la relación señal/ruido (SNR), sino que también conserva la integridad fisiológica de la señal EMG, esto gracias a su capacidad de adaptarse a señales con diferentes contenidos de frecuencia. También, la estabilidad que posee durante el reposo reduce el riesgo de falsos positivos, así como la robustez frente a contracciones intensas, sin atenuar picos ni distorsionar la señal.

### 5.3 Conclusiones EEG <a name="conclusiones-eeg"></a>
Luego de realizar el filtrado mediante la Transformada de Wavelet Discreta (DWT) con la función madre Coiflet 5 y la umbralización adaptativa SURE combinada con soft thresholding, vemos que en nuestras señales de actividad basal y tarea cognitiva se mantienen oscilaciones coherentes con EEG ya que nuestra señal, a pesar de haber recibido el filtrado, no ha perdido su la forma característica de este tipo de datos. Esto nos indica que no se ha eliminado información útil de nuestra señal lo que es esperado del método de soft thresholding adaptativo utilizado.

En el estado de Artefactos, al momento de tomar las señales, se había considerado como artefacto al movimiento ocular (parpadear) y masticar, que son los artefactos mencionados también en nuestro artículo de referencia [i]. En esta señal, luego de filtrarla, podemos verificar una notoria diferencia puesto que hay picos que han reducidos significativamente y aún así se ha mantenido conservada nuestra señal. Esto nos indica que el SURE threshold utilizado ha eliminado los componentes de ruido sin eliminar data significativa.

Finalmente, en el estado de Actividad Libre, tenemos una mezcla de estímulos de la persona de quien se tomó las medidas debido a los diferentes tipos de música que escuchó, el filtrado conserva la señal y puede observarse que ha eliminado pequeñas perturbaciones que puedan haberse dado durante la toma de datos. Aquí comprobamos que el método SURE se adapta al contenido de la señal en cada nivel de detalle.

---

## 6. Referencias <a name="referencias"></a>

[1] S. Mallat, A Wavelet Tour of Signal Processing, 3rd ed., Academic Press, San Diego, 2009. Disponible en: https://rafat.github.io/sites/wavebook/intro/fb2.html

[2] C. Li, H. Deng, S. Yin et al., “sEMG signal filtering study using synchrosqueezing wavelet transform with differential evolution optimized threshold,” Results in Engineering, vol. 18, 101150, 2023. https://doi.org/10.1016/j.rineng.2023.101150

[3] A. Phinyomark, C. Limsakul, P. Phukpattaranont, “Application of Wavelet Analysis in EMG Feature Extraction for Pattern Classification,” Measurement Science Review, vol. 11, no. 2, pp. 70-83, 2011. [https://doi.org/10.2478/v10048-011-0009-y](https://www.researchgate.net/publication/241475036_Application_of_Wavelet_Analysis_in_EMG_Feature_Extraction_for_Pattern_Classification)

[4] P. Zandiyeh et al., “Wavelet analysis reveals differential lower limb muscle activity patterns long after anterior cruciate ligament reconstruction,” Journal of Biomechanics, vol. 133, p. 110957, 2022. https://doi.org/10.1016/j.jbiomech.2022.110957

[5] S. Elouaham et al., “Empirical Wavelet Transform Based ECG Signal Filtering Method,” Journal of Electrical and Computer Engineering, vol. 2024, Article ID 9050909, 2024. https://doi.org/10.1155/2024/9050909

[6] G. Cornelia y R. Romulus, “ECG Signals Processing Using Wavelets,” University of Oradea, Electronics Department, Faculty of Electrical Engineering and Information Technology, Oradea, Rumania. Disponible en: https://www.sciencedirect.com/science/article/pii/S2590123023002773

[y]  Y. Ouyang, Z. Deng, Y. Yin, X. Wu, y Z. Chen, "An improved wavelet threshold denoising approach for surface electromyography signal," EURASIP Journal on Advances in Signal Processing, vol. 2023, no. 1, p. 10, Jan. 2023. https://doi.org/10.1186/s13634-023-01066-3

[i] A. K. Bhoi and A. K. Mallick, "EEG De-noising using SURE Thresholding based on Wavelet Transform," International Journal of Computer Applications, vol. 24, no. 6, pp. 6–10, June 2011.

[ii] R. R. Coifman and D. L. Donoho, “Translation-Invariant Denoising,” in Wavelets and Statistics, A. Antoniadis, Ed., New York: Springer, 1995, pp. 125–150.
