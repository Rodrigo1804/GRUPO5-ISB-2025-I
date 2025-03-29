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
Si no lo está, instálalo desde: https://git-scm.com

**2. Inicia sesión y autentificate con GitHub**
Para poder subir archivos a tu cuenta de GitHub desde la terminal, debes autenticarte. 
```bash
ssh-keygen -t ed25519 -C "tuemail@ejemplo.com"
```
Sigue las instrucciones y copia el SSH generado 
<br>
Luego, ve a tu perfil de GitHub → Settings → SSH and GPG keys → New SSH key, y pega la clave.

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
	1.	Registrate o inicia sesión en GitHub.
	2.	Hacer clic en New o Nuevo repositorio.
 Esta opción se encuentra en la pestaña *Home*, en la esquina superior izquierda

 *aca va imagen de eso 
 
	3.	Crear el repositorio
 Acá se abrirá una nueva pagina donde podrás asignarle un nombre a tu nuevo repositorio y opcionalmente una pequeña descripción. 
 <br>Nota: Para evitar complicaciones no sugerimos tocar nada de las otras opciones que están seleccionadas o no seleccionadas por defecto

	5.	Hacer clic en Create repository.
	6.	Copiar la URL del repositorio para conectarlo con Git.

## ¿Cómo subir archivos?

git clone hhttp 
cd repositoro

git add.

git commit -m "Escribr mrnsaje si quieres"
git commit 

git push -u origin main

git pull origin master

inicializa git 
git add.

git remote add origin https://github.com/usuario/repositorio.git
git branch -M main



### Extra: Ramas
En git existe la posibilidad de crear ramas, estas son útiles para trabajar sin dañas el documento principal
 git branch nome
  git checkout rama 

### Desde Git


### Desde GitHub
.	Entrar al repositorio creado.
	2.	Hacer clic en Add file > Upload files.
	3.	Arrastrar o seleccionar los archivos a subir.
	4.	Escribir un mensaje de commit.
	5.	Hacer clic en Commit changes.



## Extra: Lenguaje Markdown
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
 
