import reflex as rx

from dice_game_project.frontend.headers import header_home
from dice_game_project.backend.export_backend import ExportState


# This is the frontend for Export song list . it shows a dropdown menu to the user
# drop down is list of artists that backend laods them from database . 
# once user chooses the artists, and click on Export, backend generates the export 
# we create a link to download the export.txt , we used the reflex asset , which is a 
# bare minimum for providng a download link, but the export.txt is not dyanmically chnaged in reflex



def export() -> rx.Component:
    return rx.box(
        header_home(),
 
        
        # Main content area
        rx.container(
            rx.vstack(
                rx.heading("Export Song List", size="8", margin_top="2rem"),
                rx.box(
                    rx.heading("Available Artists", size="6", margin_top="2rem", margin_bottom="1rem"),
                    
                    # Dropdown/Select component for artists
                    rx.select(
                        ExportState.artists,
                        placeholder="Select an artist",
                        on_change=ExportState.set_selected_artist,
                        width="100%",
                        size="3"
                    ),
                    
                    # Export button
                    rx.button(
                        "Export Songs",
                        on_click=ExportState.load_songs,
                        margin_top="1rem",
                        size="3"
                    ),
                    
                    # Success message
                    rx.cond(
                        ExportState.message != "",
                        rx.text(
                            ExportState.message,
                            margin_top="1rem"
                        ),

                    ),
                    
                    
                    variant="surface",
                    width="100%"
                ),
                rx.link(
                    "Download Songs (export.txt)",
                    href=rx.asset("export.txt"),
                    target="_blank",
                    color="blue",
                    underline="always",
                    margin_top="1rem"
                    ),
                width="100%",
                overflow_x="auto"

            ),
            max_width="1200px",
            padding="2rem"
        ),
        on_mount=ExportState.load_artists  # This triggers loading artists when page loads!
    )