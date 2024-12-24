from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse 
from funciones import cantidad_filmaciones_mes, cantidad_filmaciones_dia, score_titulo, votos_titulo

# Crea unas instancia de la aplicación
app = FastAPI()

# Página principal
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Bienvenido a la API de Películas</h1>
            <ul>
                <li><a href="/cantidad-filmaciones-mes">Cantidad de películas por mes</a></li>
                <li><a href="/cantidad-filmaciones-dia">Cantidad de películas por día</a></li>
                <li><a href="/score-titulo">Score de una película</a></li>
                <li><a href="/votos-titulo">Votos y promedio de una película</a></li>
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
                <button type="submit">Enviar</button>
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
            <a href="/cantidad-filmaciones-mes">Volver</a>
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
                <button type="submit">Enviar</button>
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
            <a href="/cantidad-filmaciones-dia">Volver</a>
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
                <button type="submit">Enviar</button>
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
            <p>{resultado}</p>
            <a href="/score-titulo">Volver</a>
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
                <button type="submit">Enviar</button>
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
            <a href="/votos-titulo">Volver</a>
        </body>
    </html>
    """