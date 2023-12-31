import reflex as rx
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str)  -> rx.Component:

    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    margin="0px",
                    padding_right=Size.SMALL.value

                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
    