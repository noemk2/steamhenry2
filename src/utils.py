import pandas as pd
import numpy as np
import os
from datetime import datetime

def userdata(user_id):
    # df = pd.read_csv(file_path("userdata", "userdata.csv"))
    # # user_data = df[df['user_id'] == user_id]
    # user_data = df.loc[df['user_id'] == user_id]
    # print(user_data)

    # if not user_data.empty:
    #     total_price = user_data['total_price'].values[0]
    #     recomendation_porcent = user_data['recomendation_porcent'].values[0]
    #     item_count = user_data['item_count'].values[0]

    #     print(total_price, recomendation_porcent, item_count)

    #     return total_price, recomendation_porcent, item_count

    # else:
    #     return None
    user_data_dict = load_user_data(file_path("userdata", "userdata.csv"))
    print(user_data_dict[user_id])

    if user_id in user_data_dict:
        total_price, recomendation_porcent, item_count = user_data_dict[user_id]
        print(total_price, recomendation_porcent, item_count)
        return total_price, recomendation_porcent, item_count
    else:
        return None

    # return {"user_id": user_id}


def countre_views(fechas):
    print(fechas)
    fechas = fechas.split(' y ')
    fecha1 = fechas[0]
    fecha2 = fechas[1]

    df = pd.read_csv(file_path("counterviews", "countreviews.csv"))
    df['date'] = pd.to_datetime(df['date'])

    start_date = fecha1
    end_date = fecha2

    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    total_users = len(filtered_df['user_id'])
    recommend_true = filtered_df['recommend'].sum()
    recommend_false = total_users - recommend_true

    percentage_recommend = (recommend_true / total_users) * 100

    print(f"Cantidad de usuarios que realizaron revisiones: {total_users}")
    print(f"Porcentaje de recomendación: {percentage_recommend:.2f}%")

    return {"Cantidad de usuarios que realizaron revisiones": total_users,
            "Porcentaje de recomendacion": percentage_recommend
            }


def gen_re(genero):
    df = pd.read_csv(file_path("genre", "genre.csv"))
    df['genre_list'] = df['genres'].apply(
        lambda x: [genre.strip(" '[]") for genre in x.split(',')])
    genre_playtime = {}
    for index, row in df.iterrows():
        play_time = row['play_time']
        for genre in row['genre_list']:
            if genre in genre_playtime:
                genre_playtime[genre] += play_time
            else:
                genre_playtime[genre] = play_time

    sorted_genre_playtime = dict(
        sorted(genre_playtime.items(), key=lambda x: x[1], reverse=True))

    genre_rank = list(sorted_genre_playtime.keys()).index(
        genero) + 1 if genero in sorted_genre_playtime else None

    # print(genre_rank)
    return {f"genre_rank of {genero} ": genre_rank}

    # Ejemplo de uso:
    # genero_buscar = "Action"  # Reemplaza esto con el género que deseas buscar
    # rank = genre(genero_buscar, df)
    # if rank is not None:
    #     print(
    #         f"'{genero_buscar}' está en el puesto {rank} en el ranking de géneros.")
    # else:
    #     print(f"'{genero_buscar}' no se encuentra en el DataFrame.")

    # return {"user_id": user_id}


def user_forgenre(user_id: str):
    df = pd.read_csv(file_path("userforgenre", "userforgenre.csv"))
    filtered_df = df[df['genres'].apply(lambda x: genre in x)]
    sorted_df = filtered_df.sort_values(by='play_time', ascending=False)
    top_5_users = sorted_df.head(5)
    print(top_5_users[['user_id', 'play_time', 'user_url']])

    return top_5_users[['user_id', 'play_time', 'user_url']]

    # Ejemplo de uso
    # genre = 'Action'
    # result = userforgenre(genre)
    # print(result)

    # return {"user_id": user_id}


def dev_eloper(developer):

    df = pd.read_csv(file_path("developer", "developer1.csv"))

    # Filtrar por developer
    # Asegúrate de copiar el DataFrame
    filtered_df = df[df['developer'] == developer].copy()

    # Modificar las columnas
    filtered_df['price'] = pd.to_numeric(filtered_df['price'], errors='coerce')
    filtered_df['release_date'] = pd.to_datetime(
        filtered_df['release_date'], errors='coerce')  # Convierte 'release_date' a datetime
    filtered_df['year'] = filtered_df['release_date'].dt.year

    # Calcular el porcentaje gratuito
    filtered_df['free_percentage'] = (filtered_df['price'] == 0).mean() * 100


    item_counts = filtered_df['year'].value_counts().reset_index()
    item_counts.columns = ['year', 'item_count']
    year = int(item_counts['year'])
    item = int(item_counts['item_count'])

    # print( item)
    return {"year": year, "items": item}


def sentimentanalysis(year):

    df = pd.read_csv(file_path("sentiment_analysis", "senti.csv"))

    df = df[df['release_date'].str.match(r'\d{4}-\d{2}-\d{2}', na=False)]

    df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')

    # print(df.head())

    filtered_df = df[df['release_date'].dt.year == int(year)]

    sentiment_counts = filtered_df['sentiment_analysis'].value_counts(
    ).to_dict()

    sentiment_result = {
        'Negative': sentiment_counts.get(0, 0),
        'Neutral': sentiment_counts.get(1, 0),
        'Positive': sentiment_counts.get(2, 0)
    }

    # print(sentiment_result)
    return sentiment_result

    # # Ejemplo de uso
    # year = 2009
    # result = sentiment_analysis(year)
    # print(result)

    # return {"user_id": user_id}


def file_path(dir_name, file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "dataset", dir_name, file_name)


def clean_and_lower(input_str):
    # Eliminar espacios en blanco y convertir a minúsculas
    cleaned_str = input_str.strip().lower()
    return cleaned_str


def load_user_data(file_path):
    df = pd.read_csv(file_path)
    user_data_dict = {}

    for index, row in df.iterrows():
        user_id = str(row['user_id'])
        total_price = row['total_price']
        recomendation_porcent = row['recomendation_porcent']
        item_count = row['item_count']

        user_data_dict[user_id] = (
            total_price, recomendation_porcent, item_count)

    return user_data_dict
