import reflex as rx
from web_reflex.styles.styles import Size as Size
from web_reflex.styles.colors import Color as Color
import web_reflex.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "alexhDev",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            style=styles.navbar_title_style
            
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )