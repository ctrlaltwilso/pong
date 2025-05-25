from turtle import Turtle

FONTSIZE = 60
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", FONTSIZE, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", FONTSIZE, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_won(self):
        font_s = 30
        self.clear()
        self.goto(0, 100)
        if self.l_score > self.r_score:
            self.write("Player 1 Won!", align="center", font=("Courier", font_s, "normal"))
        else:
            self.write("Player 2 Won!", align="center", font=("Courier", font_s, "normal"))
        self.goto(0, -100)
        self.write("Press 'R' to  play again", align="center", font=("courier", (font_s//2), "normal"))
        self.goto(0, -150)
        self.write("Or ESC to quit", align="center", font=("Courier", (font_s//2), "normal"))

    def restart(self):
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()