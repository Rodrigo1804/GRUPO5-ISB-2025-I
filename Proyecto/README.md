
# Evaluación electromiográfica de la fatiga muscular del miembro superior durante el uso del smartphone: Un estudio comparativo entre jóvenes usuarios intensivos y ocasionales

enlace hacia el paper: https://docs.google.com/document/d/1Fk9rCmvZFyv1IQMk603ACRcE4HknOFrcELzjUgmIeEs/edit?usp=sharing

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
## Resultados

### Resultados Estadísticos

#### Músculo Extensor  
| Feature   | Prueba    | Estadístico | p-valor | Significancia            |
|:----------|:----------|:------------|:--------|:-------------------------|
| **RMS**   | Friedman  | χ² = 6.000  | 0.050   | No significativa (límite)|
| **MAV**   | Friedman  | χ² = 4.500  | 0.105   | No significativa         |
| **WL**    | Friedman  | χ² = 2.000  | 0.368   | No significativa         |
| **ZC**    | ANOVA     | F = 1.997   | 0.192   | No significativa         |
| **SSC**   | ANOVA     | F = 2.876   | 0.108   | No significativa         |
| **WAMP**  | Friedman  | χ² = 2.000  | 0.368   | No significativa         |
| **MNF**   | Friedman  | χ² = 2.000  | 0.368   | No significativa         |
| **MDF**   | Friedman  | χ² = 2.000  | 0.368   | No significativa         |
| **Power** | Friedman  | χ² = 2.000  | 0.368   | No significativa         |

> **Interpretación:** La activación del extensor radial largo del carpo se mantiene estable en Reposo, Moderado e Intenso (todos p > 0.05), lo que sugiere que su función de estabilización no varía con la carga del smartphone.

---

#### Músculo Flexor  
| Feature   | Prueba    | Estadístico | p-valor  | Significancia        |
|:----------|:----------|:------------|:---------|:---------------------|
| **RMS**   | ANOVA     | F = 13.568  | 0.002    | Significativa        |
| **MAV**   | ANOVA     | F = 11.850  | 0.003    | Significativa        |
| **WL**    | ANOVA     | F = 9.079   | 0.007    | Significativa        |
| **ZC**    | Friedman  | χ² = 6.500  | 0.039    | Significativa        |
| **SSC**   | ANOVA     | F = 27.515  | < 0.001  | Significativa        |
| **WAMP**  | ANOVA     | F = 18.686  | 0.001    | Significativa        |
| **MNF**   | Friedman  | χ² = 6.500  | 0.039    | Significativa        |
| **MDF**   | Friedman  | χ² = 6.500  | 0.039    | Significativa        |
| **Power** | ANOVA     | F = 3.983   | 0.058    | Tendencia (p ≈ 0.06) |

> **Interpretación:** El flexor superficial de los dedos incrementa su amplitud (RMS, MAV), complejidad (WL, SSC, WAMP) y contenido de frecuencia (MNF, MDF) con la intensidad del uso, confirmando un mayor reclutamiento y dinamismo de contracciones (p < 0.05 en 8 de 9 features).

---

### Clasificación por RMS Medio  
| Sujeto   | Reposo   | Moderado | Intenso  | avg_MI   | Grupo          |
|:---------|:---------|:---------|:---------|:---------|:---------------|
| Sujeto2  | 0.00179  | 0.01103  | 0.00622  | 0.00862  | Uso Regular    |
| Sujeto3  | 0.00233  | 0.01262  | 0.01666  | 0.01464  | Uso Regular    |
| Sujeto4  | 0.00033  | 0.01395  | 0.01896  | 0.01646  | Uso Ocasional  |
| Sujeto1  | 0.00007  | 0.01609  | 0.02297  | 0.01953  | Uso Ocasional  |

> **Criterio:**  
> - **Uso Regular:** menor avg_MI → mejor adaptación y menor fatiga (Sujeto2, Sujeto3).  
> - **Uso Ocasional:** mayor avg_MI → mayor fatiga (Sujeto4, Sujeto1).

---

### Resultados SAS-SV  
| Participante | Sexo   | Puntaje SAS-SV | Clasificación      |
|:-------------|:-------|:---------------|:-------------------|
| Sujeto4        | Mujer  | 26             | Ocasional          |
| Sujeto1          | Mujer  | 24             | Ocasional          |
| Sujeto2    | Hombre | 37             | Intensivo          |
| Sujeto3       | Hombre | 36             | Intensivo          |

> **Umbrales:** ≥ 31 para mujeres, ≥ 33 para hombres.  

---

## Discusión

1. **Análisis estadístico vs. SAS-SV:**  
   - Los participantes clasificados como **intensivos** en SAS-SV (Alejandro, Aaron) coinciden con los sujetos de mayor avg_MI (Sujeto1, Sujeto4), confirmando mayor fatiga electromiográfica.  
   - Los **ocasionales** (Gaby, Wen) muestran avg_MI más bajo (Sujeto2, Sujeto3), reflejando menor reclutamiento muscular.

2. **RMS como indicador de fatiga:**  
   - El RMS promedio en Moderado e Intenso se revela como un marcador confiable de adaptación muscular. Sujetos con RMS menor mantienen estabilidad en activación y menor riesgo de sobrecarga.

3. **Diferencias músculo-específicas:**  
   - **Extensor:** estable, cumple función de soporte sin cambios significativos.  
   - **Flexor:** sensible a la demanda, con aumentos progresivos en amplitud y dinamismo de la señal.

4. **Implicaciones ergonómicas y clínicas:**  
   - La sobrecarga repetitiva de los flexores puede causar fatiga y lesión por uso excesivo.  
   - Intervenciones como pausas activas o ejercicios de fortalecimiento deben enfocarse en usuarios con alto avg_MI/SAS-SV.

5. **Limitaciones y recomendaciones:**  
   - Muestra pequeña (n = 4).  
   - Faltan medidas subjetivas de fatiga y recuperación.  
   - Futuras investigaciones deben incluir más participantes y evaluar otros grupos musculares y técnicas de recuperación.

> **Conclusión:** El uso intensivo del smartphone se traduce en un reclutamiento significativo de los flexores (elevación de RMS y otras features), correlacionado con la clasificación SAS-SV. Los extensores permanecen estables. RMS medio en condiciones de esfuerzo es un buen discriminador entre usuarios regulares y ocasionales, útil para diseñar estrategias ergonómicas personalizadas.

## Referencias
[1]  Y. Ouyang, Z. Deng, Y. Yin, X. Wu, y Z. Chen, "An improved wavelet threshold denoising approach for surface electromyography signal," EURASIP Journal on Advances in Signal Processing, vol. 2023, no. 1, p. 10, Jan. 2023. https://doi.org/10.1186/s13634-023-01066-3
