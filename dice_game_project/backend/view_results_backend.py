import reflex as rx
import sqlite3

from dice_game_project.backend.parent_state import ParentStateClass

class ViewResultsState(ParentStateClass):
    results: list[dict[str, str]] = []
    
    def load_results(self):
        """Load game results from external file and parse into table data"""
        try:
            with open("winner.txt", "r") as f:
                lines = f.readlines()
            
            results_list = []
            for line in lines:
                line = line.strip()
                if line:
                    # Parse line format: "Winner: Player 1, Score: 96"
                    parts = line.split(", ")
                    if len(parts) == 2:
                        winner = parts[0].replace("Winner: ", "").strip()
                        score = parts[1].replace("Score: ", "").strip()
                        results_list.append({
                            "winner": winner,
                            "score": score,
                            "score_int": int(score)
                        })
            
            # Sort by score (descending) and get top 5
            results_list.sort(key=lambda x: x["score_int"], reverse=True)
            self.results = results_list[:5]
            
        except Exception as e:
            self.results = [{"winner": "Error", "score": str(e)}]