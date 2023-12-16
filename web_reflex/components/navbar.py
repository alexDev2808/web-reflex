import reflex as rx
from web_reflex.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "alexhDev",
            font_size="2rem"
        ),
        position="sticky",
        bg="lightgreen",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )