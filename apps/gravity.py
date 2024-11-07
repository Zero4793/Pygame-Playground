from util.ball import Ball
import random

class Gravity:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(12):
			self.balls.append(Ball(screen,
						  pos=(random.randint(0,screen.get_width()), random.randint(0,screen.get_height())),
						  vel=(random.uniform(-5,5), random.uniform(-5,5)),
						  floorGrav=.1,
						  ))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()