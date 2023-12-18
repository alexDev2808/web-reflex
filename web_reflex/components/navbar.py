import reflex as rx
from web_reflex.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "alexhDev",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
            
        ),
        position="sticky",
        # background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )