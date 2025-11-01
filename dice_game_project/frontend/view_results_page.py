import reflex as rx
from dice_game_project.backend.view_results_backend import ViewResultsState
from dice_game_project.frontend.headers import header_home

#Page to view game results
#Loads results from external file 

def view_results_page() -> rx.Component:
    return rx.container(
        header_home(),
        rx.heading("Game Results", size="6", margin_bottom="2rem"),
        
        rx.button(
            "Load Results",
            on_click=ViewResultsState.load_results,
            size="3",
            margin_bottom="2rem",
        ),
        
        rx.cond(
            ViewResultsState.results,
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Winner"),
                        rx.table.column_header_cell("Score"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(
                        ViewResultsState.results,
                        lambda result: rx.table.row(
                            rx.table.cell(result["winner"]),
                            rx.table.cell(result["score"]),
                        ),
                    ),
                ),
                width="100%",
                variant="surface",
            ),
        ),
        
        padding="2rem",
    )