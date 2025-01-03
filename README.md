![alt text](_src/soyhenry_logo.png)

# Sistema de Recomendación de Películas

## Descripción
Este proyecto implementa un sistema de recomendación de películas en el cual el usuario ingresa el título de una película y el sistema entrega un listado de cinco películas recomendadas según la similitud que tengan con la película ingresada. 

El sistema utiliza un modelo de Machine Learning basado en similitud coseno y está desplegado usando **FastAPI** y **Render**.

Este proyecto incluye las siguientes funciones:

- `cantidad_filmaciones_mes`: Proporciona la cantidad de películas estrenadas en un mes específico (en español).
- `cantidad_filmaciones_dia`: Devuelve la cantidad de películas estrenadas en un día de la semana (en español).
- `score_titulo`: Devuelve el título, el año de estreno y la popularidad (score) de una película.
- `votos_titulo`: Proporciona el total de votos y el promedio de puntuación de una película. Solo muestra resultados si cuenta con más de 2000 votos.
- `get_actor`: Muestra el éxito del actor (medido por el retorno de sus películas), la cantidad de filmaciones en las que ha participado y su promedio de retorno.
- `get_director`: Devuelve el éxito total del director, junto con el título, el año de estreno, los ingresos, el presupuesto y el retorno de cada una de sus películas.
- `recomendacion`: A partir del título de una película, genera una lista de 5 películas similares, clasificadas por puntuación de similitud.

## Dataset

Los dataset utilizados contienen la siguiente información:

### movies_details
| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `movie_id`        | Id de cada película                                       |
| `title`           | Título en inglés                                          |
| `budget`          | Presupuesto en USD                                        |
| `revenue`         | Ganacias generadas en USD                                 |
| `return`          | Retorno en USD                                            |

### movies_date
| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `movie_id`        | Id de cada película                                       |
| `release_year`    | Año de estreno                                            |
| `release_month`   | Mes de Estreno                                            |
| `release_day`     | Día de estreno                                            |

### movies_actors
| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `movie_id`        | Id de cada película                                       |
| `actor_name`      | Actor de la película                                      | 

### movies_directors
| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `movie_id`        | Id de cada película                                       |
| `director_name`   | Director de la película                                   |                                      

### movies_score
| **Columna**       | **Descripción**                                           |
|-------------------|-----------------------------------------------------------|
| `movie_id`        | Id de cada película                                       |
| `popularity`      | Puntaje de popularidad de la película, asignado por TMDB  |
| `vote_count`      | Número de votos recibidos por la película en TMDB         |
| `vote_average`    | Puntaje promedio de reseñas                               |

### movies_ml
| **Columna**            | **Descripción**                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------|
| `budget`               | Presupuesto de la película en USD.                                                                |
| `id`                   | Identificador único de cada película.                                                             |
| `popularity`           | Puntaje de popularidad asignado por TMDB.                                                         |
| `release_date`         | Fecha de lanzamiento en formato YYYY-MM-DD.                                                       |
| `revenue`              | Ingresos generados por la película en USD.                                                        |
| `runtime`              | Duración de la película en minutos.                                                               |
| `title`                | Título de la película en inglés.                                                                  |
| `vote_average`         | Puntuación promedio de los usuarios en TMDB.                                                      |
| `vote_count`           | Total de votos recibidos por la película en TMDB.                                                 |
| `Action`, `Adventure`, ..., `Western` | Géneros codificados en formato one-hot.                                            |
| `African Languages`, ..., `Slavic Languages` | Idiomas codificados en formato one-hot.                                     |
| `Africa`, ..., `South America` | Regiones codificadas en formato one-hot.                                                  |
| `release_year`         | Año de lanzamiento de la película.                                                                |
| `return`               | Relación ingresos-presupuesto (e.g., 2 = el doble del presupuesto).                               |


### movies_ml_details
Este dataset expande `movies_ml` añadiendo columnas preprocesadas para machine learning.

### movies_ml_processed
Este Dataset es una versión normalizada de `movie_ml`, preparado para algoritmos machine learning. Todas las características de tipo numérico han sido escaladas o normalizadas.

