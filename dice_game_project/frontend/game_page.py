import reflex as rx
from dice_game_project.backend.game_backend import GameState
from dice_game_project.frontend.headers import header_home

#the main game page UI
#shows the dice, roll button, scores table, current turn, messages


def game_page() -> rx.Component:

    return rx.box(
        header_home(),
        
        # Score table (top right corner - absolutely positioned)
        rx.box(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Round"),
                        rx.table.column_header_cell("Player 1 Score"),
                        rx.table.column_header_cell("Player 2 Score"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.cell("Round 1"),
                        rx.table.cell(GameState.player1_scores[0].to_string()),
                        rx.table.cell(GameState.player2_scores[0].to_string()),
                    ),
                    rx.table.row(
                        rx.table.cell("Round 2"),
                        rx.table.cell(GameState.player1_scores[1].to_string()),
                        rx.table.cell(GameState.player2_scores[1].to_string()),
                    ),
                    rx.table.row(
                        rx.table.cell("Round 3"),
                        rx.table.cell(GameState.player1_scores[2].to_string()),
                        rx.table.cell(GameState.player2_scores[2].to_string()),
                    ),
                    rx.table.row(
                        rx.table.cell("Round 4"),
                        rx.table.cell(GameState.player1_scores[3].to_string()),
                        rx.table.cell(GameState.player2_scores[3].to_string()),
                    ),
                    rx.table.row(
                        rx.table.cell("Round 5"),
                        rx.table.cell(GameState.player1_scores[4].to_string()),
                        rx.table.cell(GameState.player2_scores[4].to_string()),
                    ),
                    rx.table.row(
                        rx.table.cell("Total", weight="bold"),
                        rx.table.cell(
                            rx.text(
                                GameState.player1_total.to_string(),
                                weight="bold"
                            )
                        ),
                        rx.table.cell(
                            rx.text(
                                GameState.player2_total.to_string(),
                                weight="bold"
                            )
                        ),
                    ),
                ),
            ),
            position="absolute",
            top="2rem",
            right="2rem",
        ),
        
        # Main game area (centered)
        rx.vstack(
            rx.box(flex="1"),
            rx.vstack(
                rx.heading("Dice Game", size="9", margin_bottom="2rem"),
                
                # Current turn display
                rx.text(
                    rx.cond(
                        GameState.game_over,
                        GameState.winner_message,
                        f"Player {GameState.current_player_name}'s Turn"
                    ),
                    size="6",
                    weight="bold",
                    margin_bottom="1rem",
                ),
                
                # Dice displays
                rx.hstack(
                    rx.vstack(
                        rx.text("Dice 1", weight="bold"),
                        rx.input(
                            value=GameState.dice1.to_string(),
                            read_only=True,
                            size="3",
                            width="100px",
                            text_align="center",
                        ),
                    ),
                    rx.vstack(
                        rx.text("Dice 2", weight="bold"),
                        rx.input(
                            value=GameState.dice2.to_string(),
                            read_only=True,
                            size="3",
                            width="100px",
                            text_align="center",
                        ),
                    ),
                    spacing="4",
                    margin_bottom="1rem",
                ),
                
                # Roll button
                rx.button(
                    "Roll",
                    on_click=GameState.roll_dice,
                    size="3",
                    disabled=GameState.game_over,
                ),
                
                # Reset button
                rx.button(
                    "New Game",
                    on_click=GameState.reset_game,
                    size="2",
                    margin_top="1rem",
                    color_scheme="gray",
                ),
                
                # Message
                rx.text(
                    GameState.message,
                    size="6",
                    weight="bold",
                    margin_top="1rem",
                ),
                
                align="center",
                justify="center",
            ),
            
            rx.box(flex="1"),
            
            width="100%",
            height="100vh",
            justify="center",
            align="center",
        ),
    )