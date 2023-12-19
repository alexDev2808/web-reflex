import reflex as rx
from enum import Enum

from .colors import Color as Color
from .colors import TextColor as TextColor

from .fonts import Font as Font
from .fonts import FontWeight as FontWeight

# Constant
MAX_WIDTH = "760px"

# Fuentes remotas
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Nunito:wght@700&display=swap"
]

# Sizes

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "0.9em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    EXTRA_BIG = "8em"


# Styles
    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
        "color":TextColor.HEADER.value,
    },
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.PURPLE_SECONDARY.value,
        }

    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.BIG.value
)

title_style = dict(
    width='100%',
    size="lg",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value, 
    color=TextColor.BODY.value,
)