**Fuente de datos original**: [TMDB Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## Requisitos

Este proyecto utiliza las siguientes dependencias:

Para ejecutar este proyecto, necesitas instalar las siguientes dependencias:

- **Bibliotecas esenciales para análisis y manipulación de datos:**
  - `numpy==2.2.0`
  - `pandas==2.2.3`
  - `matplotlib==3.10.0`
  - `seaborn==0.13.2`
  - `scikit-learn`

- **Frameworks y herramientas para el desarrollo web:**
  - `fastapi==0.115.6`
  - `uvicorn==0.34.0`
  - `python-multipart`
  - `starlette==0.41.3`

- **Dependencias para manejo de fechas y formatos:**
  - `python-dateutil==2.9.0.post0`
  - `pytz==2024.2`
  - `tzdata==2024.2`

- **Otras dependencias importantes:**
  - `annotated-types==0.7.0`
  - `anyio==4.7.0`
  - `click==8.1.7`
  - `colorama==0.4.6`
  - `contourpy==1.3.1`
  - `cycler==0.12.1`
  - `fonttools==4.55.3`
  - `h11==0.14.0`
  - `idna==3.10`
  - `kiwisolver==1.4.7`
  - `packaging==24.2`
  - `pillow==11.0.0`
  - `pydantic==2.10.4`
  - `pydantic_core==2.27.2`
  - `pyparsing==3.2.0`
  - `six==1.17.0`
  - `sniffio==1.3.1`
  - `typing_extensions==4.12.2`

## Uso

El proyecto incluye diversos endpoints que permiten explorar información sobre películas y realizar recomendaciones. A continuación, se describen las funcionalidades disponibles:

### **1. Cantidad de Filmaciones por Mes: `/cantidad-filmaciones-mes`**
- **Descripción**: Devuelve la cantidad de películas estrenadas en un mes específico ingresado en español.
- **Entrada**: Nombre del mes (texto en español, por ejemplo: "Enero").
- **Salida**: Número total de películas estrenadas ese mes.

### **2. Cantidad de Filmaciones por Día: `/cantidad-filmaciones-dia`**
- **Descripción**: Devuelve la cantidad de películas estrenadas en un día específico de la semana (en español).
- **Entrada**: Día de la semana (texto en español, por ejemplo: "Lunes").
- **Salida**: Número total de películas estrenadas ese día.

### **3. Información sobre una Película: `/score-titulo`**
- **Descripción**: Proporciona el título, el año de estreno y la popularidad (score) de una película.
- **Entrada**: Título de la película (texto).
- **Salida**: Detalles básicos de la película.

### **4. Valoraciones de una Película: `/votos-titulo`**
- **Descripción**: Devuelve el total de votos y el promedio de puntuación de una película si cuenta con al menos 2000 votos.
- **Entrada**: Título de la película (texto).
- **Salida**:
  - Si tiene más de 2000 votos: Total y promedio de votos.
  - Si no cumple con esta condición: Un mensaje indicando que no se muestran valores.

### **5. Información sobre un Actor: `/get_actor`**
- **Descripción**: Devuelve el éxito de un actor, la cantidad de películas en las que ha participado y su promedio de retorno (éxito financiero de sus películas).
- **Entrada**: Nombre del actor (texto).
- **Salida**:
  - Éxito total (retorno sumado).
  - Número de películas en las que participó.
  - Promedio de retorno por película.

### **6. Información sobre un Director: `/get_director`**
- **Descripción**: Devuelve el éxito total del director (medido en retorno) y detalles sobre cada película que dirigió, como título, año de estreno, ingresos, presupuesto y retorno.
- **Entrada**: Nombre del director (texto).
- **Salida**: Éxito total del director y detalles de sus películas.

### **7. Sistema de Recomendación de Películas: `/recomendacion`**
- **Descripción**: Devuelve una lista de 5 películas similares al título ingresado, clasificadas por puntuación de similitud.
- **Entrada**: Título de la película (texto).
- **Salida**: Lista de películas similares con detalles como popularidad, año de estreno y puntaje de similitud.

## Despliegue

https://pimlops-fviera.onrender.com