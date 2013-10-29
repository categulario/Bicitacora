XBTrack
=======

#### Images

An inline image ![Smaller icon](http://smallerapp.com/favicon.ico "Title here"), title is optional.


Aplicación para el 1º Xackatón, rutas y puntos clave de ciclismo urbano.

## Si quieres desarrollar

### Setup Inicial

Todos estos pasos se realizan en la consola, cualquier duda: @categulario en twitter o a.wonderful.code@gmail.com
Tratar de seguir este procedimiento en windows podría ser un dolor en el trasero... y en la cabeza... y en todas partes

* instalar python, python-virualenv y git de ser necesario
* Crear un entorno virtual `virtualenv --distribute --system-site-packages EntornoBicitacora`
* Entrar en el entorno `cd EntornoBicitacora`
* Activar el entorno `source bin/activate`
* Clonar el proyecto `git clone https://github.com/developingo/Bicitacora.git`
* Entrar al repositorio `cd Bicitacora`
* Instalar las dependencias `pip install -r requirements_weak.txt`
* Instalar la base de datos `./manage_dev.py syncdb --all`.
	Esto pregunta por la creación de un usuario, decir que si y seguir el procedimiento es buena idea. Cuando pide el nombre de usuario hay que poner el correo
	y cuando pide el correo también hay que dar el correo. No olvidar estos datos por favor
* Correr las migraciones `./manage_dev.py migrate --fake`
* Correr el servidor `./manage_dev.py runserver`
* Visitar en un navegador la dirección `http://localhost:8000/perfil` y llenar los datos del perfil
* ¡Listo!

### Desarrollar

4 sencillos pasos

* En un terminal, ir a la carpeta `EntornoBicitacora`
* Activar el entorno `source bin/activate`
* Entrar al repo `cd Bicitacora`
* correr el servidor `./manage_dev.py runserver`
