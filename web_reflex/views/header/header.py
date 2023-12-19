import reflex as rx
from web_reflex.components.link_icon import link_icon
from web_reflex.components.info_text import info_text
from web_reflex.styles.styles import Size as Size
from web_reflex.styles.colors import Color as Color
from web_reflex.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="alexhDev2808", size="xl"),
            rx.vstack(
                rx.heading(
                    "Hola 👋🏻 mi nombre es J. Alexis",
                ),
                rx.text(
                    "@Alexh1230", 
                    margin_top="0px !important", 
                    color=TextColor.BODY.value
                    ),
                rx.hstack(
                    link_icon("https://twitter.com/Alexh1230"),
                    link_icon("https://twitter.com/Alexh1230"),
                    link_icon("https://twitter.com/Alexh1230"),
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value
        ),
        rx.flex(
            info_text("2+", "años de experiencia."),
            info_text("10+", "proyectos creados."),
            width="100%"
        ),
        rx.text(
            "Soy ingeniero de software y actualmente trabajo como desarrollador web con Python y JavaScript. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@! ",
            color=TextColor.BODY.value
            ),
        spacing=Size.BIG.value,
        align_items="start",
        width="100%"


    )