import os 
import pandas as pd

# Dinamicamente se obtiene la ruta base del proyecto
base_path = os.path.dirname(__file__)

# Se construye la ruta relativa a los datasets
movies_date_path = os.path.join(base_path, "datasets", "movies_date.csv")
movies_details_path = os.path.join(base_path, "datasets", "movies_details.csv")
movies_score_path = os.path.join(base_path, "datasets", "movies_score.csv")

# Se carga el dataset en una variable global
try:
    movies_date = pd.read_csv(movies_date_path)
    movies_details = pd.read_csv(movies_details_path)
    movies_score = pd.read_csv(movies_score_path)
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