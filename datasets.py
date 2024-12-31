import os 
import pandas as pd

# Dinamicamente se obtiene la ruta base del proyecto
base_path = os.path.dirname(__file__)

# Se construye la ruta relativa a los datasets
movies_date_path = os.path.join(base_path, "datasets", "movies_date.csv")
movies_details_path = os.path.join(base_path, "datasets", "movies_details.csv")
movies_score_path = os.path.join(base_path, "datasets", "movies_score.csv")
movies_actors_path = os.path.join(base_path, "datasets", "movies_actors.csv")
movies_directors_path = os.path.join(base_path, "datasets", "movies_directors.csv")
movies_ml_path = os.path.join(base_path, "datasets", "movies_ml_processed.csv")
movies_ml_details_path = os.path.join(base_path, "datasets", "movies_ml_details.csv")

# Se cargan los dataset en una variable global
try:
    movies_date = pd.read_csv(movies_date_path)
    movies_details = pd.read_csv(movies_details_path)
    movies_score = pd.read_csv(movies_score_path)
    movies_actors = pd.read_csv(movies_actors_path)
    movies_directors = pd.read_csv(movies_directors_path)
    movies_ml = pd.read_csv(movies_ml_path)
    movies_ml_details = pd.read_csv(movies_ml_details_path)
    
except FileNotFoundError as e:
    raise Exception(f"Error al cargar los datasets: {e}")

# Se prepara el dataset combinado
try:
    movies_pop_date = pd.merge(
        pd.merge(movies_details, movies_date, on="movie_id", how="inner"),
        movies_score, on="movie_id", how="inner"
    )

    movies_pop_date = movies_pop_date[[
        "movie_id", "title", "release_year", "popularity", "vote_count", "vote_average"
    ]]
except KeyError as e:
    raise Exception(f"Error al preparar movie_pop_date: {e}")