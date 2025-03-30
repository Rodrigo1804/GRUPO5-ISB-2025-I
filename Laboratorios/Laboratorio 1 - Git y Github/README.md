# Anexo: Resumen de comandos de git

## ¿Qué es Git y GitHub?
- **Git**: Es una herramienta que guarda versiones de tus archivos/códigos. Sirve para no perder el progreso, trabajar en equipo, y volver atrás si algo sale mal.
- **GitHub**: Es una plataforma online donde puedes guardar tus repositorios Git y colaborar con otros. Vendría a ser una especie de nube.

## Comandos Básicos de Git y GitHub
En este anexo resumiremos los comandos esenciales para trabajar con Git y GitHub, desde la creación de un repositorio hasta la subida de archivos.

## ¿Cómo crear un repositorio?

### Desde Git
**1. Instala Git o verifica que Git esté instalado**  
Puedes verificar si Git está instalado escribiendo en la terminal:

```bash
git --version
```
Este comando debería devolver la versión de git. En caso no esté instalado, instálalo desde: https://git-scm.com

**2. Inicia sesión y autentificate con GitHub**
Para poder subir archivos a tu cuenta de GitHub desde la terminal, debes autenticarte. 
```bash
ssh-keygen -t ed25519 -C "tuemail@ejemplo.com"
```
Sigue las instrucciones y copia el SSH generado 
<br>
Luego, ve a tu perfil de GitHub  → Settings 

<img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura4.png" alt="Figura 4" width="200">

→ SSH and GPG keys

<img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura5.png" alt="Figura 5" width="400">

→ New SSH key

<img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura6.png" alt="Figura 6" width="500">
	
y pega la clave :)


**3. Configura tu usuario en Git**
Este Paso solo se realiza por única vez
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

Puedes verificar si la conexión fue exitosa con 
```bash
ssh -T git@github.com
```
Si recibes de respuesta: Hi ! You've successfully authenticated, but GitHub does not provide shell access. Entonces puedes seguir con los siguientes pasos para crear tu primer repositorio.

**4. Iniciáliza un repositorio local**
El comando mkdir crea la carpeta y git init convierte esa carpeta en un repositorio local de Git.
```bash
mkdir nombre-del-proyecto ## 
cd nombre-del-proyecto
git init
```
Ahora ya tienes tu repositorio creado y puedes comenzar a usarlo!

### Desde GitHub
1. Registrate o inicia sesión en GitHub.
2. Crea un nuevo repositorio
<br>Hacer clic en *New* o *Nuevo repositorio*. Esta opción se encuentra en la pestaña *Home*, en la esquina superior izquierda
<img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura1.png" alt="Figura 1" width="500">
	
3. Crear el repositorio
 Acá se abrirá una nueva pagina donde podrás asignarle un nombre a tu nuevo repositorio y opcionalmente una pequeña descripción. 
 <img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura2.png" alt="Figura 2" width="500">
 <br>Nota: Recomendamos utilizar un repositorio publico y activar la opción de generar un archivo README.md al crearlo.
 
4. Hacer clic en Create repository.
<img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura3.png" alt="Figura 3" width="400">
6. Copiar la URL del repositorio para conectarlo con Git.

## ¿Cómo subir archivos?

### Desde Git:
1. Inicializamos Git
```bash
git init
```
2. Agregamos los archivos al área de staging
```bash
git add .
```  
El punto "." significa "todos los archivos del directorio actual".

3. Realizamos un commit:
```bash
git commit -m "1er commit: subiendo archivos iniciales"
```

4. Conectamos nuestro proyecto con GitHub:
```bash
git remote add origin https://gitgub.com/Rodrigo1804/repositorio.git
```

5. Cambiamos la rama principal a `main`:
```bash
git branch -M main
```

6. Subimos nuestros archivos a Github
```bash
git push -u origin main
```

### ¿Qué pasa si ya clonamos un repositorio con `git clone`?
- Si es que ya clonamos un repositorio existente de GitHub:
```bash
git clone https://github.com/Rodrigo1804/repositorio.git
cd repositorio
```
- Podemos hacer nuestros cambios de esta manera:
```bash
git add .
git commit -m "Mis cambios"
git push
```
- Si es que necesitamos traer los últimos cambios del repositorio remoto:
```bash
git pull origin main
```
Usualmente la rama principal tiene como nombre `master`, así que también podemos usar:
```bash
git pull origin master
```
Algunos comandos útiles:
- Podemos usar `git status` para ver qué archivos están listos para realizar `commit` para guardar el historial del proyecto o volver atrás si es que algo saliera mal.
- Usar `git log` nos sirve para ver el historial de `commits`
- siempre debes usar `git pull` antes de `git push` si es que estás trabajando en equipo.


### Desde GitHub

1. Entrar al repositorio creado.  
2. Hacer clic en **Add file > Upload files**.  
   ![Figura 7](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura7.png)  
3. Arrastrar o seleccionar los archivos a subir.  
   ![Figura 8](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura8.png)  
4. Escribir un mensaje en el campo "Commit changes" para describir los cambios que se esta realizando en el repositorio.  
   ![Figura 9](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura9.png)  
5. Hacer clic en **Commit changes**.  


## Extra 1: Ramas
En GitHub, una rama (también llamado branch) es una línea independiente de desarrollo en un repositorio. Ayuda a mantener el código principal sin cambios ya que se pueden añadir nuevas características y/o correcciones hasta que se decida que estos estén listos y se fusionen en un Pull Request.

