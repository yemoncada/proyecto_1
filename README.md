# Proyecto 1. Pipeline con TFX para el dataset UCI Covertype Dataset

Este repositorio contiene un pipeline completo que utiliza el conjunto de datos UCI Covertype y explora los metadatos utilizando TFX. Además, se proporciona una imagen de Docker que se puede utilizar para ejecutar el pipeline. El proceso del pipeline se encuentra en un Jupyter Notebook llamado "data_pipeline.ipynb".

# Conjunto de datos UCI Covertype

Conjunto de datos UCI Covertype
El conjunto de datos UCI Covertype contiene información sobre las características de los bosques de los Estados Unidos y la clasificación de los tipos de bosques. El conjunto de datos consta de 581.012 registros y 54 características, incluyendo la elevación, la pendiente, la dirección de la pendiente y la distancia a cuerpos de agua.


# Ejecución del pipeline con Docker
Para ejecutar el pipeline, es necesario tener instalado Docker en su máquina. Después de clonar este repositorio, navegue hasta el directorio raíz y ejecute los siguientes comandos:

```shell
git clone https://github.com/yemoncada/proyecto_1
cd proyecto_1
docker build -t tfx_custom .
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
sudo docker run -it --name tfx_custom -e TZ=America/Bogota --rm -p 8888:8888  -v $PWD:/work tfx_custom

```

Estos comandos clonarán el repositorio en su máquina y navegarán al directorio del repositorio. Los comandos restantes compilarán la imagen de Docker y la ejecutarán. El comando docker build construye la imagen, docker rmi elimina las imágenes sin etiquetar, y docker run inicia el contenedor Docker con la imagen construida. El puerto 8888 se asigna para Jupyter Notebook.

# Pipeline en Jupyter Notebook

Una vez que se ha iniciado el contenedor Docker, el Jupyter Notebook se puede acceder en su navegador web local mediante la dirección IP localhost:8888 y el token que se muestra en la terminal después de ejecutar el comando docker run.

El notebook "data_pipeline.ipynb" contiene el proceso completo del pipeline, desde la carga de datos hasta la evaluación del modelo. El pipeline se divide en varios componentes, incluyendo la validación de datos, la transformación de datos y la formación del modelo.

# Conclusiones
Este repositorio demuestra cómo utilizar TFX para construir un pipeline completo con el conjunto de datos UCI Covertype. Al utilizar metadatos, el pipeline puede ser mejorado continuamente y ofrecer mejores resultados. La imagen de Docker proporciona una forma fácil de ejecutar el pipeline en cualquier máquina sin la necesidad de configurar el entorno.