class CollisionManager:
    players = None
    hitBall = None

    def __init__(self, players, hitBall):
        self.players = players
        self.hitBall = hitBall

    def update(self):
        ball = self.hitBall.ball
        players = self.players

        for player in players:

            # Ball collision with players paddles
            if ball.xcor() > 360 and ball.xcor()< 370 and ball.ycor() < player.ycor() + 40 and ball.ycor() > player.ycor() - 40:
                ball.setx(360)
                self.hitBall.dx *= -1

            if ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < player.ycor() + 40 and ball.ycor() > player.ycor() - 40:
                ball.setx(-360)
                self.hitBall.dx *= -1