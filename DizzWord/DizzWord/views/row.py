import reflex as rx
import reflex_chakra as rc
from DizzWord.components.cell import cell

def row() -> rx.Component:
    return rc.hstack(
        cell(),
        cell(),
        cell(),
        cell(),
        cell()
    )