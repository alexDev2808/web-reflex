import reflex as rx
import datetime
from web_reflex.styles.styles import Size as Size
from web_reflex.styles.colors import TextColor as TextColor
import web_reflex.components.constants as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.EXTRA_BIG.value
        ),
        rx.link(
            f"@ 2022-{datetime.date.today().year} alexhDev2808 by J. Alexis V1.",
            href=const.TWITTER,
            is_external=True,
            font_size=Size.MEDIUM.value,
            text_align="center"
        ),
        rx.text(
            " Construido con ❤️ de Mexico para el mundo.",
            font_size=Size.MEDIUM.value,
            text_align="center"
        ),
        margin_top=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color=TextColor.FOOTER.value
    )