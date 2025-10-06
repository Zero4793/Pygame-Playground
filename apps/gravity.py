from util.ball import Ball
import random
import pygame

class Gravity:
	def __init__(self, screen, _):
		self.screen = screen
		self.mouseP = pygame.math.Vector2(0,0)
		self.drag = False

		self.balls = []
		# for i in range(16):
		# 	self.balls.append(Ball(screen,
		# 				  pos=(random.randint(0,screen.get_width()), random.randint(0,screen.get_height())),
		# 				  vel=(random.uniform(-2,2), random.uniform(-2,2)),
		# 				  bodyGrav=.1,
		# 				  repel=0,
		# 				  spaceJelly=0,
		# 				  collide=True,
		# 				  merging=False,
		# 				  elasticity=0.5,
		# 				  radius = random.randint(5,50),
		# 				  ))
		self.balls.append(Ball(screen,
						pos=(screen.get_width()/2, screen.get_height()/2),
						vel=(0,0),
						bodyGrav=.5,
						collide=True,
						merging=True,
						elasticity=0.9,
						radius = 100,
						col=(255,200,0),
						))
		self.balls.append(Ball(screen,
						pos=(screen.get_width()/2+200, screen.get_height()/2),
						vel=(0,5),
						bodyGrav=.5,
						collide=True,
						merging=True,
						elasticity=0.9,
						radius = 10,
						col=(255,100,0),
						))
		self.balls.append(Ball(screen,
						pos=(screen.get_width()/2+550, screen.get_height()/2),
						vel=(0,3),
						bodyGrav=.5,
						collide=True,
						merging=True,
						elasticity=0.9,
						radius = 20,
						col=(0,150,255),
						))
		self.balls.append(Ball(screen,
						pos=(screen.get_width()/2+600, screen.get_height()/2),
						vel=(0,5),
						bodyGrav=.5,
						collide=True,
						merging=True,
						elasticity=0.9,
						radius = 5,
						col=(100,100,100),
						))


	def process(self, keyheld, keypressed):
		camera = pygame.math.Vector2(0,0)
		mass = 0
		avgVel = pygame.math.Vector2(0,0)
		for ball in self.balls:
			camera += ball.pos*ball.mass
			mass += ball.mass
			avgVel += ball.vel
			for other in self.balls:
				if ball == other: continue
				ball.force(other)
		for ball in self.balls:
			ball.process()
			# ball.wallCollide()
			if not ball.exist:# or ball.mass > 10000:
				self.balls.remove(ball)
		if mass != 0:
			camera/= mass
			avgVel/= len(self.balls)
			camera-= pygame.math.Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
			for ball in self.balls:
				ball.pos -= camera
				ball.vel -= avgVel
		
		if pygame.mouse.get_pressed()[0] and not self.drag:
			self.mouseP = pygame.math.Vector2(pygame.mouse.get_pos())
			self.drag = True
		elif not pygame.mouse.get_pressed()[0] and self.drag:
			self.drag = False
			# create new ball
			self.balls.append(Ball(self.screen,
						  pos=self.mouseP,
						  vel=(self.mouseP-pygame.math.Vector2(pygame.mouse.get_pos()))/25,
						  bodyGrav=.5,
						  repel=0,
						  spaceJelly=0,
						  collide=True,
						  merging=True,
						  elasticity=0.9,
						  radius = 10,
						  ))



	def display(self):
		if self.drag:
			pygame.draw.line(self.screen, (255,100,100), self.mouseP, pygame.mouse.get_pos(), 2)
		for ball in self.balls:
			ball.display()