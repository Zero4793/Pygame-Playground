from util.ball import Ball
import random
import pygame

class Gravity:
	def __init__(self, screen, _):
		self.screen = screen

		self.balls = []
		for i in range(6):
			self.balls.append(Ball(screen,
						  pos=(random.randint(0,screen.get_width()), random.randint(0,screen.get_height())),
						  vel=(random.uniform(-5,5), random.uniform(-5,5)),
						  bodyGrav=1,
						  repel=0,
						  spaceJelly=0,
						  collide=True,
						  merging=False,
						  elasticity=.99,
						  radius = random.randint(5,50),
						  ))


	def process(self, keyheld, keypressed):
		camera = pygame.math.Vector2(0,0)
		mass = 0
		for ball in self.balls:
			camera += ball.pos*ball.mass
			mass += ball.mass
			for other in self.balls:
				if ball == other: continue
				ball.force(other)
		for ball in self.balls:
			ball.process()
			# ball.wallCollide()
			if not ball.exist:
				self.balls.remove(ball)
		# camera/= len(self.balls)
		camera/= mass
		camera-= pygame.math.Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
		for ball in self.balls:
			ball.pos -= camera		


	def display(self):
		for ball in self.balls:
			ball.display()