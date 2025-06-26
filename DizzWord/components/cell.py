import reflex as rx
import reflex_chakra as rc
from DizzWord.styles import styles

def cell() -> rx.Component:
    return rx.input(
        max_length=1,
        width="30px",
        style=styles.cell_style

    )