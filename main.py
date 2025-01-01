from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse 
from funciones import cantidad_filmaciones_mes, cantidad_filmaciones_dia, score_titulo, votos_titulo, get_actor, get_director, recomendacion

# TO-DO: 
# Informe EDA.
# Hacer video.
# BONUS: 
#       LISTO -->* Nube de palabras títulos de películas.
#       LISTO -->* Función votos_titulo devuelve solo una linea si respuesta consta de dos lineas. 
# LISTO --> Hacer readme.
# LISTO --> Hacer las 2 funciones faltantes.
# LISTO --> Hacer páginas de las funciones faltantes en la API.
# LISTO --> * Corregir funcionamiento funciones, solo la primera funciona.
# LISTO --> * Implementar boton home.
# LISTO --> Hacer el modelo de recomendación.
# LISTO --> Hacer endopoint de modelo.


# Crea unas instancia de la aplicación
app = FastAPI()

# Página principal
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Sistema de Recomendación de Películas</h1>
            <ul>
                <li><a href="/cantidad-filmaciones-mes">Películas estrenadas por mes</a></li>
                <li><a href="/cantidad-filmaciones-dia">Películas estrenadas por día</a></li>
                <li><a href="/score-titulo">Score/popularidad de una película</a></li>
                <li><a href="/votos-titulo">Votos de una película</a></li>
                <li><a href="/get_actor">Get Actor</a></li>
                <li><a href="/get_director">Get Director</a></li>
                <li><a href="/recomendacion">Recomendación</a></li>
            </ul>
        </body>
    </html>
    """

# Página para cantidad de filmaciones por mes
@app.get("/cantidad-filmaciones-mes", response_class=HTMLResponse)
def form_cantidad_filmaciones_mes():
    return """
    <html>
        <body>
            <h1>Cantidad de películas por mes</h1>
            <form action="/cantidad-filmaciones-mes" method="post">
                <label for="mes">Escribe un mes en español:</label><br>
                <input type="text" id="mes" name="mes" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/cantidad-filmaciones-mes", response_class=HTMLResponse)
def resultado_cantidad_filmaciones_mes(mes: str = Form(...)):
    resultado = cantidad_filmaciones_mes(mes)
    return f"""
    <html>
        <body>
            <h1>Resultado</h1>
            <p>{resultado}</p>
            <button type="button" onclick="window.location.href='/cantidad-filmaciones-mes'">Atrás</button> <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """

# Página para cantidad de filmaciones por día
@app.get("/cantidad-filmaciones-dia", response_class=HTMLResponse)
def form_cantidad_filmaciones_dia():
    return """
    <html>
        <body>
            <h1>Cantidad de películas por día</h1>
            <form action="/cantidad-filmaciones-dia" method="post">
                <label for="dia">Escribe un día en español:</label><br>
                <input type="text" id="dia" name="dia" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/cantidad-filmaciones-dia", response_class=HTMLResponse)
def resultado_cantidad_filmaciones_dia(dia: str = Form(...)):
    resultado = cantidad_filmaciones_dia(dia)
    return f"""
    <html>
        <body>
            <h1>Resultado</h1>
            <p>{resultado}</p>
            <button type="button" onclick="window.location.href='/cantidad-filmaciones-dia'">Atrás</button> <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """

# Página para score de una película
@app.get("/score-titulo", response_class=HTMLResponse)
def form_score_titulo():
    return """
    <html>
        <body>
            <h1>Score de una película</h1>
            <form action="/score-titulo" method="post">
                <label for="titulo">Escribe el título:</label><br>
                <input type="text" id="titulo" name="titulo" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/score-titulo", response_class=HTMLResponse)
def resultado_score_titulo(titulo: str = Form(...)):
    resultado = score_titulo(titulo)
    return f"""
    <html>
        <body>
            <h1>Resultado</h1>
            {resultado}
            <button type="button" onclick="window.location.href='/score-titulo'">Atrás</button>
            <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """

# Página para votos de una película
@app.get("/votos-titulo", response_class=HTMLResponse)
def form_votos_titulo():
    return """
    <html>
        <body>
            <h1>Votos y promedio de una película</h1>
            <form action="/votos-titulo" method="post">
                <label for="titulo">Escribe el título:</label><br>
                <input type="text" id="titulo" name="titulo" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/votos-titulo", response_class=HTMLResponse)
def resultado_votos_titulo(titulo: str = Form(...)):
    resultado = votos_titulo(titulo)
    return f"""
    <html>
        <body>
            <h1>Resultado</h1>
            <p>{resultado}</p>
            <button type="button" onclick="window.location.href='/votos-titulo'">Atrás</button> <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """

# Página para get_actor
@app.get("/get_actor", response_class=HTMLResponse)
def from_get_actor():
    return '''
    <html>
        <body>
            <h1>Get Actor</h1>
            <form action="/get_actor" method="post">
                <label for="actor">Escribe el nombre de un actor:<label><br>
                <input type="text" id="actor" name="actor" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
'''

@app.post("/get_actor", response_class=HTMLResponse)
def resultado_get_actor(actor: str = Form(...)):
    resultado = get_actor(actor)
    return f'''
    <html>
        <body>
            <h1>Resultado</h1>
            <p>{resultado}</p>
            <button type="button" onclick="window.location.href='/get_actor'">Atrás</button> <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    '''

# Página para get_director
@app.get("/get_director", response_class=HTMLResponse)
def form_get_director():
    return """
    <html>
        <body>
            <h1>Películas de un director</h1>
            <form action="/get_director" method="post">
                <label for="nombre_director">Escribe el nombre del director:</label><br>
                <input type="text" id="nombre_director" name="nombre_director" required><br>
                <button type="submit">Enviar</button> <button type="button" onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/get_director", response_class=HTMLResponse)
def resultado_get_director(nombre_director: str = Form(...)):
    resultado = get_director(nombre_director)
    return f"""
    <html>
        <body>
            <h1>Resultado</h1>
            {resultado}
            <button type="button" onclick="window.location.href='/get_director'">Atrás</button> <button type="button" onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """
# Página para recomendación
@app.get("/recomendacion", response_class=HTMLResponse)
def form_recomendacion():
    return """
    <html>
        <body>
            <h1>Recomendador de Películas</h1>
            <form action="/recomendacion" method="post">
                <label for="titulo">Escribe el título de una película:</label><br>
                <input type="text" id="titulo" name="titulo" required><br>
                <button type="submit">Enviar</button> <button onclick="window.location.href='/'">Home</button>
            </form>
        </body>
    </html>
    """

@app.post("/recomendacion", response_class=HTMLResponse)
def resultado_recomendacion(titulo: str = Form(...)):
    # Llamamos a la función recomendacion
    resultado = recomendacion(titulo)

    # Formateamos la respuesta en HTML
    return f"""
    <html>
        <body>
            <h1>Recomendaciones para "{titulo}"</h1>
            <pre>{resultado}</pre> <!-- Se usa <pre> para mostrar el texto con formato -->
            <button onclick="window.location.href='/recomendacion'">Atrás</button> <button onclick="window.location.href='/'">Home</button>
        </body>
    </html>
    """