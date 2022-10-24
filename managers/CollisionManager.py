class CollisionManager:
    collisionDistance = 80
    players = None
    hitBalls = None

    def __init__(self, players, hitBalls):
        self.players = players
        self.hitBalls = hitBalls

    def update(self):
        players = self.players

        for player in players:
            for hitball in self.hitBalls:
                ball = hitball.ball
                collisionDistance = self.collisionDistance

                # Ball collision with players paddles
                if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < player.ycor() + collisionDistance and ball.ycor() > player.ycor() - collisionDistance:
                    ball.setx(360)
                    hitball.dx *= -1

                if ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < player.ycor() + collisionDistance and ball.ycor() > player.ycor() - collisionDistance:
                    ball.setx(-360)
                    hitball.dx *= -1