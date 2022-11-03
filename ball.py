from turtle import Turtle
import random

STARTING_SPEED = 0.1


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_speed = 0.1


	def move(self):
		self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


	def bouncey(self):
		self.y_move *= -1

	def bouncex(self):
		self.x_move *= -1
		self.move_speed *= 0.9


	def reset(self):
		self.clear()
		self.goto(0,0)
		self.move_speed = STARTING_SPEED
		self.bouncex()