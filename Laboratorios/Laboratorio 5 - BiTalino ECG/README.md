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
 
  ### INHALACIÓN 1:
| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo |<img src="./Imágenes%20en%20el%20anexo/Screenshot_11.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_13.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_15.jpg" alt="Posición de electrodos" width="80%">|
| Dominio de la frecuencia | <img src="./Imágenes%20en%20el%20anexo/Screenshot_12.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_14.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_16.jpg" alt="Posición de electrodos" width="80%"> |

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

#### Análisis en el dominio del tiempo

- Durante la condición de reposo, reflejan una actividad cardíaca regular y se puede identificar los latidos como picos definidos. Asimismo, los BPM calculados  están dentro del rango normal en reposo (60–100 BPM) [1]. 

- Durante la condición de inhalación , se puede notar que la frecuencia en ciertas zonas aumenta y entras disminuye y esto se debe a que ocurre un fenómeno fisiológico llamado arritmia sinusal respiratoria, donde la frecuencia cardiaca aumenta levemente al inhalar y disminuye al exhalar [6]. Asimismo, los BPM calculados están dentro del rango normal (60–100 BPM), considerando que no se ha realizado la activada física. 
 
- Durante la condición de actividad física, las señales de ECG registradas muestran un aumento evidente en la frecuencia de los latidos cardiacos. Este incremento corresponde a la respuesta fisiológica normal del sistema simpático ante el esfuerzo físico, que provoca taquicardia para satisfacer la demanda metabólica aumentada [8]. Asimismo, los BPM calculados son mayores a 100 y se considera normal porque se realizó una actividad física. 

- Durante la condición de inhalación después de las mediciones en la condición de actividad física, los BPM siguen siendo valores mayores a 100 lo que nos indica que la persona aún se esta recuperando de la actividad física y como en la primera medición de inhalación se puede observar el fenómeno arritmia sinusal respiratoria.

#### Análisis en el dominio de la frecuencia 

- En el análisis en el dominio de la frecuencia, se mantiene la concentración principal de energía entre 0.5 y 30 Hz, observándose un pico dominante cerca de 1 Hz, como se espera en condiciones fisiológicas normales. La atenuación progresiva de la energía a partir de 40 Hz refuerza la calidad de la adquisición de las señales, minimizando la interferencia de ruidos de alta frecuencia [7].

### Limitaciones

- Entre las principales limitaciones del presente experimento se encuentran la susceptibilidad a artefactos de movimiento y la posible contaminación por interferencia de red eléctrica. Además, la corta duración de las mediciones podría no capturar completamente fenómenos de variabilidad cardíaca de baja frecuencia.

- La colocación simplificada de electrodos también limita la representatividad espacial del ECG respecto a un estudio clínico completo, y la fatiga residual post-ejercicio puede afectar los resultados de recuperación.


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
  <p><strong>Figura 12:</strong> Datos del estado de actividad física procesado (I derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaProcesada2daDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 13:</strong> Datos del estado de actividad física procesado (II derivada).</p>
</div>
<div align="center">
  <img src="./Imágenes%20en%20el%20anexo/ActividadFisicaProcesada3raDeriv.jpg" alt="Derivaciones precordiales" width="60%">
  <p><strong>Figura 14:</strong> Datos del estado de actividad física procesado (III derivada).</p>
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
 #### Análisis de las gráficas
 Se puede observar que los BMP durante esl transcurso del tiempo para reposo e inhalación se encuentras dentro de rango normal entre 60-100 BPM y para actividad física mayor a 100 BPM
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

## 5. Referencias <a name="referencias"></a>

[1] Mayo Clinic, “Electrocardiograma (ECG)”. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983. [Accedido: 24-abr-2025].

[2] “12 Lead ECG Placement Guide with Illustrations,” *Cables & Sensors*. [En línea]. Disponible en: https://www.cablesandsensors.eu/pages/12-lead-ecg-placement-guide-with-illustrations. [Accedido: 24-abr-2025].

[3] H. E. Inkley, Introduction to Biomedical Engineering, 4th ed., Elsevier, 2020

[4] BITalino documentation. https://bitalino.com/en/software

[5] Mayo Clinic, "Heart rate: What's normal?", Mayo Clinic, 2021. [Online]. Available: https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979

[6] F. Shaffer, R. McCraty, and C. L. Zerr, "A healthy heart is not a metronome: An integrative review of the heart’s anatomy and heart rate variability," Frontiers in Public Health, vol. 9, p. 779956, 2021, doi: 10.3389/fpubh.2021.779956.

[7] M. González Aguilar, Diseño de un electrocardiógrafo para el estudio de señales ECG, Tesis de Grado, Universidad de Málaga, 2021.

[8] J. Naranjo-Orellana et al., "Cardiovascular response to exercise: Integrative physiology insights," Frontiers in Physiology, vol. 12, p. 667116, 2021, doi: 10.3389/fphys.2021.667116.
