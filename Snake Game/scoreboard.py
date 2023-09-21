from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0

        #load high score
        with open("highscore.txt") as file:
            self.highscore = int(file.read())

        self.goto(0, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High-score: {self.highscore}", align="center", font=("Arial", 40, "normal"))

    def increase_score(self):
        self.score +=1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))

        #Save a new high score
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")