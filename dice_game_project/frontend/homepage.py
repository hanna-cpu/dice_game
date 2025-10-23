import reflex as rx

from dice_game_project.frontend.headers import header_home
# This is the home page. it shows 2 headers on top of the screen
# Home header has the main buttons for project and playlist has only for playlist

def homepage_page() -> rx.Component:
    return rx.box(
        header_home(),        
        min_height="100vh",
        background="#f8f9fa"
    )