import reflex as rx
from web_reflex.components.navbar import navbar
from web_reflex.views.header.header import header
from web_reflex.views.links.links import links
from web_reflex.components.footer import footer


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )


app = rx.App()
app.add_page(index)
app.compile()