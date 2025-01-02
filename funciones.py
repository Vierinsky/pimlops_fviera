import datasets as ds
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors


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
        return f"<p>Ocurrió un error inesperado {str(e)}</p>"
    
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
                    f"<p>La película <b>{row['title']}</b> cuenta con <b>menos de 2000 valoraciones</b>, por lo tanto <b>no</b> se muestran sus valores.</p>"
                )
            else:
                # Agrega la respuesta apropiada a la lista vacia resultados solo si la película tiene más de 2000 valoraciones
                resultados.append(
                    f"<p>La película <b>{row['title']}</b> fue estrenada en el año <b>{row['release_year']}</b>. "
                    f"La misma cuenta con un total de <b>{row['vote_count']}</b> valoraciones, con un promedio de <b>{row['vote_average']}</b>.</p>"
                )
        # Une y retorna las respuestas separandolas por una nueva línea 
        return "\n".join(resultados)
    
    except Exception as e:
        return f'<p>Ocurrió un error inesperado {str(e)}</p>'
    
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

            return f'<b>{nombre_actor}</b> ha participado de <b>{filmaciones_sum}</b> cantidad de filmaciones, el mismo ha conseguido un retorno de <b>{retorno_sum}</b> con un promedio de <b>{retorno_avg}/<b> por filmación.'
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
            return f"No se encontraron películas dirigidas por <b>{nombre_director}.</b><br>"
        
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
    
# def recomendacion( titulo ): 
#   Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores

# Se normalizan datos númericos continuos para que todos contribuyan al modelo de manera equitativa
# Se inicializa el escalador
scaler = MinMaxScaler()

# Se seleccionan los datos númericos
columnas_numericas = ['budget', 'popularity', 'revenue', 'release_year', 'return']

# Se normaliza las columnas
# fit_transform calcula valores minimo y máximo de cada columna y las escala según corresponda
ds.movies_ml[columnas_numericas] = scaler.fit_transform(ds.movies_ml[columnas_numericas])

# Se crea una matriz de características
#   * La cual es un array 2D en el que cada fila representa una película 
#     y cada columna representa una característica.
# La similitud será calculada comparando filas de esta matriz

caracteristicas_columnas = [
    'budget', 'popularity', 'revenue', 'release_year', 'return',
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
    'African Languages', 'Asian Languages',
    'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America' 
]

# .values convierte este subset del dataframe en un Numpy array 
# que será usado en rápidas operaciones numéricas
matriz_caracteristicas = ds.movies_ml[caracteristicas_columnas].values

# Se disminuye el peso de las columnas binarias

columnas_binarias = [
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
    'Documentary', 'Drama', 'Family', 'Fantasy', 'Foreign',
    'History', 'Horror', 'Music', 'Mystery', 'Romance',
    'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western',
    'African Languages', 'Asian Languages', 'Germanic Languages',
    'Other Languages', 'Romance Languages', 'Slavic Languages',
    'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'
]

# Se filtra columnas_binarias para incluir solo las que esten presentes en matriz_caracteristicas
columnas_presentes = [col for col in columnas_binarias if col in caracteristicas_columnas]

# Se obtienen indices de las columnas binarias
indices_binarias = [caracteristicas_columnas.index(col) for col in columnas_presentes]

# Se escalan las columnas binarias en matriz_caracteristicas
matriz_caracteristicas[:, indices_binarias] *= 0.3

# Se reduce dimensionalidad con PCA

# Se reduce la dimensionalidad a 10 componentes
pca = PCA(n_components=10)
reduced_features = pca.fit_transform(matriz_caracteristicas)

matriz_caracteristicas = reduced_features

# Se hace fit a los vecinos más cercanos usando la similitud coseno
# Usando una busqueda "brute force" para mantener la simplicidad
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(matriz_caracteristicas)

def recomendacion(titulo, n_neighbors=5):
    try:
        # Normalizamos el título para que coincida con el dataset
        titulo = titulo.title()
        
        # Buscamos el índice de la película ingresada
        movie_index = ds.movies_ml_details[ds.movies_ml_details['title'] == titulo].index[0]

        # Calculamos las distancias e índices de las películas similares
        distancias, indices = model.kneighbors([matriz_caracteristicas[movie_index]], n_neighbors=n_neighbors+1)

        # Excluimos la película ingresada por el usuario (primer resultado es siempre la misma película)
        similar_movies = indices[0][1:]
        similar_distances = distancias[0][1:]

        # Obtenemos los detalles de las películas similares
        recomendaciones = ds.movies_ml_details.iloc[similar_movies][['title', 'popularity', 'release_year']].copy()
        recomendaciones['similarity_score'] = 1 - similar_distances  # Convertimos la distancia en puntaje de similitud

        # Formateamos las recomendaciones como una lista de texto
        resultados = []
        for _, row in recomendaciones.iterrows():
            resultados.append(
                f"Película: {row['title']} | Año: {row['release_year']} | Popularidad: {row['popularity']:.2f} | Similitud: {row['similarity_score']:.2f}"
            )
        return "\n".join(resultados)  # Devolvemos como texto separado por líneas
    except IndexError:
        return f"No se encontró una película con el título: <b>{titulo}</b>"
    except Exception as e:
        return f"Ha ocurrido un error: {str(e)}"
