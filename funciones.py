import pandas as pd
import datasets as ds

# def cantidad_filmaciones_mes( Mes ): 
# Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
# * Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X

def cantidad_filmaciones_mes(mes_input: str):
    try:
        mes_usuario = mes_input.capitalize()
        meses_lista = ['Enero','Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        if mes_usuario in meses_lista:
            n_peliculas = ds.movies_date[ds.movies_date['release_month'] == mes_usuario].shape[0]
            return f'{n_peliculas} Peliculas fueron estrenadas en el mes de {mes_usuario}'
        else:
            return "Por favor introduce un mes válido"
    except Exception as e:
        return f'Ocurrió un error inesperado {str(e)}'
    
# def cantidad_filmaciones_dia( Dia ): 
# Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
# * Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X
    
def cantidad_filmaciones_dia(dia_input):
    try:    
        dia_usuario = dia_input.capitalize()
        dias_lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        if dia_usuario in dias_lista:
            n_peliculas = ds.movies_date[ds.movies_date['release_day'] == dia_usuario].shape[0]
            return f'{n_peliculas} fueron estrenadas en los días {dia_usuario}'
        else:
            return "Por favor introduce un día válido"
    except Exception as e:
        return f'Ocurrió un error inesperado {str(e)}'

#def score_titulo( titulo_de_la_filmación ): 
# Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
# * Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X

def score_titulo(titulo_usuario):
    try:
        # Capitaliza el input del usuario para que no haya problemas de formato con los títulos del DataFrame
        titulo = titulo_usuario.title()

        # Filtra el DataFrame en busca de filas que calcen con el título del usuario
        respuesta_df = ds.movies_pop_date.loc[ds.movies_pop_date['title'] == titulo, ['title', 'release_year', 'popularity']]

        # Chequea si se encontraron filas
        if respuesta_df.empty:
            return "No se encontró ninguna película con ese título."
        
        # Se arma la respuesta para todas las filas encontradas
        resultados = []
        for _, row in respuesta_df.iterrows():
            resultados.append(
                f"<p>La película <b>{row['title']}</b> fue estrenada en el año <b>{row['release_year']}</b> "
                f"con un score/popularidad de <b>{row['popularity']:.2f}</b>.</p>"
            )
        return "\n".join(resultados)
    
    except Exception as e:
        return f"<p>Ocurrió un error inesperado {str(e)}<p>"
    
# def votos_titulo( titulo_de_la_filmación ): 
# Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
# La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
# * Ejemplo de retorno: La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X

def votos_titulo(titulo_usuario):
    try:
        # Capitaliza el input del usuario para que no haya problemas de formato con los títulos del DataFrame
        titulo = titulo_usuario.title() 
        
        # Filtra el DataFrame en busca de filas que calcen con el título del usuario
        respuesta_df = ds.movies_pop_date.loc[ds.movies_pop_date['title'] == titulo, ['title', 'release_year', 'vote_count', 'vote_average']]

        # Chequea si se encontraron filas
        if respuesta_df.empty:
            return "No se encontró ninguna película con ese título."
        
        # Se arma la respuesta para todas las filas encontradas
        resultados = []
        for _, row in respuesta_df.iterrows(): # "_" es usado como placeholder para el index, el cual no necesitaremos
            # Revisa que la cantidad de valoraciones sea mayor a 2000 y agrega la respuesta apropiada a la lista vacia resultados
            if row['vote_count'] < 2000:
                resultados.append(
                    f"La película {row['title']} cuenta con menos de 2000 valoraciones, por lo tanto no se muestran sus valores."
                )
            else:
                # Agrega la respuesta apropiada a la lista vacia resultados solo si la película tiene más de 2000 valoraciones
                resultados.append(
                    f"La película {row['title']} fue estrenada en el año {row['release_year']}. "
                    f"La misma cuenta con un total de {row['vote_count']} valoraciones, con un promedio de {row['vote_average']}."
                )
        # Une y retorna las respuestas separandolas por una nueva línea 
        return "\n".join(resultados)
    
    except Exception as e:
        return f'Ocurrió un error inesperado {str(e)}'
    
# def get_actor( nombre_actor ): 
# Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
# Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
# * Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha conseguido un retorno de X con un promedio de X por filmación

def get_actor(nombre_actor):
    try:
        nombre_actor = nombre_actor.title()

        if nombre_actor in ds.movies_directors['director_name'].tolist():
            return f'{nombre_actor} Es también director. Por favor ingresa otro nombre.'
        elif nombre_actor in ds.movies_actors['actor_name'].tolist():
            filmaciones_sum = ds.movies_actors[ds.movies_actors['actor_name'] == nombre_actor].shape[0]
            merge_df = ds.movies_actors.merge(ds.movies_details, on='movie_id', how='inner')
            retorno_sum = merge_df.loc[merge_df['actor_name'] == nombre_actor, 'return'].sum()
            retorno_avg = merge_df.loc[merge_df['actor_name'] == nombre_actor, 'return'].mean()

            return f'{nombre_actor} ha participado de {filmaciones_sum} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno_sum:.2f} con un promedio de {retorno_avg:.2f} por filmación'
        else:
            return "Por favor introduce un nombre válido"
    except Exception as e:
        return f'Ocurrió un error inesperado {str(e)}'

# def get_director( nombre_director ): 
# Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
# Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

def get_director(nombre_director):
    try:
        # Se normaliza el nombre del director
        nombre_director = nombre_director.title()
        
        # Se obtiene todos los id's de las películas del director
        director_movies_id = ds.movies_directors.loc[ds.movies_directors['director_name'] == nombre_director, "movie_id"]

        # Se hace merge para obtener fechas
        merge_df = ds.movies_details.merge(ds.movies_date, on='movie_id', how='inner')

        # Se filtra el detalle para cada Id
        director_movies_details = merge_df[merge_df['movie_id'].isin(director_movies_id)]

        # Se revisa si el director tiene películas en el dataset
        if director_movies_details.empty:
            return f"No se encontraron películas dirigidas por {nombre_director}."
        
        # Se calcula el "éxito" del director
        total_return = director_movies_details['return'].dropna().sum()

        # Se le da formato a la información de cada película
        resultados = []
        for _, row in director_movies_details.iterrows():
            resultados.append(
                f"<p>Título: <b>{row['title']}</b><br>"
                f"Año de estreno: <b>{row['release_year']}</b><br>"
                f"Revenue: <b>{row['revenue']:,}</b><br>"
                f"Presupuesto: <b>{row['budget']:,}</b><br>"
                f"Retorno: <b>{row['return']:.2f}</b></p>"
            )

        # Se le hace join a los resultados en un string con formato HTML
        return (
            f"<p><b>Éxito total del director {nombre_director}: {total_return:.2f}</b></p>"
            + "".join(resultados)
        )
    
    except Exception as e:
        return f'<p>Ocurrió un error inesperado {str(e)}</p>'