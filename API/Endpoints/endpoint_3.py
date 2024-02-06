# endpoint_3.py

import pandas as pd

def UserForGenre(dataframe: pd.DataFrame, genero: str):
    """
    Devuelve el usuario que acumula más horas jugadas para el género dado
    y una lista de la acumulación de horas jugadas por año de lanzamiento.

    Parameters:
    - dataframe (DataFrame): El DataFrame que contiene los datos de los juegos.
    - genero (str): El género para el que se desea obtener la información.

    Returns:
    - dict: Un diccionario con el usuario que acumula más horas jugadas para el género dado
            y una lista de la acumulación de horas jugadas por año.
            Ejemplo de retorno: {
                "Usuario con más horas jugadas para Género X": user_id,
                "Horas jugadas": [{"Año": 2010, "Horas": 300}, {"Año": 2011, "Horas": 500}]
            }
    """
    # Filtrar el DataFrame por el género deseado
    df_genero = dataframe[dataframe['genre'] == genero]

    # Verificar si no hay datos para el género dado
    if df_genero.empty:
        return f"No hay datos disponibles para el género '{genero}'"

    # Encontrar el usuario con más horas jugadas para el género dado
    usuario_con_mas_horas = df_genero.groupby('user_id')['hours_year'].sum().idxmax()

    # Calcular las horas jugadas por año para el usuario encontrado
    horas_por_anio = df_genero[df_genero['user_id'] == usuario_con_mas_horas].groupby('year')['hours_year'].sum()

    # Crear el diccionario de salida
    output_dict = {
        "Usuario con más horas jugadas para Género X": usuario_con_mas_horas,
        "Horas jugadas": [{"Año": anio, "Horas": horas} for anio, horas in horas_por_anio.items()]
    }

    return output_dict
