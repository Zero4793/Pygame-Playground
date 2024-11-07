from util.ball import Ball
import random

class Gravity:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(64):
			self.balls.append(Ball(screen,
						  pos=(random.randint(0,screen.get_width()), random.randint(0,screen.get_height())),
						  vel=(random.uniform(-5,5), random.uniform(-5,5)),
						  bodyGrav=100,
						  repel=5000,
						  spaceJelly=0
						  ))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			for other in self.balls:
				if ball == other: continue
				ball.force(other)
		for ball in self.balls:
			ball.process()
			ball.wallCollide()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()