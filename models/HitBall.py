import turtle
from models.GameScreen import GameScreen
from managers.EventManager import EventManager


class HitBall:
    ball = None
    dx = 5
    dy = -5
    eventManager = None

    def __init__(self, eventManager):
        # Ball of circle shape
        self.ball = b = turtle.Turtle()
        self.eventManager = eventManager

        b.speed(40)
        b.shape("circle")
        b.color("blue")
        b.penup()
        b.goto(0, 0)

        GameScreen.bindKeys(self.speedincrease, "I")
        GameScreen.bindKeys(self.speeddecrease, "K")

    def speedincrease(self):
        self.dx += 2 * (-1 if self.dx < 0 else 1)
        self.dy += 2 * (-1 if self.dy < 0 else 1)

    def speeddecrease(self):
        self.dx -= 2 * (1 if self.dx > 0 else -1)
        self.dy -= 2 * (1 if self.dy > 0 else -1)

    def update(self):
        b = self.ball

        b.setx(b.xcor() + self.dx)
        b.sety(b.ycor() + self.dy)

        ymax = 280

        # Checking borders
        if b.ycor() > ymax:
            b.sety(ymax)
            self.dy *= -1

        if b.ycor() < -ymax:
            b.sety(-ymax)
            self.dy *= -1

        xmax = 500

        if b.xcor() > xmax or b.xcor() < -xmax:
            b.goto(0, 0)
            self.dy *= -1
            self.eventManager.dispatchEvent(EventManager.EVENT_GOAL)

        if b.xcor() > xmax:
            players[0] += 1

        if b.xcor() < -xmax:
            players[1] += 1
