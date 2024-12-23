from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse 
import funciones

# Crea unas instancia de la aplicación
app = FastAPI()

# Ruta principal con formulario HTML
@app.get("/", response_class=HTMLResponse)
def leer_formulario():
    html_content = '''
    <html>
        <head>
            <title>Consulta de Películas</title>
        </head>
        <body>
            <h1>Consulta la cantidad de palículas por mes</h1>
            <form action="cantidad-filmaciones" method="post">
                <label for= "mes">Escribe un mes en español:</label><br><br>
                <input type="text" id="mes" name="mes"><br><br>
                <input type="submit" value="Enviar">            
            </from>
        </body>
    </html>
    '''
    return HTMLResponse(content=html_content)

# Endpoint para recibir datos del formulario
@app.post('/cantidad-filmaciones')
def procesar_formulario(mes: str = Form(...)):
    resultado = funciones.cantidad_filmaciones_mes(mes)
    return {"resultado": resultado}