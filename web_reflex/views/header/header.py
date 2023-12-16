import reflex as rx
from web_reflex.components.link_icon import link_icon
from web_reflex.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="alexhDev2808", size="xl"),
            rx.vstack(
                rx.heading("Hola 👋🏻 mi nombre es J. Alexis", size="lg"),
                rx.text("@Alexh1230", margin_top="0px !important"),
                rx.hstack(
                    link_icon("https://twitter.com/Alexh1230"),
                    link_icon("https://twitter.com/Alexh1230"),
                    link_icon("https://twitter.com/Alexh1230"),
                ),
                align_items="start"
            ),

        ),
        rx.text("Soy ingeniero de software y actualmente trabajo como desarrollador web con Python y JavaScript"),
        spacing=Size.BIG.value,
        align_items="start",


    )