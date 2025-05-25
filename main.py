from turtle import Screen
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_state = { "is_on": True }

# Score needed to win the game
match_won = 5

def end_game():
    game_state["is_on"] = False
    t.bye()

def restart():
    scoreboard.restart()
    ball.restart_position()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(restart, "r")
screen.onkeypress(end_game, "Escape")


while game_state["is_on"]:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision
    if ball.ycor() >= 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # reset ball if missed on right paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        if scoreboard.l_score < match_won:
            ball.restart_position()
        else:
            scoreboard.game_won()

    # reset ball if missed on left paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        if scoreboard.r_score < match_won:
            ball.restart_position()
        else:
            scoreboard.game_won()


screen.exitonclick()