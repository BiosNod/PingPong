import turtle
from models.GameScreen import GameScreen


class Pad():
    distance = 20
    score = 0
    turt = None

    def __init__(self, gox, up, down):
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.shapesize(stretch_wid=6, stretch_len=2)
        self.turt.penup()
        self.turt.goto(gox, 0)

        GameScreen.bindKeys(self.moveup, up)
        GameScreen.bindKeys(self.movedown, down)

    def moveup(self):
        self.turt.sety(self.turt.ycor() + self.distance)

    def movedown(self):
        self.turt.sety(self.turt.ycor() - self.distance)

    def xcor(self):
        return self.turt.xcor()

    def ycor(self):
        return self.turt.ycor()
