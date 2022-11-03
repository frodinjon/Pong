from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
	
	def __init__(self):
		self.l_score = 0
		self.r_score = 0
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.refresh()
		


	def rscore(self):
		self.r_score += 1
		self.refresh()


	def lscore(self):
		self.l_score += 1
		self.refresh()


	def refresh(self):
		self.clear()
		while self.ycor() > -350:
			self.pendown()
			self.fd(20)
			self.penup()
			self.fd(20)
		self.goto(-100, 200)
		self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
		self.goto(100, 200)
		self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
		self.goto(0, 350)
		self.setheading(270)
		