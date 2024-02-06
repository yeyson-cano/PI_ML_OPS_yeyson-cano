# main.py

from fastapi import FastAPI, HTTPException
import pandas as pd
import traceback

# Importar los datasets para cada endpoint
df_ep1 = pd.read_parquet('../Data/Processed/API_data/ep1.parquet')
df_ep2 = pd.read_parquet('../Data/Processed/API_data/ep2.parquet')
df_ep3 = pd.read_parquet('../Data/Processed/API_data/ep3.parquet')
df_ep4 = pd.read_parquet('../Data/Processed/API_data/ep4.parquet')
df_ep5 = pd.read_parquet('../Data/Processed/API_data/ep5.parquet')

# Importar los módulos de los endpoints
from API.Endpoints import endpoint_1, endpoint_2, endpoint_3, endpoint_4, endpoint_5

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir las rutas para los distintos endpoints

@app.get("/developer")
async def developer(desarrollador: str):
    try:
        # Comprobar si el desarrollador está especificado
        if not desarrollador or not desarrollador.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'desarrollador' no puede ser nulo o estar vacío.")
        
        return endpoint_1.developer(df_ep1, desarrollador)
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/userdata")
async def userdata(User_id: str):
    try:
        # Comprobar si el ID de usuario está especificado
        if not User_id or not User_id.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'User_id' no puede ser nulo o estar vacío.")
        
        return endpoint_2.userdata(df_ep2, User_id)
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/UserForGenre")
async def usergenre(genero: str):
    try:
        # Comprobar si el género está especificado
        if not genero or not genero.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'genero' no puede ser nulo o estar vacío.")
        
        return endpoint_3.UserForGenre(df_ep3, genero)
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/best_developer_year")
async def bestdeveloper(year: int):
    try:
        # Comprobar si el año está especificado
        if not year:
            raise HTTPException(status_code=422, detail="El parámetro 'year' no puede ser nulo.")
        
        return endpoint_4.best_developer_year(df_ep4, year)
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/developer_reviews_analysis")
async def developerreviews(desarrolladora: str):
    try:
        # Comprobar si el nombre del desarrollador está especificado
        if not desarrolladora or not desarrolladora.strip():
            raise HTTPException(status_code=422, detail="El parámetro 'desarrolladora' no puede ser nulo o estar vacío.")
        
        return endpoint_5.developer_reviews_analysis(df_ep5, desarrolladora)
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
