# Laboratorio 12: Avance del proyecto
# Evaluación electromiográfica de la fatiga muscular del miembro superior durante el uso del smartphone: Un estudio comparativo entre jóvenes usuarios intensivos y ocasionales

link del paper: https://docs.google.com/document/d/1Fk9rCmvZFyv1IQMk603ACRcE4HknOFrcELzjUgmIeEs/edit?usp=sharing

## Objetivo del proyecto: 
Analizar y comparar la actividad electromiográfica de músculos específicos de la extremidad superior durante el uso del smartphone, entre jóvenes con uso intensivo y ocasional del dispositivo, identificando signos de fatiga y su relación con la puntuación en la escala SAS-SV.

## Protocolo para obtención de datos electromiográficos

El rango de edad de quiénes se obtendrá los datos debe variar de entre 18 a 24 años. Para este proyecto se estará trabajando con 4 participantes.

* Criterios de inclusión:
  - Uso regular de smartphone (mínimo 1 hora diaria).
  - Sin lesiones musculoesqueléticas en extremidad superior.

* Criterios de exclusión:
  - Cirugías recientes
  - Enfermedades neuromusculares o trastornos posturales diagnosticados.

### Materiales y metodología
  * Dispositivo BITalino (4 canales sEMG).
  * Electrodos de superficie autoadhesivos.
  * Smartphone propio del participante (uso natural).
  * Software de registro: OpenSignals, MATLAB o Python.
  * Aplicación de la transformada wavelet discreta (DWT)

  **Músculos evaluados**
  * Extensor radial largo del carpo – estabiliza muñeca en agarre.
  * Flexor superficial de los dedos – activa durante scroll y tipeo.

  
  **Tareas experimentales**
  Para cada sesión, se realizarán las mediciones con BITalino en los últimos 2 minutos.
  En reposo, el paciente se mantendrá en la misma postura sin utilizar el smartphone.
  * Sesión de reposo: 2 minutos (2 minutos se toman las medidas con BITalino)

  En las sesiones de uso del smartphone, se pide realizar acciones como scrollear, chatear o jugar. 
  * Sesión de uso moderado: 3 a 6 minutos (6 a 8 minutos se toman las medidas con BITalino)
  * Sesión de uso intensivo: 8 a 24 minutos (24 a 26 minutos se toman las medidas con BITalino)

## Resultados obtenidos

Para filtrar nuestras señales EMG, utilizamos los parámetros y metodología propuestos en la literatura encontrada para mejorar la relación entre eliminación de ruido y preservación de señal útil [1].  
Específicamente, se aplicó una descomposición por wavelet discreta (DWT) utilizando la función madre Symlet 4 (`sym4`), con un nivel de descomposición de 10. A cada conjunto de coeficientes de detalle se le aplicó un umbral adaptativo por nivel (λⱼ), seguido de una función de umbralización mejorada, la cual incorpora los parámetros de ajuste μ = 0.91 y δ = 0.01.  
| Familia de funciones Wavelet | Nivel | Threshold utilizado                         | Tipo de Threshold           | Coeficiente de Aproximación | Coeficientes de Detalle                                                       |
|------------------------------|--------|----------------------------------------------|------------------------------|------------------------------|--------------------------------------------------------------------------------|
| Symlet 4 (`sym4`)            | 10     | Umbral adaptativo por nivel (`λ_j`)          | Función mejorada  | A10                         | D1, D2, D3, D4, D5, D6, D7, D8, D9, D10 (cada uno umbralizado con `f_i(x, λ_j)`) |

### Extensor:
- Persona 1:
 <img src="./Imagenes en el anexo/Wen_reposo_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Wen_moderado_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Wen_intenso_extensor.png" width="800"/>
 
- Persona 2:
 <img src="./Imagenes en el anexo/Ecos_reposo_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Ecos_moderado_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Ecos_intenso_extensor.png" width="800"/>

 - Persona 3:
 <img src="./Imagenes en el anexo/Gaby_reposo_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Gaby_moderado_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Gaby_intenso_extensor.png" width="800"/>

 - Persona 4:
 <img src="./Imagenes en el anexo/Aaron_reposo_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Aaron_moderado_extensor.png" width="800"/>
 <img src="./Imagenes en el anexo/Aaron_intenso_extensor.png" width="800"/>
 
