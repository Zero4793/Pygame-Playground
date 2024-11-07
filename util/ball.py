import pygame
import random
import util.SFX as SFX

class Ball:
	def __init__(self, screen, pos=None, vel=None, col=None, radius=10, elasticity=1, friction=0, spaceJelly=0, floorGrav=0, bodyGrav=0, repel=0):
		# either give value, true for random, or empty for base
		self.screen = screen
		self.exist = True
		
		width, height = screen.get_size()
		self.pos = pygame.math.Vector2(pos) if pos is not None else pygame.math.Vector2(width/2, height/2)
		self.vel = pygame.math.Vector2(vel) if vel is not None else pygame.math.Vector2(0,0)
		if col:
			self.R, self.G, self.B = col
		else:
			self.R = random.randint(0,255)
			self.G = random.randint(0,255)
			self.B = random.randint(0,255)
		self.radius = radius
		self.elasticity = elasticity
		self.friction = friction
		self.spaceJelly = spaceJelly
		self.floorGrav = floorGrav
		self.bodyGrav = bodyGrav
		self.repel = repel


	def process(self):
		self.killNoClip()
		self.vel *= 1-self.spaceJelly
		self.pos += self.vel


	def killNoClip(self):
		# kill ball if dist too big
		if self.pos.magnitude() > 10000:
			self.exist = False


	def wallCollide(self):
		walls = [False, False, False, False]
		width, height = self.screen.get_size()
		if self.pos.x - self.radius <= 0:
			self.vel.x *= -self.elasticity
			self.pos.x -= 2*(self.pos.x-self.radius)
			self.vel.y *= 1-self.friction
			if self.vel.x != 0: SFX.note(self.vel.magnitude()*50, 0.1, 0.5, 1)
			walls[0] = True			
		elif self.pos.x + self.radius >= width:
			self.vel.x *= -self.elasticity
			self.pos.x -= 2*(self.pos.x+self.radius-width)
			self.vel.y *= 1-self.friction
			if self.vel.x != 0: SFX.note(self.vel.magnitude()*50, 0.1, 0.5, 0)
			walls[1] = True
		if self.pos.y - self.radius <= 0:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y-self.radius)
			self.vel.x *= 1-self.friction
			if self.vel.y != 0: SFX.note(self.vel.magnitude()*50, 0.1, 0.5, .5)
			walls[2] = True
		elif self.pos.y + self.radius >= height:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y+self.radius-height)
			self.vel.x *= 1-self.friction
			if self.vel.y != 0: SFX.note(self.vel.magnitude()*50, 0.1, 0.5, .5)
			walls[3] = True
		return walls


	def gravity(self):
		self.vel.y += self.floorGrav

	
	def force(self, other):
		diff = (other.pos - self.pos)
		dist = diff.magnitude()
		dir = diff.normalize()
		if dist < self.radius + other.radius:
			self.vel -= dir*self.vel.magnitude()
			return

		#gravity
		self.vel += dir * self.bodyGrav / (dist**2)
		#repel
		self.vel -= dir * self.repel / (dist**3)


	def display(self):
		col = (self.R, self.G, self.B)
		pygame.draw.circle(self.screen, col, (int(self.pos.x), int(self.pos.y)), self.radius)
