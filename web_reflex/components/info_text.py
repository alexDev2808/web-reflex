import reflex as rx
from web_reflex.styles.styles import Size as Size
from web_reflex.styles.colors import Color as Color
from web_reflex.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component():
    return rx.box(
        rx.span(
            title, 
            font_weight="bold", 
            color=Color.PURPLE_SECONDARY.value
            ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
        margin_right=Size.BIG.value
    )