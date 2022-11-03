from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

starting_positions = [(-350, 0), (350, 0)]
paddles = []
scoreboard_positions = [(-150, 250), (150, 250)]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height = 600)
screen.title("Pong")
screen.tracer(0)

for position in starting_positions:
	paddle = Paddle(position)
	paddles.append(paddle)

scoreboard = Scoreboard()

ball = Ball()

screen.onkey(paddles[1].go_up, "Up")
screen.onkey(paddles[1].go_down, "Down")
screen.onkey(paddles[0].go_up, "w")
screen.onkey(paddles[0].go_down, "s")
screen.listen()

game_on = True

while game_on:
	screen.update()
	ball.move()
	time.sleep(ball.move_speed)

	# detect top/bottom collision
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bouncey()


	#detect collision with paddle
	if ball.xcor() > 320 or ball.xcor() < -320:
		if ball.distance(paddles[0]) < 50 or ball.distance(paddles[1]) < 50:
			ball.bouncex()
		else:
			#detect score
			if ball.xcor() > 400:
				scoreboard.lscore()
				for i in range (2):
					paddles[i].reset(starting_positions[i])
				ball.reset()
				time.sleep(1)
			elif ball.xcor() < -400:
				scoreboard.rscore()
				for i in range (2):
					paddles[i].reset(starting_positions[i])
				ball.reset()
				time.sleep(1)

	
	#detect score
	# if ball.xcor() > 400:
	# 	scoreboard.increase_score()
	# 	for i in range (2):
	# 		paddles[i].reset(starting_positions[i])
	# 	ball.reset()
	# 	time.sleep(1)
	# elif ball.xcor() < -400:
	# 	scoreboard2.increase_score()
	# 	for i in range (2):
	# 		paddles[i].reset(starting_positions[i])
	# 	ball.reset()
	# 	time.sleep(1)


screen.exitonclick()