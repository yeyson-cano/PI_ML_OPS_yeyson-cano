# endpoint_5.py

import pandas as pd

def developer_reviews_analysis(dataframe: pd.DataFrame, desarrolladora: str):
    """
    Realiza un análisis de las reseñas de un desarrollador específico.

    Parameters:
    - dataframe (DataFrame): El DataFrame que contiene los datos de las reseñas.
    - desarrolladora (str): El nombre del desarrollador a analizar.

    Returns:
    - dict: Un diccionario con el nombre del desarrollador como llave y una lista
            con la cantidad total de registros de reseñas de usuarios categorizados
            con un análisis de sentimiento como valor positivo o negativo.
            Ejemplo de retorno: {'Valve': {'Negative': 182, 'Positive': 278}}
    """
    # Filtrar el DataFrame para obtener las reseñas del desarrollador especificado
    desarrolladora_df = dataframe[dataframe['developer'] == desarrolladora]

    # Calcular la cantidad total de registros de reseñas positivas y negativas
    total_positivas = desarrolladora_df['positive_reviews'].sum()
    total_negativas = desarrolladora_df['negative_reviews'].sum()

    # Crear el diccionario de resultados
    resultado = {desarrolladora: {'Positive': total_positivas, 'Negative': total_negativas}}

    return resultado
