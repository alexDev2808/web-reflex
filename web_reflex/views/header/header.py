import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="alexhDev2808", size="xl"),
        rx.text("@Alexh1230"),
        rx.text("Soy ingeniero de software y actualmente trabajo como desarrollador web con Python y JavaScript"),

    )