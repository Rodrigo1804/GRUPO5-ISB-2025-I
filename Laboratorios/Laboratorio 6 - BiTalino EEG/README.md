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

| Banda     | Ran-go (Hz)| Estado asociado                         | Ejemplos de tareas/estudios                    |
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
    
2. **Secuencia de Registro**
| Minuto     | Condición           | Detalle |
|------------|-----------------|-----------------|
| 0-1        | Basal 1         | Ojos abiertos, fijar punto
| 1-2        | Basal 2         | Ojos cerrados
| 2-4        | Tarea Cognitiva | Restar 7 desde 100 en silencio o ejercicios punto 4.4 
| 4-6        | Artefactos      | Parpadear cada 2 s y masticar 
| 6-12       | Libre           | Diseño del grupo (música, respe)


   
## 4. Resultados y limitaciones <a name="resultados-y-limitaciones"></a>


## 5. Referencias <a name="referencias"></a>
[1] Mayo Clinic. Electroencefalograma (EEG) [Internet]. Mayo Clinic; 2023 [citado 2 mayo 2025]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875

[2] Proença M, Mrotzeck K. BITalino Home Guide #3 – Electroencephalography (EEG). Lisbon: PLUX – Wireless Biosignals S.A.; 2021. Disponible en: https://bitalino.com

