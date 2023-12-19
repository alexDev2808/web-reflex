import reflex as rx
from web_reflex.components.navbar import navbar
from web_reflex.views.header.header import header
from web_reflex.views.links.links import links
from web_reflex.components.footer import footer
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,
                    padding=Size.BIG.value
                ),
            ),

            footer()
    )



app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.compile()