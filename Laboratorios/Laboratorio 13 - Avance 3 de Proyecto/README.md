# Evaluación electromiográfica de la fatiga muscular del miembro superior durante el uso del smartphone  
**Enlace al proyecto:** https://docs.google.com/document/d/1Fk9rCmvZFyv1IQMk603ACRcE4HknOFrcELzjUgmIeEs/edit?usp=sharing

---

## Objetivo  
Comparar la actividad electromiográfica de músculos seleccionados del antebrazo en jóvenes con uso intensivo y ocasional del smartphone, identificando indicadores de fatiga y su relación con la puntuación en la escala SAS-SV.

---

## Protocolo de obtención de datos  

- **Participantes:** 4 jóvenes, 18–24 años  
- **Criterios de inclusión:**  
  - Uso de smartphone ≥ 1 h/día  
  - Ausencia de lesiones musculoesqueléticas en extremidad superior  
- **Criterios de exclusión:**  
  - Cirugías recientes  
  - Enfermedades neuromusculares o trastornos posturales  

### Materiales y métodos  
- **Dispositivo:** BITalino (4 canales sEMG)  
- **Electrodos:** Superficie autoadhesivos  
- **Smartphone:** Propio del participante, uso natural  
- **Software:** OpenSignals, MATLAB o Python  
- **Procesamiento:** DWT (Symlet 4, nivel 10) con umbralización adaptativa (μ = 0.91, δ = 0.01)  

#### Músculos evaluados  
- **Extensor radial largo del carpo** (estabilización de la muñeca)  
- **Flexor superficial de los dedos** (scroll y tipeo)  

#### Tareas  
1. **Reposo:** 2 minutos de registro sin interacción  
2. **Uso moderado:** 6 minutos registrando scroll y chat  
3. **Uso intensivo:** 24 minutos registrando juego y videos  

---

## Resultados
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

 
### Análisis estadístico

#### Extensor radial largo del carpo  
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

**Interpretación:** La activación del extensor se mantiene estable entre las tres condiciones (todos p > 0.05), lo que respalda su rol de soporte sin cambios relevantes ante distintas intensidades de uso.

---

#### Flexor superficial de los dedos  
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

**Interpretación:** El flexor aumenta su amplitud (RMS, MAV), complejidad (WL, SSC, WAMP) y contenido frecuencial (MNF, MDF) con la intensidad, evidenciando un reclutamiento y dinámica crecientes (p < 0.05 en 8/9 features).

---

### Clasificación por RMS medio  
| Sujeto   | Moderado | Intenso  | avg_MI   | Grupo          |
|:---------|:---------|:---------|:---------|:---------------|
| Sujeto2  | 0.01103  | 0.00622  | 0.00862  | Uso Regular    |
| Sujeto3  | 0.01262  | 0.01666  | 0.01464  | Uso Regular    |
| Sujeto4  | 0.01395  | 0.01896  | 0.01646  | Uso Ocasional  |
| Sujeto1  | 0.01609  | 0.02297  | 0.01953  | Uso Ocasional  |

 **Criterio:**  
 - **Uso regular:** menor avg_MI → mejor adaptación y menor fatiga.
 - - **Uso ocasional:** mayor avg_MI → mayor fatiga.

---

### Resultados SAS-SV  
| Participante | Sexo   | Puntaje SAS-SV | Clasificación    |
|:-------------|:-------|:---------------|:-----------------|
| Sujeto4      | Mujer  | 26             | Ocasional        |
| Sujeto1      | Mujer  | 24             | Ocasional        |
| Sujeto2      | Hombre | 37             | Intensivo        |
| Sujeto3      | Hombre | 36             | Intensivo        |

> **Umbrales:** ≥ 31 para mujeres, ≥ 33 para hombres.

---

## Discusión

1. **Concordancia entre EMG y SAS-SV:**  
   - Sujetos clasificados como intensivos en SAS-SV (Sujeto2, Sujeto3) coinciden con los de mayor avg_MI (mayor fatiga EMG).  
   - Sujetos ocasionales (Sujeto4, Sujeto1) presentan avg_MI más bajo y menor reclutamiento muscular.

2. **RMS medio como marcador de fatiga:**  
   - Refleja la adaptación muscular; valores bajos indican menor riesgo de sobrecarga.

3. **Diferencias músculo‐dependientes:**  
   - El extensor permanece estable (función de soporte).  
   - El flexor responde a la demanda con mayores amplitud y dinamismo.

4. **Implicaciones ergonómicas:**  
   - El uso prolongado sobrecarga los flexores, potencialmente derivando en lesiones por sobreuso.  
   - Recomendaciones: pausas activas y ejercicios de fortalecimiento, especialmente para usuarios intensivos.

5. **Limitaciones y perspectivas:**  
   - Tamaño muestral reducido (n = 4).  
   - Falta de medidas subjetivas de fatiga y recuperación.  
   - Futuras investigaciones: más participantes, evaluación de otros músculos y técnicas de recuperación.

**Conclusión:** El uso intensivo del smartphone incrementa significativamente la actividad y fatiga de los flexores, acorde con la clasificación SAS-SV. El extensor se mantiene estable. El RMS medio en condiciones de esfuerzo es un indicador robusto para diferenciar grupos de usuarios y diseñar intervenciones ergonómicas personalizadas.

## Referencias
[1]  Y. Ouyang, Z. Deng, Y. Yin, X. Wu, y Z. Chen, "An improved wavelet threshold denoising approach for surface electromyography signal," EURASIP Journal on Advances in Signal Processing, vol. 2023, no. 1, p. 10, Jan. 2023. https://doi.org/10.1186/s13634-023-01066-3

