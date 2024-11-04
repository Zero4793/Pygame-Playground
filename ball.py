import pygame
import random

class Ball:
	def __init__(self, screen):
		self.screen = screen
		self.exist = True
		width, height = screen.get_size()
		self.rad = random.randint(10, 30)
		self.pos = pygame.math.Vector2(random.randint(self.rad, width - self.rad), random.randint(self.rad, height - self.rad))
		self.vel = pygame.math.Vector2(random.randint(-10, 10), random.randint(-10, 10))
		self.elasticity = random.uniform(0, 1)
		self.friction = random.uniform(0, .1)
		self.airResistance = random.uniform(0, .001) #space jelly
		self.col = (self.elasticity*255, self.friction*2550, self.airResistance*255000)


	def process(self):
		self.killNoClip()
		self.wallCollide()
		# self.gravity()
		self.vel *= 1-self.airResistance
		self.pos += self.vel


	def killNoClip(self):
		# kill ball if dist too big
		if self.pos.magnitude() > 10000:
			self.exist = False


	def wallCollide(self):
		width, height = self.screen.get_size()
		if self.pos.x - self.rad <= 0:
			self.vel.x *= -self.elasticity
			self.pos.x -= 2*(self.pos.x-self.rad)
			self.vel.y *= 1-self.friction
		if self.pos.y - self.rad <= 0:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y-self.rad)
			self.vel.x *= 1-self.friction
		if self.pos.x + self.rad >= width:
			self.vel.x *= -self.elasticity
			self.pos.x -= 2*(self.pos.x+self.rad-width)
			self.vel.y *= 1-self.friction
		if self.pos.y + self.rad >= height:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y+self.rad-height)
			self.vel.x *= 1-self.friction


	def gravity(self):
		self.vel.y += 0.1


	def display(self, image=None):
		pygame.draw.circle(self.screen, self.col, (int(self.pos.x), int(self.pos.y)), self.rad)
