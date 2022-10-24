"""
For homework ping-pong home work, you have to implement an addon to the ping-pong game. The list of possible projects includes (but not limits to):
1. done Add more players with separate key binding and collisions between players.
2. almost done Add obstacles on the canvas with different shapes (rectangles or balls).
3. TODO Make a function for players' registration with a name and displays a table of records.
4. Add the possibility to increase the difficulty by adding balls during the game.
5. DONE Increase or decrease the speed of the ball over time and implement speed controls with keys.
6*. Add walls that disappear (similar to task 2, but obstacle reappears randomly on hit).
7*. Enable physics with ball-pad friction and ball rotation.
8*. Write a bot not too hard, and not too easy: it makes mistakes and imitates the human's behavior.
"""

from models.GameScreen import GameScreen
from models.Pad import Pad
from managers.CollisionManager import CollisionManager
from managers.EventManager import EventManager
from models.HitBall import HitBall
from models.Obstalce import Obstacle

eventManager = EventManager()
eventManager.registerCallback(lambda: gameScreen.drawSketch(players), EventManager.EVENT_GOAL)
gameScreen = GameScreen()
hitBall = HitBall(eventManager)

players = [Pad(-400, "W", "S"), Pad(400, "Up", "Down"), Pad(400, "E", "D")]
gameScreen.drawSketch(players)
collisionManager = CollisionManager(players, hitBall)

Obstacle()

while 1:
    gameScreen.update()
    hitBall.update()
    collisionManager.update()
