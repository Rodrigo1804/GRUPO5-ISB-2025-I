# Anexo: Titulo..

## ¿Cómo crear un entorno virtual?

### 1. Desde el entorno virtual de Python
![FIG1 - Señal EMG](./Imágenes%20en%20el%20Anexo/FIG1.png)
1. Abrir el terminal (cmd) y ubica la ruta donde guardarás tu entorno virtual.
2. Este comando nos permite crear un entorno virtual: `python -m venv Nombre`
3. Activar el entorno virtual con: `Nombre\Scripts\activate`
4. Verificar las librerías instaladas con:  `pip list`
5. Para poder instalar las librerias necesarias para el laboratorio en el entorno virtual se usa el siguiente comando: `pip install neurokit2 matplotlib numpy pandas`

### 2. Desde anaconda??
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

- Resultado:
<img src="./Imágenes en el Anexo/ECG.png" alt="Gráfica ECG" width="800">

### Ploteo de la señal EMG en el dominio de la frecuencia
- Código en python:
<img src="./Imágenes en el Anexo/CodigoECGft.png" alt="Código ECGft" width="600">

- Resultado:
<img src="./Imágenes en el Anexo/ECGft.png" alt="Gráfica ECGft" width="800">

## 2. EMG
### Ploteo de la señal EMG en el dominio del tiempo
- Código en python:
<img src="./Imágenes en el Anexo/CodigoEMG.png" alt="Código EMG" width="600">

- Resultado:
<img src="./Imágenes en el Anexo/EMG.png" alt="Gráfica EMG" width="800">

### Ploteo de la señal EMG en el dominio de la frecuencia
- Código en python:
<img src="./Imágenes en el Anexo/CodigoEMGft.png" alt="Código EMGft" width="600">

- Resultado:
<img src="./Imágenes en el Anexo/EMGft.png" alt="Gráfica EMGft" width="800">




