import reflex as rx
from web_reflex.components.link_button import link_button
from web_reflex.components.title import title
from web_reflex.styles.styles import Size as Size
import web_reflex.components.constants as Link

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        link_button(
            "16 dias con Python", 
            "16 dias aprendiendo Python y creando varias apps", 
            "icons/python.svg",
            Link.PYTHON_16
        ),
        link_button(
            "Administrador de Pacientes", 
            "App creada con Vue.js", 
            "icons/vuejs.svg",
            Link.ADMIN_PACIENTES_VUE
        ),
        link_button(
            "Apps Android", 
            "Una sola app que contiene por dentro diferentes apps con diferente funcionalidad.",
            "icons/android.svg",
            Link.ANDROID
        ),
        link_button(
            "TMDB API", 
            "Consumo de la API de TMDB con JavaScript.", 
            "icons/square-js.svg",
            Link.TMDB_API_JS
        ),

        title("Contacto"),
        link_button(
            "Email", 
            Link.EMAIL, 
            "icons/envelope-solid.svg", 
            f"mailto:{Link.EMAIL}"
        ),
        link_button(
            "CV", 
            "Descargar CV", 
            "icons/file-solid.svg", 
            Link.CV
        ),

        width="100%",
        spacing=Size.MEDIUM.value
    )