import reflex as rx
from dice_game_project.backend.register_backend import RegisterState
# This is the  registration page frontend
# This page includes fields for username, password, date of birth, favorite artists, and favorite genre.
# It also includes a submit button that triggers the registration process and displays success or error messages.
# The page is styled for a clean and user-friendly interface.

def register_page() -> rx.Component:
    return rx.container(
           rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Sign Up", size="9", margin_bottom="2rem"),
            
            rx.vstack(
                rx.text("Username", size="3", weight="bold"),
                rx.input(
                    placeholder="Enter username",
                    on_change=RegisterState.set_username,
                    width="100%",
                    size="3"
                ),
                
                rx.text("Password", size="3", weight="bold", margin_top="1rem"),
                rx.input(
                    placeholder="Enter password",
                    type="password",
                    on_change=RegisterState.set_password,
                    width="100%",
                    size="3"
                ),
                
                rx.text("Confirm Password", size="3", weight="bold", margin_top="1rem"),
                rx.input(
                    placeholder="Confirm password",
                    type="password",
                    width="100%",
                    size="3"
                ),
     
                
                rx.button(
                    "Submit",
                    on_click=RegisterState.register,
                    size="3",
                    margin_top="1.5rem",
                    width="100%"
                ),
                
                rx.cond(
                    RegisterState.message != "",
                    rx.text(
                        RegisterState.message,
                        color=rx.cond(
                            RegisterState.register_success,
                            "green",
                            "red"
                        ),
                        margin_top="1rem"
                    )
                ),
                
              
                width="100%",
                spacing="2"
            ),
            
            width="400px",
            padding="2rem",
            border_radius="10px",
            box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)"
        ),
        center_content=True,
        height="100vh"
    )