### Ver las ramas en el repositorio en GitHub
1. Ve al repositorio en GitHub
   
    ![Figura 10](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura10.png)
   
3. Haz clic en el botón desplegable que muestra la rama actual (por defecto, suele ser `main`)
4. Verás una lista de ramas disponibles
   
    ![Figura 11](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura11.png)
   
### Creación de nueva rama en GitHub
1. En el repositorio, haz clic en el botón desplegable de la rama
2. Escribe el nombre de la nueva rama a crear en el cuadro de búsqueda
3. Haz clic en `Create branch`

    ![Figura 12](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura12.png)

### Hacer cambios en una rama y creación de Pull Request
1. Cambia a la rama en donde deseas hacer cambios (a través del menú desplegable)
2. Edita los archivos. Puede ser directamente en GitHub o puedes subir dedsde tu computadora
3. Confirma los cambios dando clic en **Commit changes**
4. Ve a la pestaña `Pull Requests` y haz clic en `New pull request`
   
    ![Figura 13](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura13.png)
    ![Figura 14](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura14.png)
   
6. Selecciona la rama con cambios y compárala con `main`
   
   ![Figura 15](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura15.png)

Un Pull Request ayudará a algún miembro del equipo a revisar las diferencias entre el main y la rama antes de fusionarlas.

### Fusión de una rama en `main`

1. Abre el Pull Request correspondiente.
2. Revisa los cambios y asegúrate de que todo esté correcto.
3. Haz clic en `Merge pulll request` y confirma la fusión.

Una vez fusionado el main con la rama elegida, puedes eliminar la rama en caso de que ya no la necesites.

### Eliminar ramas en GitHub
1. Ve a la pestaña de `Branches` en el repositorio
2. Busca la rama que deseas eliminar
3. Haz clic en el ícono de eliminar (papelera) que se encuentra junto a la rama
   
    ![Figura 16](/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imagenes%20en%20el%20Anexo/Figura16.png)

## Extra 2: Lenguaje Markdown
Markdown es un lenguaje de marcado ligero para dar formato a texto en plataformas como GitHub. Existen diversos tipos de elementos de síntaxis pero 3 son los más importantes y engloban la mayoría de elementos.

# Elementos de Bloque 
## Párrafos y saltos de línea
Para crear un nuevo párrafo en Markdown, solo necesitas dejar una línea en blanco entre los bloques de texto (presionar dos veces la tecla Enter).

Ten en cuenta que Markdown no permite múltiples líneas en blanco seguidas: si colocas varias, se reducirán a una sola cuando se renderice el texto.

Si lo que buscas es hacer un salto de línea dentro del mismo párrafo, debes presionar la barra espaciadora dos veces y luego `Enter`.

## Encabezados
Para crear títulos o subtítulos en Markdown se usan las almohadillas (#), que funcionan como indicadores de nivel.

Debes colocar una almohadilla por cada nivel de encabezado que desees, desde el nivel 1 (más grande) hasta el nivel 6 (más pequeño).

Por ejemplo:

```
# Encabezado de nivel 1  
## Encabezado de nivel 2  
### Encabezado de nivel 3  
#### Encabezado de nivel 4  
##### Encabezado de nivel 5  
###### Encabezado de nivel 6  
```
# Encabezado de nivel 1  
## Encabezado de nivel 2  
### Encabezado de nivel 3  
#### Encabezado de nivel 4  
##### Encabezado de nivel 5  
###### Encabezado de nivel 6  

## Citas
Las citas se generan utilizando  `>` al comienzo del bloque de texto:
```
>Tengo deberes sagrados que cumplir y los cumpliré hasta quemar el último cartucho. - Francisco Bolognesi
 
```
>Tengo deberes sagrados que cumplir y los cumpliré hasta quemar el último cartucho. - Francisco Bolognesi

Si la cita está conformada de varios párrafos, se debe añadir el mismo símbolo `>` al comienzo de cada uno de ellos.


## Listas
Para crear listas, se puede utilizar asteriscos `*`, guiones `-` o suma `+`

```
* Elemento de lista 1
* Elemento de lista 2
- Elemento de lista 3
- Elemento de lista 4
+ Elemento de lista 5
+ Elemento de lista 6
 
```

* Elemento de lista 1
* Elemento de lista 2
- Elemento de lista 3
- Elemento de lista 4
+ Elemento de lista 5
+ Elemento de lista 6


## Bloque de códigos

Para la creación de un bloque de códigos solo se debe encerrarlo en tres virgulilllas `~`

```
~~~
Código
~~~
 
```

~~~
Código
~~~

 
# Elementos de Línea 
## Negritas y cursivas

En markdown se utilizan asteriscos `*` y guiones bajos `_` para enfatizar. Se escribe entre 2 `*` o `_` para negritas, entre 4 para cursivas y entre 6 para cursiva y negritas.

```
_cursiva_
*cursiva*

__negrita__
**negrita**

___cursivaynegrita___
***cursivaynegrita***
```
_cursiva_
*cursiva*

__negrita__
**negrita**

___cursivaynegrita___
***cursivaynegrita***


## Links o enlaces 
## Código
## Imágenes

 

 ### Titulo 3
 ´´´
 # Título 1, ## Título 2, ### Título 3
 
