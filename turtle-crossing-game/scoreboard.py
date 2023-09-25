from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-200,250)
        self.hideturtle()
        self.color("black")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=FONT)
        
    def level_up(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align="center", font=FONT)
        
    
