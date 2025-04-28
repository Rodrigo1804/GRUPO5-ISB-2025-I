# Laboratorio 5: Adquisición de señal ECG con BITalino

## Contenido:
1. [Introducción](#introducción)
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y limitaciones](#resultados-y-limitaciones)  
5. [Referencias](#referencias)

## 1. Introducción <a name="introducción"></a>

El **electrocardiograma (ECG)** es una herramienta diagnóstica fundamental que permite registrar la actividad eléctrica del corazón de forma no invasiva, rápida y precisa. Es ampliamente utilizado para detectar alteraciones en el ritmo cardíaco, identificar infartos, evaluar el estado del sistema de conducción del corazón y diagnosticar diversas enfermedades cardiovasculares.

Durante cada latido, el corazón genera impulsos eléctricos que se propagan por sus estructuras. Estos impulsos pueden ser detectados desde la superficie del cuerpo mediante **electrodos** adhesivos conectados a un dispositivo de registro. Las señales obtenidas muestran una serie de ondas, conocidas como **onda P, complejo QRS, onda T y onda U**, que reflejan la secuencia de despolarización y repolarización del tejido cardíaco.

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Figura1_OndasECG.jpg" alt="Ondas del ECG" width="60%">
  <p><strong>Figura 1:</strong> Ondas del Electrocardiograma.</p>
</div>

- **Onda P**: Activación de las aurículas.
- **Complejo QRS**: Despolarización de los ventrículos.
- **Onda T**: Repolarización ventricular.
  
Para realizar un ECG clínico completo, se colocan **10 electrodos** en el cuerpo del paciente, distribuidos de la siguiente forma:

- **6 electrodos precordiales**: colocados en el pecho (V1 a V6), captan la actividad eléctrica desde planos horizontales.
- **4 electrodos de extremidades**: ubicados en ambos brazos y piernas (RA, LA, RL, LL), captan la actividad desde planos frontales.

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Figura2_DerivacionesPrecordiales.png" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 2:</strong> Ubicación de las derivaciones precordiales V1 a V6 sobre el tórax [2].</p>
</div>

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Figura3_ElectrodosExtremidades.png" alt="Electrodos de extremidades" width="50%">
  <p><strong>Figura 3:</strong> Posición de los electrodos en extremidades para derivaciones RA, LA, RL y LL [2].</p>
</div>

Aunque se colocan 10 electrodos, el sistema de registro genera **12 derivaciones** en total. Esto es posible gracias a que las derivaciones no corresponden a los electrodos como tal, sino a las **diferencias de potencial (direcciones de observación)** entre pares específicos de electrodos[1][2]:

- **6 derivaciones de miembros (plano frontal):**
  - **Bipolares:** DI (RA-LA), DII (RA-LL), DIII (LA-LL)
  - **Unipolares aumentadas:** aVR, aVL, aVF

- **6 derivaciones precordiales (plano horizontal):**
  - V1, V2, V3, V4, V5, V6 (cada una mide respecto a un electrodo virtual de referencia)

Estas derivaciones permiten observar la actividad eléctrica del corazón desde distintos ángulos, proporcionando una visión completa en 3D de la función cardíaca. Gracias a esto, el ECG es capaz de localizar con precisión el origen de una arritmia o la zona afectada en un infarto.

En esta práctica, se trabajará con una configuración simplificada utilizando un sistema de tres electrodos y el dispositivo **BITalino**, captando una señal equivalente a una derivación (generalmente Lead I) y analizando su comportamiento en distintas condiciones fisiológicas.

 ## 2. Propósito de la práctica: <a name="propósito-de-la-práctica"></a>
El propósito de esta práctica es adquirir señales ECG utilizando el kit BITalino, evaluando su comportamiento bajo distintas condiciones fisiológicas: reposo, apnea y post-ejercicio. Asimismo, se busca familiarizarse con el uso del software *OpenSignals* para visualizar biopotenciales y realizar un análisis básico en Python en el dominio del tiempo y la frecuencia.

 ## 3. Materiales y metodología: <a name="materiales-y-metodología"></a> 
 ### Materiales:
 | Cantidad | Descripción                         |
|----------|-------------------------------------|
| 1        | KIT BITalino (r)evolution con módulos ECG           |
| 1        | Laptop/celular con Bluetooth                |
| 1        | Software OpenSignals (r)evolution   |
| 5        | Electrodos adhesivos de superficie            |
| 1        | Cable de 3 conductores (para ECG)   |
| 1        | Batería LiPo 3.7V                   |
| 1        | Simulador ProSim 4             |



### Metodología
1. **Preparación del sistema**
   - Encender el dispositivo BITalino.
   - Emparejar vía Bluetooth con la laptop (PIN: 1234).
   - Abrir OpenSignals y seleccionar el canal ECG.

2. **Colocación de electrodos**
   - **Rojo (activo +):** debajo del pectoral derecho.
   - **Blanco (referencia -):** debajo del pectoral izquierdo.
   - **Negro (GND):** costado del torso o zona neutra.
   - Verificar que la señal se estabilice en OpenSignals.
  
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Figura4_PosicionElectrodos.jpg" alt="Posición de electrodos" width="50%">
  <p><strong>Figura 4:</strong> Posición de los electrodos.</p>
</div>   

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Figura5_ConexionBitalino.png" alt="Posición de electrodos" width="50%">
  <p><strong>Figura 5:</strong> Conexión con el Bitalino.</p>
</div>  

3. **Condiciones evaluadas**
   - **Reposo basal:** sujeto sentado, relajado.
   - **Apnea (10s):** contención de la respiración.
   - **Post-esfuerzo:** luego de 5 minutos de actividad física leve.
   - *(Opcional)* simulación ECG con ProSim.

      [Video realizando actividad física](https://youtube.com/shorts/KNphvw5y52I?feature=share)

4. **Registro audiovisual del procedimiento**

| Condición | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Estado basal | [🎥 Ver video](https://youtube.com/shorts/vVY88n9KfAk?feature=share) |[🎥 Ver video](https://youtube.com/shorts/2bLt-sYCtmI?feature=share)|[🎥 Ver video](https://youtube.com/shorts/s4G-Rlms8AA?feature=share)|
| Apnea (10s) | [🎥 Ver video](https://youtube.com/shorts/9ByDjbO6oqQ?feature=share) |[🎥 Ver video](https://youtube.com/shorts/9BmTBhu1jpA?feature=share)|[🎥 Ver video](https://youtube.com/shorts/hejaDptHt4U?feature=share)|
| Post-ejercicio | [🎥 Ver video](https://youtube.com/shorts/hDtf_SdD4dA?feature=share) |[🎥 Ver video](https://youtube.com/shorts/B9SYISAgSFM?feature=share)|[🎥 Ver video](https://youtube.com/shorts/dsOA6KDlBD4?feature=share) |

4. **Exportación de datos**
   - Exportar archivos .txt desde OpenSignals para análisis posterior en Python.
   - 

## 4. Resultados y limitaciones <a name="resultados-y-limitaciones"></a>

###  Análisis en Python

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.fft import fft, fftfreq
from google.colab import drive

drive.mount('/content/drive')

# Ruta donde están tus señales
folder_path = '/content/drive/MyDrive/ECG_señales'

# Lista de todos los archivos .txt en la carpeta
file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Definir frecuencia de muestreo
fs = 1000  # Hz

# Iterar sobre cada archivo
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    
    # Cargar el archivo
    data = pd.read_csv(file_path, comment='#', sep='\t', header=None)
    data.columns = ['nSeq', 'I1', 'I2', 'O1', 'O2', 'A1', 'A2']
    
    # Extraer la señal (A1 o A2)
    senal = data['A1']
    
    # Crear vector de tiempo
    t = np.arange(len(senal)) / fs
    
    # ------------------------
    # Gráfica en dominio del TIEMPO
    # ------------------------
    plt.figure(figsize=(12,5))
    plt.plot(t, senal)
    plt.title(f'Señal en el dominio del tiempo: {file_name}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.xlim(0, 20)  
    plt.grid(True)
    plt.show()

    # ------------------------
    # Gráfica en dominio de la FRECUENCIA (dB)
    # ------------------------

    # Aplicar FFT
    N = len(senal)
    yf = fft(senal)
    xf = fftfreq(N, 1/fs)[:N//2]

    # Magnitud
    magnitud = np.abs(yf[0:N//2])

    # Magnitud en decibelios
    magnitud_db = 20 * np.log10(magnitud + 1e-12)  # le sumamos 1e-12 para evitar log(0)

    # Gráfica
    plt.figure(figsize=(12,5))
    plt.plot(xf, magnitud_db)
    plt.title(f'Señal en el dominio de la frecuencia (dB): {file_name}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud (dB)')
    plt.grid(True)
    plt.show()
```
  ### REPOSO:
| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo | <img src="./Imágenes%20en%20el%20anexo/Screenshot_23.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_25.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_27.jpg" alt="Posición de electrodos" width="80%"> |
| Dominio de la frecuencia |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_24.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_26.jpg" alt="Posición de electrodos" width="80%"> |<img src="./Imágenes%20en%20el%20anexo/Screenshot_28.jpg" alt="Posición de electrodos" width="80%"> |

#### Análisis de resultados
Durante la condición de reposo, en el domino del tiempo, reflejan una actividad cardíaca regular y se puede identificar los latidos como picos definidos. La segunda derivada presentan una señal más limpia, con menor cantidad de ruido y una mejor delimitación de los complejos cardíacos. Asimismo, los BPM calculados están entre 78 y 87 BPM, que están dentro del rango normal en reposo (60–100 BPM) [a]. 

En el análisis en el dominio de la frecuencia, se observa que la mayor concentración de energía se encuentra en el rango de 0.5 a 30 Hz, con un claro pico máximo cerca de 1 Hz. Este comportamiento es consistente con las frecuencias cardíacas fisiológicas, ya que el ECG humano típico concentra su energía entre 0.5 Hz y 40 Hz [b]. Además, la atenuación progresiva de la magnitud a partir de 40 Hz refuerza la calidad de la adquisición, dado que el rango por encima de esta frecuencia suele ser más afectado por artefactos eléctricos o musculares [c].


 
   ## INHALACIÓN 1:
| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo |<img src="./Imágenes%20en%20el%20anexo/Screenshot_11.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_13.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_15.jpg" alt="Posición de electrodos" width="80%">|
| Dominio de la frecuencia | <img src="./Imágenes%20en%20el%20anexo/Screenshot_12.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_14.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_16.jpg" alt="Posición de electrodos" width="80%"> |

#### Análisis de resultados
Durante la condición de inhalación , las señales de ECG registradas muestran una ligera variabilidad en las amplitudes respecto a la condición de reposo, particularmente en las primeras fases de la respiración. En el dominio del tiempo, las tres derivadas reflejan una actividad cardíaca rítmica, aunque se observa una modulación respiratoria que afecta levemente la estabilidad de la línea base. Esta variabilidad es esperada, ya que durante la inhalación profunda ocurre un fenómeno fisiológico llamado arritmia sinusal respiratoria, donde la frecuencia cardiaca aumenta levemente al inhalar y disminuye al exhalar [4]. En este contexto, la segunda derivada continúa mostrando la señal más limpia y estable, siendo la más adecuada para el análisis detallado de los ciclos cardíacos.

Respecto al análisis en el dominio de la frecuencia, se identifica nuevamente que la mayor concentración de energía se encuentra en el rango de 0.5 a 30 Hz, manteniéndose un pico máximo cercano a 1 Hz, similar al observado en reposo. Este comportamiento sigue siendo consistente con las frecuencias cardíacas fisiológicas típicas [5]. Sin embargo, comparado al reposo, se observa una ligera elevación de la energía en frecuencias muy bajas (por debajo de 0.5 Hz), atribuible al movimiento respiratorio [6]. La atenuación progresiva de la energía a partir de 40 Hz también se conserva, indicando que no hay una contaminación significativa de artefactos de alta frecuencia en la señal capturada.

   ### ACTIVIDAD FÍSICA:

| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo |<img src="./Imágenes%20en%20el%20anexo/Screenshot_5.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_7.jpg" alt="Posición de electrodos" width="80%">|   <img src="./Imágenes%20en%20el%20anexo/Screenshot_9.jpg" alt="Posición de electrodos" width="80%">|
| Dominio de la frecuencia | <img src="./Imágenes%20en%20el%20anexo/Screenshot_6.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_8.jpg" alt="Posición de electrodos" width="80%">| <img src="./Imágenes%20en%20el%20anexo/Screenshot_10.jpg" alt="Posición de electrodos" width="80%"> |
 

   ### POST ACTIVIDAD FÍSICA:
 | Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo |<img src="./Imágenes%20en%20el%20anexo/Screenshot_17.jpg" alt="Posición de electrodos" width="80%">|  <img src="./Imágenes%20en%20el%20anexo/Screenshot_19.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_21.jpg" alt="Posición de electrodos" width="80%">|
| Dominio de la frecuencia |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_18.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_20.jpg" alt="Posición de electrodos" width="80%">| <img src="./Imágenes%20en%20el%20anexo/Screenshot_22.jpg" alt="Posición de electrodos" width="80%">| 
 

 #### Análisis de resultados


 #### Limitaciones


##  Actividad Adicional

1. Como parte complementaria de esta práctica, se procesó la data obtenida utilizando la función ecg_process() de la librería neurokit2. La función ecg_process() nos brindará una señal filtrada y también nos permitirá identificar los picos (P, Q, S y T) más la frecuencia cardiaca.

  ### Señales procesadas
  #### Reposo

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoProcesado1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 6:</strong> Datos del estado de reposo procesado (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoProcesado2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 7:</strong> Datos del estado de reposo procesado (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoProcesado3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 8:</strong> Datos del estado de reposo procesado (III derivada).</p>
</div>

  #### Inhalación 1
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionProcesada1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 9:</strong> Datos del estado de primera inhalación procesado (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionProcesada2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 10:</strong> Datos del estado de primera inhalación procesado (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionProcesada3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 11:</strong> Datos del estado de primera inhalación procesado (III derivada).</p>
</div>

  #### Actividad física
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaProcesada1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 12:</strong> Datos del estado de reposo procesado (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaProcesada2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 13:</strong> Datos del estado de reposo procesado (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaProcesada3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 14:</strong> Datos del estado de reposo procesado (III derivada).</p>
</div>

  #### Post- actividad física
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2Procesada1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 15:</strong> Datos del estado post-actividad física procesado (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2Procesada2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 16:</strong> Datos del estado post-actividad física (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2Procesada3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 17:</strong> Datos del estado post-actividad física (III derivada).</p>
</div>

2. Ploteo de señales en un electrocardiograma utilizando la librería https://pypi.org/project/ecg-plot/

  #### Reposo

<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoECG1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 18:</strong> Ploteo de señal de reposo en Electrocardiograma (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoECG2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 19:</strong>  Ploteo de señal de reposo en Electrocardiograma (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ReposoECG3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 20:</strong>  Ploteo de señal de reposo en Electrocardiograma (III derivada).</p>
</div>

  #### Inhalación 1
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionECG1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 21:</strong> Ploteo de señal de primera inhalación en Electrocardiograma  (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionECG2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 22:</strong> Ploteo de señal de primera inhalación en Electrocardiograma (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/InhalacionECG3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 23:</strong> Ploteo de señal de primera inhalación en Electrocardiograma (III derivada).</p>
</div>

  #### Actividad física
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaECG1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 24:</strong> Ploteo de señal de actividad física en Electrocardiograma (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaECG2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 25:</strong> Ploteo de señal de actividad física en Electrocardiograma (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaECG3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 26:</strong> Ploteo de señal de actividad física en Electrocardiograma (III derivada).</p>
</div>

  #### Post- actividad física
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2ECG1raDeriv.jpg" alt="Posición de electrodos" width="60%">
  <p><strong>Figura 27:</strong> Ploteo de señal post-actividad física en Electrocardiograma (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2ECG2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 28:</strong> Ploteo de señal post-actividad física en Electrocardiograma (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/Inhalacion2ECG3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 29:</strong> Ploteo de señal post-actividad física en Electrocardiograma (III derivada).</p>
</div>

  #### Análisis de las gráficas obtenidas



## 5. Referencias <a name="referencias"></a>

[1] Mayo Clinic, “Electrocardiograma (ECG)”. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983. [Accedido: 24-abr-2025].

[2] “12 Lead ECG Placement Guide with Illustrations,” *Cables & Sensors*. [En línea]. Disponible en: https://www.cablesandsensors.eu/pages/12-lead-ecg-placement-guide-with-illustrations. [Accedido: 24-abr-2025].

[3] H. E. Inkley, Introduction to Biomedical Engineering, 4th ed., Elsevier, 2020
[4] BITalino documentation. https://bitalino.com/en/software
