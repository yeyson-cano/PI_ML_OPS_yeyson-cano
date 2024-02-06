# endpoint_1.py

import pandas as pd

def developer(df: pd.DataFrame, desarrollador: str):
    """
    Retorna la cantidad de items y porcentaje de contenido gratuito por año según empresa desarrolladora.

    Args:
    - df (pandas.DataFrame): El DataFrame que contiene los datos.
    - desarrollador (str): El nombre del desarrollador para el cual se desea obtener la información.

    Returns:
    - dict: Un diccionario con la información del desarrollador.
    """
    retorno = {}
    
    # Filtrar los datos por el desarrollador dado
    df_desarrollador = df[df['developer'] == desarrollador]

    # Agrupar por desarrollador y año, contar la cantidad de items desarrollados y gratuitos
    items_por_año = df_desarrollador.groupby('year').agg(
        items_per_year=('item_count', 'sum'),
        free_content_per_year=('free_content_percentage', 'mean')
    ).reset_index()

    # Convertir el porcentaje de contenido gratuito a formato de cadena con símbolo de porcentaje
    items_por_año['free_content_per_year'] = items_por_año['free_content_per_year'].apply(lambda x: f"{x:.0f}%")

    # Crear el diccionario de retorno
    retorno = {
        "developer": desarrollador,
        "items_per_year": dict(zip(items_por_año['year'].astype(str), items_por_año['items_per_year'])),
        "free_content_per_year": dict(zip(items_por_año['year'].astype(str), items_por_año['free_content_per_year']))
    }

    return retorno
