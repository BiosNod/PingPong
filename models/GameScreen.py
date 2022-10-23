import turtle
from patterns.Singleton import singleton


@singleton
class GameScreen:
    sc = None
    sketch = None

    def __init__(self):
        # Create screen
        self.sc = sc = turtle.Screen()

        sc.title("Pong game")
        sc.bgcolor("white")
        sc.setup(width=1000, height=600)
        # Keyboard bindings
        sc.listen()

        self._initSketch()

    def update(self):
        self.sc.update()

    @staticmethod
    def bindKeys(callback, key):
        s = GameScreen()

        # Make it not case sensitive
        if len(key) == 1:
            s.sc.onkeypress(callback, key.lower())
            s.sc.onkeypress(callback, key.upper())
        else:
            s.sc.onkeypress(callback, key)

    def _initSketch(self):
        # Displays the score
        sketch = turtle.Turtle()
        sketch.speed(0)
        sketch.color("blue")
        sketch.penup()
        sketch.hideturtle()
        sketch.goto(0, 260)

        self.sketch = sketch

    def drawSketch(self, players: list):
        s = self.sketch
        s.clear()
        title = ', '.join(f"Player{i}: {p.score}" for i, p in enumerate(players))
        s.write(title, align="center", font=("Courier", 24, "normal"))
