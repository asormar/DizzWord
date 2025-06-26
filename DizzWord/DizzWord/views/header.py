import reflex as rx
import reflex_chakra as rc
from DizzWord.styles.styles import Size

def header() -> rx.Component:
    return rc.vstack(
        rc.text(
            "DizzWord",
            font_size=Size.D
        ),
        
        rx.image(
            src="roll2.gif",
            width="60px",
        ),
        
        margin_top=Size.M
    )