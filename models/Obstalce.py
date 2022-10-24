import turtle

class Obstacle():
    turt = None

    def __init__(self):
        self.turt = turtle.Turtle()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("green")
        self.turt.shapesize(stretch_wid=6, stretch_len=2)
        self.turt.penup()
        #self.turt.goto(100, 100)
