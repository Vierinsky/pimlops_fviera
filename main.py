from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse 
from funciones import cantidad_filmaciones_mes, cantidad_filmaciones_dia, score_titulo, votos_titulo

# Crea unas instancia de la aplicación
app = FastAPI()

# Ruta principal con formulario HTML
@app.get("/", response_class=HTMLResponse)
def home():
    html_content = '''
    <html>
        <head>
            <title>Consulta de Películas</title>
            <script>
                async function enviarFormulario(endpoint, formId, resultId) {
                    const form = document.getElementById(formId);
                    const formData = new FormData(form);
                    try {
                        const reponse = await fetch(enpoint, {
                            method: "POST",
                            body: formData
                        });

                        if (!response.ok) {
                            document.getElementaryById(resultId).innerText = "Error en el servidor.";
                            return;
                        }
                        const data = await response.json();
                        document.getElementById(resultId).innerText = data.resultado;
                    } catch (error) {
                        console.error("Error en el envío del formulario:", error);
                        document.getElementById(resultId).innerText = "Error en la conexión.";
                    }
                }
            </script>
        </head>
        <body>
            <h1>Consulta la cantidad de palículas por mes</h1>

            <!-- Formulario para cantidad_filmaciones_mes -->
            <h2>Cantidad de palículas por mes</h2>
            <form id="form_mes" onsubmit="event.preventDefault(); enviarFormulario('/cantidad-filmaciones-mes', 'form_mes', 'result_mes')">
                <label for="mes">Escribe un mes en español:</label>
                <input type="text" id="mes" name="mes" required>
                <button type="submit">Enviar</button>            
            </from>
            <p id="result_mes"></p>

            <!-- Formulario para cantidad_filmaciones_dia -->
            <h2>Cantidad de películas por día</h2>
            <form id="form_dia" onsubmit="event.preventDefault(); enviarFormulario('/cantidad-filmaciones-dia', 'form_dia', 'result_dia')">
                <label for="dia">Escribe un día:</label>
                <input type="text" id="dia" name="dia" required>
                <button type="submit">Enviar</button>
            </form>
            <p id="result_dia"></p>

            <!-- Formulario para score_titulo -->
            <h2>Score de una película</h2>
            <form id="form_score" onsubmit="event.preventDefault(); enviarFormulario('/score-titulo', 'form_score', 'result_score')">
                <label for="titulo">Escribe el título:</label>
                <input type="text" id="titulo" name="titulo" required>
                <button type="submit">Enviar</button>
            </form>
            <p id="result_score"></p>

            <!-- Formulario para votos_titulo -->
            <h2>Votos y promedio de una película</h2>
            <form id="form_votos" onsubmit="event.preventDefault(); enviarFormulario('/votos-titulo', 'form_votos', 'result_votos')">
                <label for="titulo_votos">Escribe el título:</label>
                <input type="text" id="titulo_votos" name="titulo" required>
                <button type="submit">Enviar</button>
            </form>
            <p id="result_votos"></p>
        </body>
    </html>
    '''
    return HTMLResponse(content=html_content)

# Endpoints para recibir datos del formulario
@app.post('/cantidad-filmaciones-mes')
def cantidad_filmaciones_mes_endpoint(mes: str = Form(...)):
    resultado = cantidad_filmaciones_mes(mes)
    return {"resultado": resultado}

@app.post("/catindad-filmaciones-dia")
def cantidad_filmaciones_dia_endpoint(dia: str = Form(...)):
    resultado = cantidad_filmaciones_dia(dia)
    return {"reslutado" : resultado}

@app.post("/score-titulo")
def score_titulo_endpoint(titulo: str = Form(...)):
    resultado = score_titulo(titulo)
    return {"resultado": resultado}

@app.post("/votos_titlo")
def votos_titulo_endpoint(titulo: str = Form(...)):
    resultado = votos_titulo(titulo)
    return {"resultado": resultado}