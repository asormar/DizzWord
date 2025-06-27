import reflex as rx
import reflex_chakra as rc
from DizzWord.styles import styles

from rxconfig import config

from DizzWord.pages.index import index
from DizzWord.pages.about import about

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from DizzWord.api.api import hello


# Create a FastAPI app
fastapi_app = FastAPI(title="My API")

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    api_transformer=fastapi_app # Create a Reflex app with the FastAPI app as the API transformer
)



#META-TAGS
title= "DizzWord | Comienza el reto de las palabras random"
description="Esto es una página inspirada en el juego Wordle pero con alguna variación para hacerlo más interesante"
preview= "logo.png" #Cuando lanze la web poner aquí la url

app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name":"og.type","content":"website"},
        {"name":"og.title","content":title},
        {"name":"og.description","content":description},
        {"name":"og.image","content":preview},
        {"name":"twitter:card","content":"summary_large_image"},
        {"name":"twitter:side","content":"@asormar"}
    ]
    )

app.add_page(
    about,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name":"og.type","content":"website"},
        {"name":"og.title","content":title},
        {"name":"og.description","content":description},
        {"name":"og.image","content":preview},
        {"name":"twitter:card","content":"summary_large_image"},
        {"name":"twitter:side","content":"@asormar"}
    ]
    )


fastapi_app.add_api_route("/hello", hello)