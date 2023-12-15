import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "alexhDev",
            font_size="2rem"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )