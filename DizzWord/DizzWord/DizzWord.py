import reflex as rx
import reflex_chakra as rc
from DizzWord.styles import styles

from rxconfig import config

from DizzWord.pages.index import index
from DizzWord.pages.about import about


class State(rx.State):
    """The app state."""



app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
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

