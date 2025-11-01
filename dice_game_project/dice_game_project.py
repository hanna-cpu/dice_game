"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


# Below we import all our frontend and baxkend files. 
# it is mandatory
from dice_game_project.frontend.player1_login_page import player1_login_page
from dice_game_project.frontend.player2_login_page import player2_login_page
from dice_game_project.frontend.register_page import register_page
from dice_game_project.frontend.homepage import homepage_page
from dice_game_project.frontend.game_page import game_page 
from dice_game_project.frontend.view_results_page import view_results_page

## This is our Landing Page. It is the default page that the program shows
# it shows a welcome and 2 links to Login and Register. 
        
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to the Dice Game", size="6"),
            rx.link("Login", href="player1_login"),
            rx.link("Register", href="register"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


## This are the Reflex WEB URLs that we create
# For every frontend page that we create, we need to create a line below here
# this is for creating the URLs and tells reflex , when each URL is selected which frontend 
# page shoudl be executed. 

app = rx.App()
app.add_page(index)
app.add_page(player1_login_page, route="/player1_login")
app.add_page(player2_login_page, route="/player2_login")
app.add_page(register_page, route="/register")
app.add_page(homepage_page, route="/homepage")
app.add_page(game_page, route="/game_page")
app.add_page(view_results_page, route="/view_results")