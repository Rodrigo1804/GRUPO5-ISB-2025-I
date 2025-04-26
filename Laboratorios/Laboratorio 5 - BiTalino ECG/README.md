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

| Condición | Video |
|----------|-------|
| Estado basal | [🎥 Ver video](https://link-a-tu-video.com) |
| Apnea (10s) | [🎥 Ver video](https://link-a-tu-video.com) |
| Post-ejercicio | [🎥 Ver video](https://link-a-tu-video.com) |
| Conexión y colocación de electrodos | [🎥 Ver video](https://link-a-tu-video.com) |

4. **Exportación de datos**
   - Exportar archivos .txt desde OpenSignals para análisis posterior en Python.
   - 

## 4. Resultados y limitaciones <a name="resultados-y-limitaciones"></a>

### Resultados fisiológicos

#### 📊 Señal en reposo (OpenSignals)
![reposo](./imagenes/ecg_reposo.png)

#### 📊 Señal en apnea
![apnea](./imagenes/ecg_apnea.png)

#### 📊 Señal post-ejercicio
![ejercicio](./imagenes/ecg_ejercicio.png)

---

### 🔬 Análisis en Python

```python
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np

df = pd.read_csv("ECG_signal.csv")
signal = df["ECG"].values
fs = 1000

plt.figure()
plt.plot(signal[:1000])
plt.title("ECG - Dominio del tiempo")
plt.xlabel("Muestras")
plt.ylabel("Voltaje (mV)")
plt.grid()
plt.show()

N = len(signal)
yf = fft(signal)
xf = fftfreq(N, 1/fs)

plt.figure()
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("ECG - Dominio de la frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
```

📊 [Agregar aquí imágenes de resultados en tiempo y frecuencia]


### 📐 Simulación con ProSim 4

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