### Flexor:
- Persona 1:
 <img src="./Imagenes en el anexo/Wen_reposo_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Wen_moderado_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Wen_intenso_flexor.png" width="800"/>
 
- Persona 2:
 <img src="./Imagenes en el anexo/Ecos_reposo_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Ecos_moderado_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Ecos_intenso_flexor.png" width="800"/>

 - Persona 3:
 <img src="./Imagenes en el anexo/Gaby_reposo_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Gaby_moderado_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Gaby_intenso_flexor.png" width="800"/>

 - Persona 4:
 <img src="./Imagenes en el anexo/Aaron_reposo_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Aaron_moderado_flexor.png" width="800"/>
 <img src="./Imagenes en el anexo/Aaron_intenso_flexor.png" width="800"/>

## Resultados del test SAS-SV

| Participante | Sexo    | Puntaje SAS-SV | Clasificación         |
|--------------|---------|----------------|------------------------|
| Gaby         | Mujer   | 37             | Usuario intensivo     |
| Wen          | Mujer   | 35             | Usuario intensivo     |
| Alejandro    | Hombre  | 26             | Usuario ocasional     |
| Aaron        | Hombre  | 24             | Usuario ocasional     |


Con base en los puntajes obtenidos en la escala Smartphone Addiction Scale - Short Version (SAS-SV) y el análisis visual de la actividad electromiográfica (EMG), se clasificó a los participantes en dos grupos:
- Usuarios intensivos: Gaby y Wen
- Usuarios ocasionales: Alejandro y Aaron

Las participantes clasificadas como usuarias intensivas superaron el umbral de 31 puntos establecido para mujeres, mientras que los varones estuvieron por debajo del umbral de 33 puntos, confirmando su clasificación como usuarios ocasionales. Esta categorización se corresponde con los patrones de activación muscular observados en las señales EMG, donde Gaby y Wen presentaron mayor frecuencia y amplitud de contracciones, especialmente en el flexor superficial de los dedos, durante las sesiones prolongadas de uso del smartphone.

## Discusión y próximos pasos
Los resultados obtenidos revelan diferencias en la actividad muscular entre usuarios intensivos y ocasionales, especialmente en el músculo flexor superficial de los dedos, mientras que en el extensor radial largo del carpo las diferencias fueron menos marcadas.

En las señales EMG procesadas mediante descomposición wavelet discreta (sym4, nivel 10) y umbralización mejorada, se observó que en los usuarios intensivos (Gaby y Wen) el flexor superficial de los dedos presentó mayor cantidad de activaciones, amplitudes más altas y una distribución más densa de eventos durante las sesiones de uso prolongado. Esto refleja un mayor esfuerzo muscular asociado a acciones como el tipeo y el desplazamiento táctil continuo, actividades típicas en el uso del smartphone.

En contraste, la señal registrada en el extensor radial largo del carpo, responsable principalmente de estabilizar la muñeca, mostró patrones similares entre usuarios intensivos y ocasionales. Si bien se registraron activaciones, estas no evidenciaron un incremento sustancial con el aumento de la duración del uso, lo que sugiere que el esfuerzo postural requerido para mantener el agarre del dispositivo puede mantenerse relativamente constante entre los distintos grupos.

Este hallazgo es relevante, ya que sugiere que el movimiento repetitivo de los dedos es un factor más determinante en la aparición de signos de fatiga muscular durante el uso del smartphone, en comparación con la carga postural mantenida de la muñeca. Así, el flexor superficial de los dedos se posiciona como un músculo clave para la evaluación temprana de sobreuso en este contexto.

Finalmente, la metodología empleada no solo facilitó la limpieza del ruido y la mejora de la señal, sino que sentó las bases para un análisis cuantitativo más preciso con métricas como RMS y frecuencia mediana, que serán abordadas en la siguiente fase del estudio.

## Referencias
[1]  Y. Ouyang, Z. Deng, Y. Yin, X. Wu, y Z. Chen, "An improved wavelet threshold denoising approach for surface electromyography signal," EURASIP Journal on Advances in Signal Processing, vol. 2023, no. 1, p. 10, Jan. 2023. https://doi.org/10.1186/s13634-023-01066-3
