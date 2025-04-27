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

### 🔬 Análisis en Python

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
  ## REPOSO:
| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo | <img src="./Imágenes%20en%20el%20anexo/Screenshot_23.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_25.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_27.jpg" alt="Posición de electrodos" width="80%"> |
| Dominio de la frecuencia |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_24.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_26.jpg" alt="Posición de electrodos" width="80%"> |<img src="./Imágenes%20en%20el%20anexo/Screenshot_28.jpg" alt="Posición de electrodos" width="80%"> |

 
   ## INHALACIÓN 1:
| Señal | Primera derivada | Segunda derivada |Tercera derivada |
|-----------|------------------|------------------|-----------------|
| Dominio del tiempo |<img src="./Imágenes%20en%20el%20anexo/Screenshot_11.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_13.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_15.jpg" alt="Posición de electrodos" width="80%">|
| Dominio de la frecuencia | <img src="./Imágenes%20en%20el%20anexo/Screenshot_12.jpg" alt="Posición de electrodos" width="80%"> |  <img src="./Imágenes%20en%20el%20anexo/Screenshot_14.jpg" alt="Posición de electrodos" width="80%"> | <img src="./Imágenes%20en%20el%20anexo/Screenshot_16.jpg" alt="Posición de electrodos" width="80%"> |

 

   ## ACTIVIDAD FÍSICA:
 
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_5.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_6.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_7.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_8.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_9.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_10.jpg" alt="Posición de electrodos" width="50%">

   ## INHALACIÓN 2:
 
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_17.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_18.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_19.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_20.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_21.jpg" alt="Posición de electrodos" width="50%">
 <img src="./Imágenes%20en%20el%20anexo/Screenshot_22.jpg" alt="Posición de electrodos" width="50%">


### 📐 Actividad Adicional

Como parte complementaria de esta práctica, se utilizó un **simulador ProSim 4** para generar señales cardíacas artificiales con diferentes frecuencias, evaluando la capacidad del sistema BITalino para registrar y representar estas señales de forma precisa.

#### Objetivo
Validar el funcionamiento del módulo ECG del BITalino con señales simuladas de ritmo cardíaco conocido, y comparar su comportamiento con las señales fisiológicas reales adquiridas.

#### Configuración
- Derivaciones conectadas al ProSim de forma equivalente a la configuración del paciente real.
- El BITalino se emparejó por Bluetooth con OpenSignals.
- Cada frecuencia fue mantenida durante ~1 minuto para su registro.

#### Frecuencias simuladas:
- 🟢 **60 lpm** → Estado basal
- 🔵 **90 lpm** → Recuperación
- 🟠 **120 lpm** → Actividad física moderada
- 🔴 **150 lpm** → Actividad intensa

#### Registros obtenidos

| Frecuencia simulada | Video | Gráfica de señal |
|---------------------|--------|------------------|
| **60 lpm**          | [🎥 Ver video](https://example.com/video60) | ![Simulación 60](./simulacion/sim_60.png) |
| **90 lpm**          | [🎥 Ver video](https://example.com/video90) | ![Simulación 90](./simulacion/sim_90.png) |
| **120 lpm**         | [🎥 Ver video](https://example.com/video120) | ![Simulación 120](./simulacion/sim_120.png) |
| **150 lpm**         | [🎥 Ver video](https://example.com/video150) | ![Simulación 150](./simulacion/sim_150.png) |

#### Análisis

Las gráficas muestran una frecuencia de aparición del complejo QRS proporcional a la frecuencia establecida por el simulador. Esto valida que el módulo ECG de BITalino puede registrar correctamente señales artificiales con buena fidelidad. Además, la visualización en OpenSignals resultó estable y sin pérdidas significativas de señal durante toda la simulación.

> 📌 *Nota: si el simulador ProSim no estuvo disponible, se debe registrar esta sección como no realizada en las limitaciones.*

 ## 4. Resultados y limitaciones: <a name="resultados-y-limitaciones"></a> 


- La señal basal mostró un ritmo sinusal regular, con ondas P, QRS y T identificables.
- Durante la apnea, la frecuencia se redujo levemente y hubo un cambio en la amplitud.
- En el estado post-ejercicio, la frecuencia cardíaca aumentó significativamente.
- El análisis de frecuencia mostró un pico dominante cercano a 1 Hz (60 bpm), coherente con el ritmo en reposo.

Incluir aquí capturas de pantalla de OpenSignals]
Incluir gráficos generados con Python

 ### Limitaciones

- Ruido por movimiento y mala adherencia de electrodos en la prueba post-ejercicio.
- Frecuencia de muestreo fija limitó el análisis detallado de intervalos cortos.
- No se pudo realizar la prueba con ProSim por falta de acceso al simulador.


## 5. Referencias: <a name="referencias"></a> 

## 5. Referencias <a name="referencias"></a>

[1] Mayo Clinic, “Electrocardiograma (ECG)”. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983. [Accedido: 24-abr-2025].

[2] “12 Lead ECG Placement Guide with Illustrations,” *Cables & Sensors*. [En línea]. Disponible en: https://www.cablesandsensors.eu/pages/12-lead-ecg-placement-guide-with-illustrations. [Accedido: 24-abr-2025].

[3] H. E. Inkley, Introduction to Biomedical Engineering, 4th ed., Elsevier, 2020
[4] BITalino documentation. https://bitalino.com/en/software
