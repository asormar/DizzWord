from rxconfig import config

import reflex as rx
import reflex_chakra as rc
from DizzWord.views.header import header
from DizzWord.views.row import row
from DizzWord.styles import styles
from DizzWord.components.cell import cell
from DizzWord.views.routes import Route

@rx.page(
        route=Route.ABOUT
)


def about() -> rx.Component:
    return rc.vstack(
        rx.text("ABOUT ME")
    )