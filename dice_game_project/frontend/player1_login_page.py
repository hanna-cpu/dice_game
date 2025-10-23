import reflex as rx
from dice_game_project.backend.player1_login_backend import LoginState

# This is our Login Page. it shows 2 text box for entering username and password.
# when user enters username and password , it sets the variables of Login State in backend class.
# when user click on Login ,the login function of backend class will be called. 

def player1_login_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Player 1 Login", size="9", margin_bottom="2rem"),
            
            rx.vstack(
                rx.text("Username", size="3", weight="bold"),
                rx.input(
                    placeholder="Enter username",
                    on_change=LoginState.set_username,
                    width="100%",
                    size="3"
                ),
                
                rx.text("Password", size="3", weight="bold", margin_top="1rem"),
                rx.input(
                    placeholder="Enter password",
                    type="password",
                    on_change=LoginState.set_password,
                    width="100%",
                    size="3"
                ),
                
                rx.button(
                    "Submit",
                    on_click=LoginState.login,
                    size="3",
                    margin_top="1.5rem",
                    width="100%"
                ),
                
                rx.cond(
                    LoginState.message != "",
                    rx.text(
                        LoginState.message,
                        color=rx.cond(
                            LoginState.login_success,
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