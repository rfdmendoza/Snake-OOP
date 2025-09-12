from turtle import Turtle




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.check_high_score()
        self.show_score()

    def check_high_score(self):
        with open("data.txt") as h_score:
            current_high_score = int(h_score.read())
            self.high_score =  current_high_score

    def show_score(self):
        self.hideturtle()
        self.setpos(x=-20, y = 275)
        self.pencolor("white")
        self.clear()
        self.write(f"Score: {self.current_score} High-score: {self.high_score}",
                   move = False, align= "Center",font=("Courier", 16, "normal"))

    def add_score(self):
        self.current_score += 1
        self.show_score()

    def reset_score(self):
        if self.current_score > self.high_score:
            with open("data.txt", mode="w") as h_score:
                h_score.write(str(self.current_score))
        self.check_high_score()
        self.current_score = 0
        self.show_score()


