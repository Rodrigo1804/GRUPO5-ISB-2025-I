# Laboratorio 6: Adquisición de señal EEG con BITalino

## Contenido:
1. [Introducción](#introducción)
2. [Propósito de la práctica](#propósito-de-la-práctica)  
3. [Materiales y metodología](#materiales-y-metodología)  
4. [Resultados y limitaciones](#resultados-y-limitaciones)  
5. [Referencias](#referencias)

## 1. Introducción <a name="introducción"></a>
La electroencefalografía (EEG) es una técnica no invasiva que permite registrar la actividad eléctrica del cerebro mediante electrodos colocados sobre el cuero cabelludo. Esta actividad refleja principalmente los potenciales postsinápticos generados por neuronas piramidales de la corteza cerebral, organizadas de manera paralela, lo que permite detectar oscilaciones neuronales a través de diferentes bandas de frecuencia (delta, theta, alfa, beta y gamma) [1].
<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/IMAGE1.png?raw=true" alt="Ilustración de bandas EEG" width="600"/>
  <p><em>Figura 1. Actividad cerebral</em></p>
</div>


## Bandas de frecuencia EEG

| Banda     | Rango (Hz)| Estado asociado                         | Ejemplos de tareas/estudios                    |
|-----------|------------|-----------------------------------------|------------------------------------------------|
| **Delta** | 0–4        | Sueño profundo, fases de descanso       | Estudios del sueño                             |
| **Theta** | 4–8        | Somnolencia, navegación espacial        | Prueba N-back, tareas de memoria espacial      |
| **Alpha** | 8–12       | Relajación con ojos cerrados            | Meditación, entrenamiento con biofeedback      |
| **Beta**  | 12–25      | Pensamiento activo, control motor       | Tareas de concentración, respuesta motora      |
| **Gamma** | >25        | Procesamiento visual, micro-movimientos | Estudios de microsacadas, resolución de problemas |

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/IMAGE2.png?raw=true" alt="Ilustración de bandas EEG" width="600"/>
  <p><em>Figura 2. Representación visual de las bandas de frecuencia en una señal EEG [2].</em></p>
</div>

### Tipos de medición y ubicación de los electrodos
La señal EEG puede adquirirse de forma monopolar (un electrodo activo respecto a una referencia común) o bipolar, que mide la diferencia entre dos electrodos activos más una referencia (El BITalino utiliza esta última). Por otro lado, una forma estandarizada de ubicar los electrodos en el cráneo humano es el sistema internacional **10-20**, que distribuye las posiciones según porcentajes del tamaño del cráneo y usa letras para identificar las regiones corticales [2]:
- **F (Frontal)**: funciones ejecutivas y atención (por ejemplo: F1, F2)
- **C (Central)**: área motora (por ejemplo: C3, C4)
- **P (Parietal)**: integración sensorial (por ejemplo: P3, P4)
- **O (Occipital)**: procesamiento visual (por ejemplo: O1, O2)
- **T (Temporal)**: audición, memoria y lenguaje (por ejemplo: T3, T4)
- **Z (Zero)**: línea media (por ejemplo: Fz, Cz, Pz)

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/IMAGE3.png?raw=true" alt="Ilustración de bandas EEG" width="600"/>
  <p><em>Figura 3. Vista superior de un cabezal con posicionamiento de electrodos según el sistema internacional 10-20 [2].</em></p>
</div>



## 2. Propósito de la práctica: <a name="propósito-de-la-práctica"></a>
El propósito de esta práctica es adquirir señales EEG utilizando el kit BITalino (r)evolution, registrando la actividad cerebral desde las posiciones Fp1, Fp2 y O2 del sistema 10-20. Se evaluará la señal en condiciones de reposo (ojos abiertos/cerrados), durante una tarea cognitiva y ante artefactos controlados.

 ## 3. Materiales y metodología: <a name="materiales-y-metodología"></a> 
 ### Materiales:
| Cantidad | Descripción                         |
|----------|-------------------------------------|
| 1        | KIT BITalino (r)evolution con módulos ECG           |
| 1        | Laptop/celular con Bluetooth                |
| 1        | Software OpenSignals (r)evolution   |
| 3        | Electrodos Ag/AgCl desechables (gel)            |
| 1        | Cable de 3 conductores (para ECG)   |
| 1        | Batería LiPo 3.7V                   |
| Rotativo (demo)        | Ultracortex Mark IV (dry-electrode headset)            |



### Metodología
1. **Montaje de electrodos**
   - Limpiar Fp1, Fp2 y mastoide derecha.
   - Conectar Electrodo1 → Fp1, GND → Fp2, Electrodo2 → mastoide (referencia).
   - Comprobar impedancia en OpenSignals (< 20 kΩ).
     
<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/ColocacionElectrodosI.jpg?raw=true" alt="Colocación de electrodos" width="600"/>
  <p><em>Figura 4. Colocación del electrodo de referencia.</em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/ColocacionElectrodosII.jpg?raw=true" alt="Colocación de electrodos" width="600"/>
  <p><em>Figura 5. Colocación de electrodos en la frente (FP1-derecha y FP2-izquierda).</em></p>
</div>


2. **Secuencia de Registro**
   
| Minuto     | Condición        | Detalle |
|------------|-----------------|-----------------|
| 0-1        | Basal 1         | Ojos abiertos, fijar punto |
| 1-2        | Basal 2         | Ojos cerrados| 
| 2-4        | Tarea Cognitiva | Restar 7 desde 100 en silencio o ejercicios punto 4.4 |
| 4-6        | Artefactos      | Parpadear cada 2 s y masticar |
| 6-12       | Libre           | Diseño del grupo (música, respiración,etc.)|


3. **Preguntas realizadas en la tarea cognitiva**
   
    | Categoría  | Ejemplo         | Respuesta |
    |------------|-----------------|-----------------|
    | Simple     | Hay 3 aves en un árbol, llegan 7 más. ¿Cuántas aves hay en total? | 11 aves |
    | Simple     | Jonas tiene 5 manzanas y María tiene 4. ¿Cuántas manzanas tienen en total?| 9 manzanas| 
    | Simple     | Hanna tiene 9 dólares pero se ha gastado 4. ¿Cuántos dólares le quedan? | 5 dólares |
    | Complejo   | Juan anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que Juan y José juntos. ¿Cuántos puntos anotaron en total?      | 173 puntos|
    | Complejo   | El grupo A tiene 24 alumnos; 13 menos que el grupo B. El grupo C tiene 12 alumnos más que los grupos A y B juntos. ¿Cuál es el número total de alumnos?           | 134 alumnos|
   | Complejo     | Una tienda vendió 21 refrescos por la mañana, 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total?| 68 refrescos |
   
## 4. Resultados y limitaciones <a name="resultados-y-limitaciones"></a>
- **Resultados obtenidos en OpenSignals**
  
| Condición |Resultados|
|-----------|------------------|
| Basal 1 | [🎥 Ver video](https://youtu.be/dD4qEfKLl80) |
| Basal 2 | [🎥 Ver video](https://youtu.be/deVhpbaQNz4) |
| Tarea cognitiva| [🎥 Ver video](https://youtu.be/uEgXcAsAyZM)|
| Artefactos| [🎥 Ver video](https://youtu.be/2Y8fNCgnL4w)|
| Actividad libre: escuchar distintos tipos de música| [🎥 Ver video](https://youtu.be/SW1TGJtgqhQ)|

- **Resultados obtenidos en Python**
  
| Condición |RAW               |Señal Filtrada    |
|-----------|------------------|------------------|
| Basal 1 | <img src="./Imágenes%20en%20el%20anexo/EEGRawBasal1.jpg" alt="Raw Basal 1" width="80%">| <img src="./Imágenes%20en%20el%20anexo/EEGFiltradaBasal1.jpg" alt="Filtrado Basal 1" width="80%">|
| Basal 2 |<img src="./Imágenes%20en%20el%20anexo/EEGRawBasal2.jpg" alt="Raw Basal 2" width="80%">| <img src="./Imágenes%20en%20el%20anexo/EEGFiltradaBasal2.jpg" alt="Filtrado Basal 2" width="80%">|
| Tarea cognitiva|<img src="./Imágenes%20en%20el%20anexo/EEGRawTareaCognitiva.jpg" alt="Raw Tarea Cognitiva" width="80%">| <img src="./Imágenes%20en%20el%20anexo/EEGFiltradaTareaCognitiva.jpg" alt="Filtrado Tarea Cognitiva" width="80%">|
| Artefactos|<img src="./Imágenes%20en%20el%20anexo/EEGRawArtefactos.jpg" alt="Raw Artefactos" width="80%">| <img src="./Imágenes%20en%20el%20anexo/EEGFiltradaArtefactos.jpg" alt="Filtrado Artefactos" width="80%">|
| Actividad libre: escuchar distintos tipos de música|<img src="./Imágenes%20en%20el%20anexo/EEGRawActividadLibre.jpg" alt="Raw Actividad Libre" width="80%">| <img src="./Imágenes%20en%20el%20anexo/EEGFiltradaActividadLibre.jpg" alt="Filtrado Actividad Libre" width="80%">|

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/basal1-freq.jpeg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 6. FFT de la EEG filtrada de BASAL 1</em></p>
</div>

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/basal2-freq.jpeg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 7. FFT de la EEG filtrada de BASAL 2</em></p>
</div>

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/tareacog-freq.jpeg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 8. FFT de la EEG filtrada de TAREA COGNITIVA</em></p>
</div>

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/artefact-freq.jpeg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 9. FFT de la EEG filtrada de ARTEFACTOS</em></p>
</div>

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/libre-freq.jpeg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 10. FFT de la EEG filtrada de ACTIVIDAD LIBRE</em></p>
</div>

- **Potencia α en ojos abiertos vs. cerrados**
  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/PSDBasal1.jpg?raw=true" alt="PSD Basal 1" width="600"/>
  <p><em>Figura 11. PSD Basal 1</em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/PSDBasal2.jpg?raw=true" alt="PSD Basal 2" width="600"/>
  <p><em>Figura 12. PSD Basal 2</em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/PSDTareaCognitiva.jpg?raw=true" alt="PSD Tarea Cognitiva" width="600"/>
  <p><em>Figura 13. PSD Tarea Cognitiva</em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/PSDArtefactos.jpg?raw=true" alt="PSD Artefactos" width="600"/>
  <p><em>Figura 14. PSD Artefactos </em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/PSDActividadLibre.jpg?raw=true" alt="PSD Actividad Libre" width="600"/>
  <p><em>Figura 15. PSD Actividad Libre (Música) </em></p>
</div>

- **Incremento de β durante la tarea cognitiva (t‑test pareado)**

  <div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/Basal1VSTareaCognitiva.jpg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 16. Basal 1 vs Tarea Cognitiva </em></p>
</div>

<div align="center">
  <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/Basal2VSTareaCognitiva.jpg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 17.  Basal 2 vs Tarea Cognitiva </em></p>
</div>

- **Detectar artefactos de parpadeo (> 80 μV) y contabilización (FALTA)**
<div align="center">
   <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/01c265f2-b4dd-481d-a353-feb048993aa3.jpeg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 18.  Detección de parpadeo en BASAL 1 </em></p>
</div>

<div align="center">
   <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/88bbd241-ae4c-4e8a-a7e6-a33b7eb98b00.jpeg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 19.  Detección de parpadeo en BASAL 2 </em></p>
</div>

<div align="center">
   <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/ee9aeb5e-9c38-4284-8a6f-b2154e77010a.jpeg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 20.  Detección de parpadeo en TAREA COGNITIVA </em></p>
</div>

<div align="center">
   <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/5a172f81-df4a-441f-8cc3-75f66b949b03.jpeg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 21.  Detección de parpadeo en ARTEFACTOS </em></p>
</div>

<div align="center">
   <img src="https://github.com/Rodrigo1804/GRUPO5-ISB-2025-I/blob/main/Laboratorios/Laboratorio%206%20-%20BiTalino%20EEG/Im%C3%A1genes%20en%20el%20anexo/4ce8c5fd-6350-41cb-aa8f-1ddc5aed8271.jpeg?raw=true" alt="Basal 1 VS tarea cognitiva" width="600"/>
  <p><em>Figura 22.  Detección de parpadeo en ACTIVIDAD LIBRE </em></p>
</div>

- **Preguntas adicionales para discusión**
  * ¿Qué banda de frecuencia predomina al cerrar los ojos?
    
    Se concluyó en diversos estudios que la banda de frecuencia que predomina se encuentra desde 0 a 10 y 12 Hz, además se enfatiza su predominancia en la banda 
    alfa, de 8 a 12 Hz. Esto se debe a la ausencia de actividad cerebral de la región occipital que regula los procesos visuales activos, incluso cuando no hay 
    estimulación visual directa, que en este caso sería al cerrar los ojos.[3][4]
    
  * ¿Qué filtro es imprescindible para EEG y por qué?
    
     El filtro imprescindible para un EEG es el pasabanda, ya que hay diferentes componentes de la señal repartidos que requieren ser eliminados, tanto en 
     frecuencias bajas como altas. Debido a que la señal es muy débil, de orden bajo, se requiere eliminar interferencias como movimientos lentos, sudoración o 
     respiración y masticación, que son frecuencias bajas, y asimismo interferencias artefactos musculares de la cabeza, ruido eléctrico o mecánico del ambiente 
     perteneciente a frecuencias altas.[5]
    
  * ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.
 
    Estudios recientes afirman la posibilidad de modular a voluntad las señales de un EEG. Esto se consigue a través de técnicas de entranamiento cerebral de regiones específicas del mismo para potenciarlas, entre las más populares se encuentra el neurofeedback.[6] Este consiste en un autoentrenamiento no invasivo de la actividad cerebral en tiempo real. Se puede usar para tratar diferentes afecciones como mejorar la concentración en niños con TDAH.[7]
     
  * ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?
    
    Sí se encuentran diferencias entre Fp1 y Fp2 principalmente porque se encuentran en hemisferios diferentes y son activos en procesos diferentes distinguibles 
    en el EEG y como mencionamos anteriormente, notables por ejemplo a través del entrenamiento con neurofeedback.[8]  Por ejemplo, Fp1 está involucrado en mecanismos de lenguaje, lógica e incluso en la influencia emocional positiva, mientras que Fp2 está relacionado a mecanismos del sistema simpático, que nos mantiene alertas, atentos, e igualmente en emociones negativas.[8][9]



 
## 5. Referencias <a name="referencias"></a>
[1] Mayo Clinic. Electroencefalograma (EEG) [Internet]. Mayo Clinic; 2023 [citado 2 mayo 2025]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875

[2] Proença M, Mrotzeck K. BITalino Home Guide #3 – Electroencephalography (EEG). Lisbon: PLUX – Wireless Biosignals S.A.; 2021. Disponible en: https://bitalino.com

[3]Kuhbandner, C., Lichtenfeld, S., & Pekrun, R. (2021). Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes. Scientific Reports, 11, 11510. https://www.nature.com/articles/s41598-021-90437-7

[4]Zibrandtsen, I. C., Kidmose, P., & Kjaer, T. W. (2022). Electroencephalographic Assessment of Eye Closure in Resting State: A Large-Scale Clinical EEG Study. Brain Sciences, 12(1), 85. https://pubmed.ncbi.nlm.nih.gov/35075196/

[5] J. Huang, M. Y. Wang, C. Jin, y H. Wu, “Detection of Depression in Children and Adolescents Based on EEG Using an Interpretable Deep Learning Framework,” Discover Artificial Intelligence, vol. 4, no. 1, Art. no. 15, 2024. Disponible en: https://www.sciencedirect.com/science/article/pii/S2666720724001152

[6]M. J. Ros, B. Gonçalves, N. Sato, y M. A. Sitaram, “Neurofeedback training of default mode network connectivity in major depressive disorder: A randomized controlled trial,” NeuroImage, vol. 275, Art. no. 120216, 2023. Disponible en: https://www.sciencedirect.com/science/article/pii/S1053811923004718

[7]Neuros Center, “¿Qué es el neurofeedback?,” Neuros Center, 2024. Disponible en: https://neuroscenter.com/neurofeedback/que-es/

[8] M. Balconi and G. Mazza, “Brain oscillations and BIS/BAS (behavioral inhibition/activation system) effects on processing masked emotional cues. ERP and coherence measures of valence and frequency band,” Brain Research, vol. 1353, pp. 92–102, 2010. Disponible en: https://www.sciencedirect.com/science/article/abs/pii/S0304394010011821

[9]Cleveland Clinic, “Parasympathetic Nervous System (PSNS),” Cleveland Clinic, 2023. Disponible en: https://my.clevelandclinic.org/health/body/23266-parasympathetic-nervous-system-psns

