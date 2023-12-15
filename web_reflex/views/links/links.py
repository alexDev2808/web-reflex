import reflex as rx
from web_reflex.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitter", "https://twitter.com/Alexh1230"),
        link_button("Linkedin", "https://linkedin.com"),
        link_button("Spotify", "https://spotify.com"),
        link_button("GitHub", "https://github.com/alexDev2808"),
    )