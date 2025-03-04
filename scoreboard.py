from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.file = open("high_score.txt")
        self.high_score = int(self.file.read())
        self.file.close()
        self.print_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}     High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.file = open("high_score.txt", mode="w")
        self.file.write(str(self.high_score))
        self.clear()
        self.score = 0
        self.print_score()
    # def game_over(self):
    #     self.high_score = self.score
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER\nYour final score: {self.score}", align=ALIGNMENT, font=FONT)