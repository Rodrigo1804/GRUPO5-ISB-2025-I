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
.	Entrar al repositorio creado.
	2.	Hacer clic en Add file > Upload files.
 <img src="/Laboratorios/Laboratorio 1 - Git y Github/Imagenes en el Anexo/Figura7.png" alt="Figura 7" width="200">
	3.	Arrastrar o seleccionar los archivos a subir.
	4.	Escribir un mensaje de commit.
	5.	Hacer clic en Commit changes.

### Extra 1: Ramas
En git existe la posibilidad de crear ramas, estas son útiles para trabajar sin dañas el documento principal
 git branch nome
  git checkout rama 


## Extra 2: Lenguaje Markdown
Markdown es un lenguaje de marcado ligero para dar formato a texto en plataformas como GitHub.
<br>
Ejemplos útiles:
	•	Títulos: 
 ´´´bash
 # Título 1
 ## Título 2
 ### Titulo 3
 ´´´
 # Título 1, ## Título 2, ### Título 3
 
