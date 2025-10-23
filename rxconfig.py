import reflex as rx

config = rx.Config(
    app_name="dice_game_project",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)