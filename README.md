![Logo Soy Henry](source/soyhenry_logo.png)

# Sistema de Recomendación de Películas

## Descripción
Este proyecto implementa un sistema de recomendación de películas en el cual el usuario ingresa el título de una película y el sistema entrega un listado de cinco películas recomendadas según la similitud que tengan con la película ingresada. 

El sistema utiliza un modelo de Machine Learning basado en similitud coseno y está desplegado usando **FastAPI** y **Render**.

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