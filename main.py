from fastapi import FastAPI 

# Crea unas instancia de la aplicación
app = FastAPI()

# Ruta raíz (GET /)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}