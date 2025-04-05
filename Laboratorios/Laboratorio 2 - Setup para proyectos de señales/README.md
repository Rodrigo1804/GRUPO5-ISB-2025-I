# Anexo: Titulo..

## ¿Cómo crear un entorno virtual?

### 1. Desde el entorno virtual de Python
![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/FIG1.png)
1. Abrir el terminal (cmd) y ubica la ruta donde guardarás tu entorno virtual.
2. Este comando nos permite crear un entorno virtual: `python -m venv Nombre`
3. Activar el entorno virtual con: `Nombre\Scripts\activate`
4. Verificar las librerías instaladas con:  `pip list`
5. Para poder instalar las librerias necesarias para el laboratorio en el entorno virtual se usa el siguiente comando: `pip install neurokit2 matplotlib numpy pandas`

### 2. Desde anaconda
![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/Captura1.PNG)

1. Crear un entorno virtual desde el Anaconda prompt, es recomendable ejecutarlo como administrador antes de crear el entorno en el prompt. El entorno se crea con el siguiente código:

``` 
   conda create -n mi_entorno python=3.9 numpy pandas matplotlib 
   ``` 

![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/Captura5.PNG)

 2. Se activa el entorno con el siguiente código:
   
   ``` 
   conda activate mi_entorno
   ```  

![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/Captura6.PNG)

  3. Se instalan más paquetes en el entorno con:
   
   ``` 
   conda install scikit-learn
   ```  

![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/Captura7.PNG)

  4. Se desactiva el entorno con:
   
   ``` 
   conda deactivate
   ```




## Ploteo de señales ECG y EMG
Todos los códigos se ejecutaron desde el terminal CMD con el siguiente comando: `python nombre.py`
## 1. ECG
### Ploteo de la señal ECG en el dominio del tiempo
- Código en python:
<img src="./Imágenes en el Anexo/CodigoECG.png" alt="Código ECG" width="600">

``` 
   import neurokit2 as nk
   import pandas as pd
   import matplotlib.pyplot as plt
   import numpy as np
   ```
En esta primera sección, se importan las librerías de uso para el ploteo de las señales. Por ejemplo, neurokit2 se usa para la simulación de señales fisiológicas como ECG.

``` 
 duration = 10
 sampling_rate = 1000
 tiempo = np.linspace(0, duration, duration * sampling_rate)
```
En esta segunda sección, se define la duración de las señales en segundos, la frecuencia de sampleo y el vector de tiempo para el ploteo de las señales.

``` 
ecg_simple_80 = nk.ecg_simulate(duration=duration, heart_rate=80, method="simple")
ecg_simple_120 = nk.ecg_simulate(duration=duration, heart_rate=120, method="simple")
ecg_complex_80 = nk.ecg_simulate(duration=duration, heart_rate=80, method="ecgsyn")
ecg_complex_120 = nk.ecg_simulate(duration=duration, heart_rate=120, method="ecgsyn")

```
En esta tercera sección, se define la duración de la señal como el vector de tiempo que se había creado previamente, la frecuencia cardíaca de la señal y el modelo con el que se generará la señal. En este caso se usa simple y ecgsyn que es más complejo y realista.

``` 
ecg_df = pd.DataFrame({
    "ECG_Simple_80bpm": ecg_simple_80,
    "ECG_Simple_120bpm": ecg_simple_120,
    "ECG_Complex_80bpm": ecg_complex_80,
    "ECG_Complex_120bpm": ecg_complex_120
}, index=tiempo)

```
Ahora, se crea un dataframe para adjuntar las señales y presentarlas mejor en el ploteo.

``` 
# Graficar
nk.signal_plot(ecg_df, subplots=True)
plt.suptitle("Comparación de Señales ECG Simuladas (Dominio del Tiempo)", fontsize=16)
plt.xlabel("Tiempo (s)")
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Para organizar cada gráfica con sus etiquetas.
plt.show()

```
Finalmente, se plotean todas señales con sus respectivas etiquetas en X y Y






- Resultado:
<img src="./Imágenes en el Anexo/ECG.png" alt="Gráfica ECG" width="800">

### Ploteo de la señal EMG en el dominio de la frecuencia
- Código en python:
<img src="./Imágenes en el Anexo/CodigoECGft.png" alt="Código ECGft" width="600">

