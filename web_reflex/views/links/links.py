import reflex as rx
from web_reflex.components.link_button import link_button
from web_reflex.components.title import title
from web_reflex.styles.styles import Size as Size
import web_reflex.components.constants as Link

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        link_button("Twitter", "Mi perfil de Twitter donde comparto recursos para aprender", "https://twitter.com/Alexh1230"),
        link_button("Linkedin", "Mi perfil en Linkedin", "https://linkedin.com"),
        link_button("Spotify", "La musica que me gusta organizada en playlists" ,"https://spotify.com"),
        link_button("GitHub", "Todos mis proyectos creados a lo largo de mi experiencia.", "https://github.com/alexDev2808"),

        title("Contacto"),
        link_button("Email", Link.EMAIL, f"mailto:{Link.EMAIL}"),
        link_button("CV", "Descargar CV", Link.CV),
        width="100%",
        spacing=Size.MEDIUM.value
    )