import reflex as rx
import sqlite3

from dice_game_project.backend.parent_state import ParentStateClass 

# The login state class is a child of our Parent State Class 

class Player2LoginState(ParentStateClass):
    username: str = ""
    password: str = ""
    message: str = ""
    login_success: bool = False
    
# The login function connects to datbase
# runs a select query to find users with the user entered userame and password
# if username or password combination incorrect the select query will not return anything
# therefore we find if the user is found or not. 
    
    def login(self):

        # Connect to the database
        conn = sqlite3.connect('dice_gamedb')
        cursor = conn.cursor()
        
        # Execute the query
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (self.username, self.password))
        
        # Fetch the result
        user = cursor.fetchone()
        conn.close()
        
        if user:
            self.message = f"Login successful! Welcome, {self.username}"
            self.login_success = True
            # Below line is very very important, as here we set the Username of Parent State Class. 
            self.player2username = self.username
            # And once the user and password is correct we redirect to HomePage
            return rx.redirect("/homepage")
        else:
            self.message = "Invalid username or password"
            self.login_success = False
            