En el dominio de la frecuencia, las secciones de importación de librerías y creación del vector de tiempo es igual. Donde es diferente es en la creación del vector de frequencias a partir del vector de tiempo y la obtención de las transformada de fourier de cada señal.

``` 
frequencies = np.fft.fftfreq(len(tiempo), d=1/sampling_rate)

fft_simple_80 = np.abs(np.fft.fft(ecg_simple_80))  
fft_simple_120 = np.abs(np.fft.fft(ecg_simple_120))  
fft_complex_80 = np.abs(np.fft.fft(ecg_complex_80))  
fft_complex_120 = np.abs(np.fft.fft(ecg_complex_120))

```

El resto de secciones es igual. Solo se debe respetar el uso de `frequencies` como el index del df para el ploteo y en y el uso de las variables fft.



- Resultado:
<img src="./Imágenes en el Anexo/ECGft.png" alt="Gráfica ECGft" width="800">

## 2. EMG
### Ploteo de la señal EMG en el dominio del tiempo
- Código en python:
<img src="./Imágenes en el Anexo/CodigoEMG.png" alt="Código EMG" width="600">

En esta primera sección, se importan las librerías necesarias. neurokit2 se usa para la simulación de señales fisiológicas como EMG (electromiograma), mientras que pandas, matplotlib y numpy ayudan con el manejo de datos y la visualización.

``` 
   import neurokit2 as nk
   import pandas as pd
   import matplotlib.pyplot as plt
   import numpy as np
   ```

En esta segunda sección, se define la duración de la señal en segundos, la frecuencia de muestreo (sampling_rate), y se genera un vector de tiempo uniforme utilizando linspace.

``` 
  duration = 10  
  sampling_rate = 1000  
  tiempo = np.linspace(0, duration, duration * sampling_rate)
   ```
En esta sección se generan cuatro señales EMG con diferentes características. `burst_number` controla cuántos estallidos (ráfagas musculares) tiene cada señal, mientras que `burst_duration` define la duración de cada estallido. Estas variaciones permiten estudiar cómo cambia la señal con distintos niveles de actividad muscular.

```
emg3 = nk.emg_simulate(duration=duration, burst_number=3, burst_duration=1.0)  
emg4_long = nk.emg_simulate(duration=duration, burst_number=4, burst_duration=1.5)  
emg5 = nk.emg_simulate(duration=duration, burst_number=5, burst_duration=1.0)  
emg6_short = nk.emg_simulate(duration=duration, burst_number=6, burst_duration=0.5) 
```

Ahora se organiza la información generada en un `DataFrame` de pandas, usando el vector de tiempo como índice. Cada columna representa una señal EMG distinta. Esto facilita la visualización y posterior análisis comparativo.
```
emg_df = pd.DataFrame({  
    "EMG_3bursts": emg3,  
    "EMG_4bursts_long": emg4_long,  
    "EMG_5bursts": emg5,  
    "EMG_6bursts_short": emg6_short  
}, index=tiempo)  
```
Finalmente, se grafican las señales EMG utilizando signal_plot, con una subgráfica para cada señal. Se agrega un título general, se etiqueta el eje X como tiempo y se ajusta el diseño de las gráficas para una mejor presentación.
```
nk.signal_plot(emg_df, subplots=True)  
plt.suptitle("Comparación de Señales EMG Simuladas (Dominio del Tiempo)", fontsize=16)  
plt.xlabel("Tiempo (s)")  
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Para organizar cada gráfica con sus etiquetas.  
plt.show()  
```







- Resultado:
<img src="./Imágenes en el Anexo/EMG.png" alt="Gráfica EMG" width="800">

### Ploteo de la señal EMG en el dominio de la frecuencia
- Código en python:
<img src="./Imágenes en el Anexo/CodigoEMGft.png" alt="Código EMGft" width="600">

En este caso, todo las seccións anteriores en códigos es igual a excepción de que ahora agregamos, como en el caso de ECG, la creación de un vector de frecuencias y la generación de las fft de cada señal.
```

```

- Resultado:
<img src="./Imágenes en el Anexo/EMGft.png" alt="Gráfica EMGft" width="800">




