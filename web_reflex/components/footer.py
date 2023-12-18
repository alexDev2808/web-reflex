import reflex as rx
import datetime
from web_reflex.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            f"@ 2022-{datetime.date.today().year} alexhDev2808 by J. Alexis V1.",
            href="https://twitter.com/Alexh1230",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            " Construido con ❤️ de Mexico para el mundo.",
            font_size=Size.MEDIUM.value
        ),
        margin_bottom=Size.BIG.value,
        bottom="0"
    )