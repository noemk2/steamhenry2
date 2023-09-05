# Proyecto de Machine Learning (MLOps) - Sistema de Recomendación de Juegos en Steam

## Introducción

Este proyecto se centra en el desarrollo de un sistema de recomendación de juegos para la plataforma Steam. El objetivo principal es predecir cinco juegos que podrían gustar a un usuario en función de su historial de juego y reseñas. 

## Video 
Se incluye un video de 7min explicando el proyecto:
https://steamhenry.onrender.com


Para lograr esto, se ha creado un API web que proporciona diversas funcionalidades relacionadas con el análisis de datos y la generación de recomendaciones. El API está alojado en https://steamhenry.onrender.com y ofrece los siguientes endpoints:


### 1. `userdata(User_id: str)`

Este endpoint devuelve información sobre un usuario en particular. Recibe un parámetro `User_id` que representa el identificador único del usuario en Steam. La respuesta incluye la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reseñas y la cantidad de juegos en su biblioteca.

### 2. `countreviews(YYYY-MM-DD: str, YYYY-MM-DD: str)`

Este endpoint permite contar la cantidad de usuarios que realizaron reseñas entre dos fechas dadas. Además, proporciona el porcentaje de recomendación de estos usuarios en base a sus reseñas.

### 3. `genre(género: str)`

Devuelve el puesto en el que se encuentra un género de juegos en el ranking de juegos de Steam, analizado bajo la columna "PlayTimeForever."

### 4. `userforgenre(género: str)`

Este endpoint muestra los cinco usuarios con más horas de juego en un género específico. Incluye sus URLs de perfil y User_id.

### 5. `developer(desarrollador: str)`

Proporciona información sobre un desarrollador de juegos, incluyendo la cantidad de juegos desarrollados por año y el porcentaje de contenido gratuito.

### 6. `sentiment_analysis(año: int)`

Según el año de lanzamiento, este endpoint devuelve una lista con la cantidad de registros de reseñas de usuarios categorizados con un análisis de sentimiento.

## Exploración de Datos y Desarrollo del Modelo

El proceso de desarrollo de este sistema de recomendación se encuentra documentado en el archivo EDA_Steami.pynb (Jupyter Notebook) o EDA_Steami.pdf. En este documento se detalla la carga de los datos, la exploración de los mismos y el estudio de la variable "recommend". Además, se describen las etapas de preprocesamiento de datos, creación del modelo de recomendación y evaluación de errores.

El objetivo principal del modelo es generar recomendaciones precisas y personalizadas para los usuarios de Steam, lo que mejora la experiencia del usuario y puede aumentar la retención en la plataforma.

El proyecto combina elementos de Machine Learning y MLOps para garantizar un flujo de trabajo eficiente y la implementación de un modelo de recomendación en producción a través del API web mencionado anteriormente.

El código y los detalles técnicos específicos se encuentran en el repositorio del proyecto, que está disponible en [URL del repositorio](https://github.com/noemk2/steamhenry/src).

Este README.md proporciona una descripción general del proyecto y su funcionalidad, mientras que el archivo EDA_Steami.pynb o EDA_Steami.pdf contiene los detalles técnicos y los resultados obtenidos en el proceso de desarrollo.

¡Esperamos que este sistema de recomendación de juegos en Steam sea útil y proporcione recomendaciones emocionantes a los usuarios de la plataforma!