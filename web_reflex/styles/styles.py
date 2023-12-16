import reflex as rx
from enum import Enum

# Constant
MAX_WIDTH = "760px"


# Sizes

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "0.9em"
    BIG = "2em"


# Styles
    
BASE_STYLE = {
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

title_style = dict(
    size='lg',
    width='100%',
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value, 
)

