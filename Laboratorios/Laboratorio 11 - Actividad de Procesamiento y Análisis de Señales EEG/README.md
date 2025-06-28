# Laboratorio de actividad de procesamiento y análisis de señales EEG

## Contenidos
1. [Origen de los Datos](#1-origen-de-los-datos)
2. [Preprocesamiento](#2-preprocesamiento)
3. [Extracción de Características](#3-extracción-de-características)
4. [Optimización y Selección de Features](#4-optimización-y-selección-de-features)
5. [Discusión](#6-discusion)
6. [Referencias](#7-referencias)



## 1. Origen de los Datos

**Fuente [1]:** [EEG Motor Movement/Imagery Dataset (EEGBCI)](https://physionet.org/content/eegmmidb/1.0.0/)

Esta base de datos está compuesta por 109 sujetos. Para cada caso, se realizaron las siguientes sesiones:

1. Basal: ojos abiertos
2. Basal: ojos cerrados
3. Tarea 1: abrir y cerrar el puño derecho o izquierdo
4. Tarea 2: imaginar que se abre y cierra el puño derecho o izquierdo
5. Tarea 3: abrir y cerrar ambos puños o ambos pies 
6. Tarea 4: imaginar que se abren y cierran ambos puños o ambos pies
7. Se volvieron a repetir las tareas 1-4.
  
Se utilizaron 64 electrodos con un sistema de distribución 10-10 y los datos se encuentran en formato `.edf´


## 2. Preprocesamiento
**Objetivo:** limpiar las señales de EEG mediante técnicas de filtrado (por ejemplo, filtros pasa banda, notch y wavelet), eliminar artefactos (blink, EMG, ECG) y normalizar/alinear las señales para hacerlas comparables entre sesiones y sujetos.

Para el laboratorio nos basaremos en la data del primer y segundo sujeto analizando solo la data de las primeras 6 actividades (que se indicaron previamente). Es decir, de la base de datos, utilizaremos los siguientes archivos: 
* Primer sujeto: `S001R01.edf  S001R02.edf  S001R03.edf  S001R04.edf  S001R05.edf  S001R06.edf  S001R07.edf`
* Segundo sujeto: `S002R01.edf  S002R02.edf  S002R03.edf  S002R04.edf  S002R05.edf  S002R06.edf  S002R07.edf`  

**Pasos a seguir:**
1. Carga de datos: Se cargaron los datos `.edf` utilizando la función `mne.io.read_raw_edf()`. Los datos del archivo se almacenaron en `raw`
2. Visualización de la señal cruda (`raw`): se utiliza la herramienta `raw.plot()` visualizamos los primeros 10 segundos y utilizamos `scalings='auto'` para evitar que los canales se superpongan al visualizar el ploteo.
3. Filtración de la señal: se aplicó un filtro pasa-banda con un rango de frecuencias de 1 a 40 Hz. Esto garantiza la eliminación de ruidos de baja y alta frecuencia que se encuentran fuera del rango para la actividad EEG.
4. Filtro Notch: se aplica un filtro Notch a 60 Hz para eliminar la interferencia que haya podido generar la red eléctrica. Es decir, eliminamos ruidos de alta frecuencia.
5. Análisis ICA: este análisis permite identificar y eliminar artefactos como el parpadeo o movimientos musculares que pueden distorsionar la data de interés. Los componentes identificados son excluídos de la señal para luego ser eliminados mediante la corrección ICA. El resultado será una señal limpia.
6. Se aplica una normalización a la señal ya limpia. Esto permitirá comparar con otras de las tareas realizadas o con otro sujeto.
7. Visualización de señal filtrada y normalizada: al igual que en la señal cruda, visualizamos los 10 primeros segundos de la señal, ahora filtrada y usamos `scalings='auto'`para evitar solapamiento de los canales

**Resultados obtenidos**
### Paciente 1:
| Actividad                 | Señal Filtrada                |
|-----------------------|--------------------|
| Basal 1               | ![BASAL1_PACIENTE_1](./Imágenes_Lab11/BASAL1_PACIENTE_1.png)|
| Basal 2     |![BASAL2_PACIENTE_1](./Imágenes_Lab11/BASAL2_PACIENTE_1.png)|
| Tarea 1     |![TAREA1_PACIENTE_1](./Imágenes_Lab11/TAREA1_PACIENTE_1.png)|
| Tarea 2 |![TAREA2_PACIENTE_1](./Imágenes_Lab11/TAREA2_PACIENTE_1.png)|
| Tarea 3 |![TAREA3_PACIENTE_1](./Imágenes_Lab11/TAREA3_PACIENTE_1.png)|
| Tarea 4 |![TAREA4_PACIENTE_1](./Imágenes_Lab11/TAREA4_PACIENTE_1.png)|


### Paciente 2:
| Actividad                 | Señal Filtrada                |
|-----------------------|--------------------|
| Basal 1               | ![BASAL1_PACIENTE_2](./Imágenes_Lab11/BASAL1_PACIENTE_2.png)|
| Basal 2     |![BASAL2_PACIENTE_2](./Imágenes_Lab11/BASAL2_PACIENTE_2.png)|
| Tarea 1     |![TAREA1_PACIENTE_2](./Imágenes_Lab11/TAREA1_PACIENTE_2.png)|
| Tarea 2 |![TAREA2_PACIENTE_2](./Imágenes_Lab11/TAREA2_PACIENTE_2.png)|
| Tarea 3 |![TAREA3_PACIENTE_2](./Imágenes_Lab11/TAREA3_PACIENTE_2.png)|
| Tarea 4 |![TAREA4_PACIENTE_2](./Imágenes_Lab11/TAREA4_PACIENTE_2.png)|

## 3. Extracción de Características
**Objetivo:** aplicar técnicas de feature engineering sobre las componentes extraídas (estadísticas, bandas, transformaciones) para mejorar la calidad de los datos antes de alimentar modelos de clasificación.
## 4. Optimización y Selección de Features
**Objetivo:** integrar y analizar los datos a través de observaciones temporales, frecuenciales y espaciales empleando MNE Python (Epochs, Evoked, montage, interpolate_bads).

## 5. Resultados PCA

**Resultados obtenidos**

### Paciente 1:
| Actividad                 | PCA Obtenido               |
|-----------------------|--------------------|
| Basal 1               | ![BASAL1_PACIENTE_1](./Imágenes_Lab11/BASAL_1_PACIENTE_1_PCA.png)|
| Basal 2     |![BASAL2_PACIENTE_1](./Imágenes_Lab11/BASAL_2_PACIENTE_1_PCA.png)|
| Tarea 1     |![TAREA1_PACIENTE_1](./Imágenes_Lab11/TAREA_1_PACIENTE_1_PCA.png)|
| Tarea 2 |![TAREA2_PACIENTE_1](./Imágenes_Lab11/TAREA_2_PACIENTE_1_PCA.png)|
| Tarea 3 |![TAREA3_PACIENTE_1](./Imágenes_Lab11/TAREA_3_PACIENTE_1_PCA.png)|
| Tarea 4 |![TAREA4_PACIENTE_1](./Imágenes_Lab11/TAREA_4_PACIENTE_1_PCA.png)|


### Paciente 2:
| Actividad                 | PCA Obtenido               |
|-----------------------|--------------------|
| Basal 1               | ![BASAL1_PACIENTE_2](./Imágenes_Lab11/BASAL_1_PACIENTE_2_PCA.png)|
| Basal 2     |![BASAL2_PACIENTE_2](./Imágenes_Lab11/BASAL_2_PACIENTE_2_PCA.png)|
| Tarea 1     |![TAREA1_PACIENTE_2](./Imágenes_Lab11/TAREA_1_PACIENTE_2_PCA.png)|
| Tarea 2 |![TAREA2_PACIENTE_2](./Imágenes_Lab11/TAREA_2_PACIENTE_2_PCA.png)|
| Tarea 3 |![TAREA3_PACIENTE_2](./Imágenes_Lab11/TAREA_3_PACIENTE_2_PCA.png)|
| Tarea 4 |![TAREA4_PACIENTE_2](./Imágenes_Lab11/TAREA_4_PACIENTE_2_PCA.png)|

## 6. Discusión

## Discusión de Resultados - Análisis PCA sobre Señales EEG

El análisis de componentes principales (PCA) fue aplicado a las características extraídas de las señales EEG correspondientes a las tareas motoras e imaginadas de dos pacientes. Esta técnica permitió reducir la dimensionalidad de los datos y visualizar la distribución espacial de las muestras en un espacio de dos componentes principales (PC1 y PC2), facilitando la identificación de patrones, agrupamientos y outliers.


### Paciente 1

- **Basal 2:** Se observa una nube de puntos agrupada con pocos valores atípicos, indicando una actividad cerebral estable en estado de reposo.
- **Tarea 1 (movimiento real):** Hay una dispersión mayor con algunos outliers, lo que sugiere una mayor variabilidad neurológica asociada al movimiento.
- **Tarea 2 (imaginación):** Aumenta la dispersión en la dirección de PC2, posiblemente reflejando diferencias individuales en la ejecución de la tarea imaginada.
- **Tarea 3 (ambos puños/pies):** Presencia de dos puntos fuertemente alejados del centro, los cuales podrían representar artefactos o respuestas fisiológicas anómalas.
- **Tarea 4 (imaginación de ambos):** Se evidencia un patrón elíptico alargado en PC1, con un valor atípico extremo en torno a 300, lo que indica una señal fuera del comportamiento típico.


### Paciente 2

- **Basal 2:** Los datos están distribuidos mayormente hacia el lado izquierdo del gráfico, con una dispersión moderada y sin outliers pronunciados.
- **Tarea 1:** Se observa un outlier destacado alrededor del punto (200, 100), probablemente asociado a una respuesta neural fuerte o un artefacto puntual.
- **Tarea 2:** La distribución es compacta, similar a la del estado basal, indicando una posible menor activación durante la tarea imaginada.
- **Tarea 3:** Se forma un patrón diagonal descendente, con dispersión considerable en ambas componentes, reflejando activaciones heterogéneas.
- **Tarea 4:** Predomina una nube compacta con algunos puntos lejanos, especialmente uno con una puntuación muy alta en PC1, lo que puede estar relacionado con una activación mental intensa o una diferencia sustancial entre ensayos.


### Comparación General

- Las **condiciones basales** tienden a presentar menor dispersión y mayor homogeneidad.
- Las **tareas reales** (Tarea 1 y 3) presentan mayor variabilidad en la distribución de las componentes principales, lo cual es coherente con una mayor activación y dinamismo cerebral.
- Las **tareas imaginadas** (Tarea 2 y 4) muestran patrones más controlados en algunos casos, aunque no exentos de valores atípicos.
- **Paciente 2** evidencia mayor separación entre tareas en comparación con **Paciente 1**, lo que podría implicar una mayor diferenciación de estados mentales.

---

## Conclusiones y Recomendaciones

- Se identificaron patrones diferenciados en la actividad cerebral entre tareas y pacientes.
- Es importante considerar la eliminación o estudio separado de **outliers extremos**, ya que podrían afectar el rendimiento de modelos de clasificación posteriores.
- Se sugiere complementar este análisis con técnicas como **t-SNE** o **UMAP** para capturar relaciones no lineales que el PCA no detecta.
- Finalmente, se recomienda analizar la **varianza explicada** por cada componente para validar la representatividad del espacio PCA generado.
  
## 7. Referencias
[1] Schalk, G., McFarland, D.J., Hinterberger, T., Birbaumer, N., Wolpaw, J.R. BCI2000: A General-Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering 51(6):1034-1043, 2004.
