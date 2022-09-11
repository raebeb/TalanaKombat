![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
# TALANAKOMBAT 🖥👾🥊

Esta es una pequeña aplicación que relata el épico duelo entre Tonnyn Stallone y Arnaldor Schuatseneger


## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

-   Docker 19.03^
-   Docker Compose 1.25^

---

## Instalación 🔧

### 1. Clonar el repositorio
```
git clone git@github.com:raebeb/TalanaKombat.git
```
ó
```
git clone https://github.com/raebeb/TalanaKombat.git
```
---

### 2. Levantar el contenedor
```
docker-compose up
```
> Si es primera vez que se levanta el proyecto, este se _buildeara_ e instalara todas las dependencias necesarias

Una vez levantado, la pelea comenzará automáticamente

Si en la terminal aparece un mensaje como el siguiente, el proyecto se ha levantado y ejecutado con éxito

```
app_1  | Tonnyn Stallone avanza y da una patada
app_1  | Arnaldold Scchuatseneger usa un Remuyuken!
app_1  | Tonnyn Stallone usa un Taladoken!
app_1  | Arnaldold Schuatseneger se mueve
app_1  | Tonnyn Stallone se agacha
app_1  | Arnaldold Scchuatseneger usa un Remuyuken!
app_1  | HA GANADO Arnaldold Schuatseneger y aun le quedaban 2 puntos de energia!
talanakombat_app_1 exited with code 0
```

### 3. Casos de prueba

En la raíz del proyecto se encuentra el archivo ```input.json```, desde este archivo se leen los datos para la pelea, para probar distintos casos es necesario modificar este archivo


## Ejecutando las pruebas ⚙
_El proyecto cuenta con una serie de tests, para llevarlos a cabo se debe ejecutar el siguiente comando_
```
docker-compose run app python app/tests/runner.py
```

***
## Construido con 🛠️
* [Python 3.10](https://www.python.org) - Lenguaje de programación
* [Docker](https://www.docker.com) - Gestor de contenedores

***


## Autores ✒️
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Trabajo inicial


## ⌨️ con ❤️ por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) 👩‍💻

```
          ／＞　 フ
         | 　_　_| 
       ／` ミ＿xノ 
      /　　　　 |
     /　 ヽ　　 ﾉ
    │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_  ヽ_)__)
＼二)
```
