import reflex as rx
from dice_game_project.backend.parent_state import ParentStateClass

# We create the headers as a function so it will be easy to call them and add them 
# to different pages. 

def header_home() -> rx.Component:
    """Main navigation header"""
    return rx.hstack(
        rx.heading("Dice Game", size="7", color="white"),
        rx.text(f"Player 1: , {ParentStateClass.player2_username}", color="black", size="3"),
        rx.spacer(),
        rx.color_mode.button(),
        rx.spacer(),
        rx.hstack(
            rx.link(
                rx.button("Login", variant="ghost", color_scheme="gray", size="3"),
                href="/login"
            ),
            rx.link(
                rx.button("Signup", variant="ghost", color_scheme="gray", size="3"),
                href="/register"
            ),

           



            rx.link(
                rx.button("Export", variant="ghost", color_scheme="gray", size="3"),
                href="/export"
            ),
           
            spacing="4"
        ),
        width="100%",
        padding="1rem 2rem",
        background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        align="center",
        position="sticky",
        top="0",
        z_index="100"
    )

