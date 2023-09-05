from typing import Union
from fastapi import FastAPI
from src.utils import userdata, countre_views, gen_re, user_forgenre, dev_eloper, sentimentanalysis

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# API : steam


@app.get("/userdata/{user_id}")
def user_data(user_id):
    return userdata(user_id)


@app.get("/countreviews/{fechas}")
def countreviews(fechas):
    return countre_views(fechas)


@app.get("/genre/{genero}")
def genre(genero):
    return gen_re(genero)


@app.get("/userforgenre/{genero}")
def userforgenre(genero):
    return user_forgenre(genero)


@app.get("/developer/{desarrollador}")
def developer(desarrollador):
    return dev_eloper(desarrollador)


@app.get("/sentiment_analysis/{ano}")
def sentiment_analysis(ano):
    return sentimentanalysis(ano)
