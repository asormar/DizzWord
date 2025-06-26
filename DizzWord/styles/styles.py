from enum import Enum
import reflex as rx
import reflex_chakra as rc

from .font import Font as Font
from .font import FontWeight as FontWeight

class Size(Enum):
    S="0.5em"
    M="1em"
    D="1.5em"
    L="2em"
    XL="4em"

STYLESHEETS= [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=WDXL+Lubrifont+TC&display=swap",
    "https://fonts.googleapis.com/css2?family=Coiny&display=swap"
]

BASE_STYLE={
    "background_color":"white",
    "font_family":Font.DEFAULT,
    "font_weight":FontWeight.LIGHT,

    rx.input:{
        ":focus":{"border": "3px solid", "background-color": "lightblue" }
    }
}

cell_style= {
    "input:focus": {
        "border": "3px solid",
    }
}