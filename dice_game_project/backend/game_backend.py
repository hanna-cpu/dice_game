import reflex as rx
import random
from typing import List
from dice_game_project.backend.parent_state import ParentStateClass

class GameState(ParentStateClass):
    # Game state variables
    current_player: int = 1
    round_number: int = 1
    dice1: int = 0
    dice2: int = 0
    player1_scores: List[int] = [0, 0, 0, 0, 0]
    player2_scores: List[int] = [0, 0, 0, 0, 0]
    game_over: bool = False
    winner_message: str = ""
    is_tiebreaker: bool = False
    roll_count: int = 0
    
    @rx.var
    def player1_total(self) -> int:
        """Calculate Player 1's total score"""
        return sum(self.player1_scores)
    
    @rx.var
    def player2_total(self) -> int:
        """Calculate Player 2's total score"""
        return sum(self.player2_scores)
    
    def roll_dice(self):
        """Handle dice rolling logic"""
        if self.game_over:
            return
        
        # Roll two dice
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        total = self.dice1 + self.dice2
        
        # Calculate score based on rules
        score = total
        
        # Even number: add 10 points
        if total % 2 == 0:
            score += 10
        # Odd number: subtract 5 points
        else:
            score -= 5
        
        # Double: roll extra die
        extra_points = 0
        if self.dice1 == self.dice2:
            extra_die = random.randint(1, 6)
            extra_points = extra_die
            score += extra_points
        
        # Score cannot go below 0
        score = max(0, score)
        
        # Update scores
        if not self.is_tiebreaker:
            if self.current_player == 1:
                self.player1_scores[self.round_number - 1] += score
            else:
                self.player2_scores[self.round_number - 1] += score
        else:
            # Tiebreaker logic
            if self.current_player == 1:
                self.player1_scores[4] += score
            else:
                self.player2_scores[4] += score
        
        self.roll_count += 1
        
        # Switch turns or advance round
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
            if not self.is_tiebreaker:
                if self.round_number < 5:
                    self.round_number += 1
                else:
                    self.check_winner()
            else:
                self.check_tiebreaker()
    
    def check_winner(self):
        """Check who won after 5 rounds"""
        player1_total = sum(self.player1_scores)
        player2_total = sum(self.player2_scores)
        
        if player1_total > player2_total:
            self.winner_message = f"Player 1 wins with {player1_total} points!"
            self.save_winner("Player 1", player1_total)
            self.game_over = True
        elif player2_total > player1_total:
            self.winner_message = f"Player 2 wins with {player2_total} points!"
            self.save_winner("Player 2", player2_total)
            self.game_over = True
        else:
            self.winner_message = "It's a tie! Starting tiebreaker round..."
            self.is_tiebreaker = True
            self.current_player = 1
    
    def check_tiebreaker(self):
        """Check tiebreaker result"""
        player1_total = sum(self.player1_scores)
        player2_total = sum(self.player2_scores)
        
        if player1_total > player2_total:
            self.winner_message = f"Player 1 wins tiebreaker with {player1_total} points!"
            self.save_winner("Player 1", player1_total)
            self.game_over = True
        elif player2_total > player1_total:
            self.winner_message = f"Player 2 wins tiebreaker with {player2_total} points!"
            self.save_winner("Player 2", player2_total)
            self.game_over = True
        else:
            self.winner_message = "Still tied! Roll again..."
            self.current_player = 1
    
    def save_winner(self, name: str, score: int):
        """Save winner to external file"""
        try:
            with open("winner.txt", "a") as f:
                f.write(f"Winner: {name}, Score: {score}\n")
        except Exception as e:
            print(f"Error saving winner: {e}")
    
    def reset_game(self):
        """Reset game to initial state"""
        self.current_player = 1
        self.round_number = 1
        self.dice1 = 0
        self.dice2 = 0
        self.player1_scores = [0, 0, 0, 0, 0]
        self.player2_scores = [0, 0, 0, 0, 0]
        self.game_over = False
        self.winner_message = ""
        self.is_tiebreaker = False
        self.roll_count = 0