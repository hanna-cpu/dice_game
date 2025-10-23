import reflex as rx
import sqlite3
# Define the backend state for registration
# This is the backend for Register
# register frontend sets the class variables when user types them.
# we have a register function , which is called when user press the register button.
# the function connects to the database and runs a INSERT query and adds the user inputs 
# to the users table in the database. 

class RegisterState(rx.State):
    username: str = ""
    password: str = ""
    date_of_birth: str = ""
    favorite_artists: str = ""
    favorite_genre: str = ""
    message: str = ""
    register_success: bool = False
    
    def register(self):
        # Connect to the database
        conn = sqlite3.connect('dice_gamedb')
        cursor = conn.cursor()
        
        # Insert the new user
        query = "INSERT INTO users (username, password)  VALUES (?, ?)"
        cursor.execute(query, (self.username, self.password))
        
        conn.commit()
        conn.close()
        
        self.message = "Registration successful! You can now login."
        self.register_success = True
        # Below we redirect the user to the login after sucessful registration
        return rx.redirect("/player1_login")

