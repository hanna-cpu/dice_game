
import reflex as rx

# This is the Parent Class. it holds a variable called username so all the other backend state classes 
# can have access to this variable.
# All the backend state classes are a child from this class.
# This class is a child of Reflex State . that is by Reflex design .


class ParentStateClass(rx.State):
    player1username: str = "*(Player 1 You Are Not Logged In)*"
    player2username: str = "*(Player 2 You Are Not Logged In)*"
    

