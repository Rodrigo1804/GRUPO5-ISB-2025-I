Buenas tardes estimados alumnos,

El entregable de la proxima semana es subir un notebook documentado al github (en su folder adecuado), lo siguiente:

Deben elegir y desarrollar un ejercicio:

Ejercicio A: Simulación de distintos grados de asimetría
Objetivo: Estudiar cómo varía el Symmetry Ratio al alterar la amplitud relativa del músculo “izquierdo”.
Tarea:
Simula cinco pares de señales EMG idénticas (burst_number=10, noise=0.01) y escala el segundo canal al 20 %, 40 %, 60 %, 80 % y 100 % de la amplitud original.
Para cada par, limpia con nk.emg_clean(), extrae la envolvente con nk.emg_amplitude() y calcula el Symmetry Ratio.
Grafica en un único plot de barras el ratio obtenido frente al %% de escala utilizado.
Pregunta de reflexión: ¿A partir de qué nivel de desbalance la simetría cae por debajo de un umbral “aceptable” (p.ej. 80 %)?
