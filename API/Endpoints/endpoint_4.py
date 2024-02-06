# endpoint_4.py

import pandas as pd

def best_developer_year(dataframe: pd.DataFrame, anio: int):
    """
    Obtiene el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.

    Parameters:
    - dataframe (DataFrame): El DataFrame que contiene los datos de los juegos y las reviews.
    - año (int): El año para el que se desea obtener el top 3 de desarrolladores.

    Returns:
    - list: Una lista de diccionarios con el puesto y el nombre de los desarrolladores más recomendados.
            Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    """
    # Filtrar el DataFrame por el año dado
    df_year = dataframe[dataframe['year'] == anio]

    # Obtener los 3 mejores desarrolladores para el año dado
    top_developers = df_year.groupby('developer')['recommend_score'].sum().nlargest(3)

    # Crear la lista de salida
    output_list = []
    for puesto, (developer, score) in enumerate(top_developers.items(), start=1):
        output_list.append({f'Puesto {puesto}': developer})

    return output_list
