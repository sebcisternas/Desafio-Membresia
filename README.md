# Desafio-Membresia

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación de streaming de videos de películas y series chilenas. El foco principal está en la implementación del backend, específicamente en la estructura de clases para gestionar las membresías de los usuarios suscriptores.


## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **`membresia.py`**: Contiene la definición de las clases que representan los distintos tipos de membresías de los usuarios suscriptores. Se emplea herencia para gestionar los comportamientos específicos de cada tipo de membresía.

- **`apoyo_desafio.py`**: Archivo de soporte que proporciona un método protegido `_crear_nueva_membresia` para crear nuevas membresías según el tipo solicitado.


## Clases de Membresías Implementadas

- **`Membresia`**: Clase abstracta base que define la estructura común de todas las membresías.

- **`MembresiaGratis`**: Representa la membresía gratuita con un dispositivo y la capacidad de cambiar a otros tipos de membresía.

- **`MembresiaBasica`**: Membresía con un costo, un límite de dos dispositivos y la posibilidad de cambiar a membresías superiores.

- **`MembresiaFamiliar`**: Membresía con un mayor costo, hasta cinco dispositivos y días de regalo al crearse.

- **`MembresiaSinConexion`**: Membresía que permite ver contenido sin conexión, con un límite de dos dispositivos y días de regalo al crearse.

- **`MembresiaPro`**: La membresía más avanzada con mayor costo, hasta seis dispositivos y días de regalo al crearse.


## Ejecución y Pruebas

El archivo `membresia.py` incluye casos de prueba al final del código que demuestran el funcionamiento de las distintas membresías. Estos casos cubren la creación de membresías, cambios entre diferentes tipos y la cancelación de suscripciones.

Para ejecutar las pruebas, simplemente ejecute el archivo `membresia.py` en su entorno de desarrollo de Python.

