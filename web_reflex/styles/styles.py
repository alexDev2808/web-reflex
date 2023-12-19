import reflex as rx
from enum import Enum

from .colors import Color as Color
from .colors import TextColor as TextColor

from .fonts import Font as Font

# Constant
MAX_WIDTH = "760px"


# Sizes

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "0.9em"
    LARGE = "1.5em"
    BIG = "2em"


# Styles
    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "font_family": Font.TITLE.value,
        "color":TextColor.HEADER.value,
    },
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
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
    font_weight="bold",
    font_size=Size.BIG.value
)

title_style = dict(
    width='100%',
    size="lg",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value, 
    color=TextColor.BODY.value,
)

