from fastapi import FastAPI
import funciones 

# Crea unas instancia de la aplicación
app = FastAPI()

# Ruta raíz (GET /)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Función cantidad de filmaciones por mes
@app.get('/filmaciones-mes')
def obtener_fimalciones_mes(mes: str):
    '''
    Endpoint que devuelve la cantidad de películas estrenadas en un mes específico.
    - 'mes': Nombre del mes en español (string)
    '''
    resultado = funciones.cantidad_filmaciones_mes(mes)
    return resultado