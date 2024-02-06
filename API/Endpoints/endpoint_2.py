# endpoint_2.py

import pandas as pd

def userdata(df: pd.DataFrame, user_id: str):
    """
    Retorna la cantidad de dinero gastado por el usuario, el porcentaje de recomendación
    basado en las revisiones y la cantidad de items para el usuario dado.
    
    Args:
    - df (pandas.DataFrame): El DataFrame que contiene los datos.
    - user_id (str): El ID del usuario para el cual se desea obtener la información.
    
    Returns:
    - dict: Un diccionario con la información del usuario.
    """
    user_data = {}
    
    # Filtrar los datos del usuario dado
    user_data['User_id'] = user_id
    user_info = df[df['user_id'] == user_id]
    
    # Calcular la cantidad de dinero gastado por el usuario
    amount_spent = user_info['amount'].sum()
    user_data['Dinero gastado'] = f"${amount_spent}"
    
    # Calcular el porcentaje de recomendación
    recommendation_percentage = user_info['recommendation_percentage'].iloc[0]  # asumiendo que es el mismo para todos los registros del usuario
    user_data['% de recomendación'] = f"{recommendation_percentage}%"
    
    # Calcular la cantidad de items del usuario
    items_count = user_info['items_count'].iloc[0]  # asumiendo que es el mismo para todos los registros del usuario
    user_data['cantidad de items'] = items_count
    
    return user_data
