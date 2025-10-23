import reflex as rx
import sqlite3
import os
from typing import List
from dice_game_project.backend.parent_state import ParentStateClass

# Thsi is the backedn state class for export. 
# first it loads list of artists from datbase by running a SELECT artist query to datbase. we use group by artist
# to not show duplicates. 
# the list of artists is loaded from database to the artists list in the class and then frotend loads that list
# once the user click on export the load_songs function runs and runs a query to database to get list 
# of song titles of selected_artist . then it creates a export.txt file and writes into that. 


class ExportState(ParentStateClass):

    username: str = ParentStateClass.player1_username
    message: str = ""
    save_success: bool = False
    artists: List[str] = []
    selected_artist: str = ""

    def load_artists(self):
        #Load all artists from library
        conn = sqlite3.connect('musicdb')
        cursor = conn.cursor()
        
        cursor.execute("SELECT artist FROM songlibrary GROUP BY artist")
        rows = cursor.fetchall()
        
        self.artists = [row[0] for row in rows]
       
        conn.close()


    def load_songs(self):
        # Load all songs of selected artist
        if not self.selected_artist:
            self.message = "Please select an artist first"
            return
            
        conn = sqlite3.connect('musicdb')
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT song_title FROM songlibrary WHERE artist = ?", (self.selected_artist,))
        rows = cursor.fetchall()
        
        export_path = os.path.join("assets", "export.txt")
        with open(export_path, "w", encoding="utf-8") as f:
            f.write(f"Artist: {self.selected_artist}\n")
            for song_title in rows:
                f.write(f"{song_title[0]}\n") 
        
        conn.close()
        self.message = f"Exported {len(rows)} songs of {self.selected_artist} to export.txt"
        self.save_success = True
        