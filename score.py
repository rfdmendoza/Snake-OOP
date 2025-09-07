from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.show_score()

    def show_score(self):
        self.hideturtle()
        self.setpos(x=-20, y = 275)
        self.pencolor("white")
        self.write(f"Score: {self.current_score}", move = False, align= "Center",font=("Courier", 16, "normal"))

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.show_score()
    def game_over(self):
        self.penup()
        self.setpos(x=0, y = 0)
        self.pencolor("red")
        self.write("GAME OVER", move=False, align="Center", font=("Courier", 24, "bold"))