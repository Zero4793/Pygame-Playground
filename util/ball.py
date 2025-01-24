import pygame
import random

class Ball:
	def __init__(self, screen, pos=None, vel=None, col=None, radius=10, mass=None, elasticity=1, friction=0, spaceJelly=0, floorGrav=0, bodyGrav=0, repel=0, collide=False, merging=False):
		# either give value, true for random, or empty for base
		self.screen = screen
		self.exist = True
		
		width, height = screen.get_size()
		self.pos = pygame.math.Vector2(pos) if pos is not None else pygame.math.Vector2(width/2, height/2)
		self.vel = pygame.math.Vector2(vel) if vel is not None else pygame.math.Vector2(0,0)
		self.acc = pygame.math.Vector2(0,0)
		self.mov = pygame.math.Vector2(0,0)

		if col:
			self.R, self.G, self.B = col
		else:
			self.R = random.randint(0,255)
			self.G = random.randint(0,255)
			self.B = random.randint(0,255)
		self.radius = radius
		self.mass = mass if mass is not None else radius**2
		self.elasticity = elasticity
		self.friction = friction
		self.spaceJelly = spaceJelly
		self.floorGrav = floorGrav
		self.bodyGrav = bodyGrav
		self.repel = repel
		self.collide = collide
		self.merging = merging


	def process(self):
		self.killNoClip()
		self.vel *= 1-self.spaceJelly
		self.vel += self.acc
		self.pos += self.vel + self.mov
		self.acc = pygame.math.Vector2(0,0)
		self.mov = pygame.math.Vector2(0,0)


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
			walls[0] = True			
		elif self.pos.x + self.radius >= width:
			self.vel.x *= -self.elasticity
			self.pos.x -= 2*(self.pos.x+self.radius-width)
			self.vel.y *= 1-self.friction
			walls[1] = True
		if self.pos.y - self.radius <= 0:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y-self.radius)
			self.vel.x *= 1-self.friction
			walls[2] = True
		elif self.pos.y + self.radius >= height:
			self.vel.y *= -self.elasticity
			self.pos.y -= 2*(self.pos.y+self.radius-height)
			self.vel.x *= 1-self.friction
			walls[3] = True
		return walls


	def gravity(self):
		self.vel.y += self.floorGrav

	
	def force(self, other):
		diff = other.pos - self.pos
		dist = diff.magnitude()
		dir = diff.normalize() if dist > 0 else diff
		if dist > self.radius + other.radius:
			#gravity
			self.acc += dir * other.mass * self.bodyGrav / (dist**2)
			#repel
			self.acc -= dir * other.mass * self.repel / (dist**3)
			return
		if not self.collide: return

		# ball to ball collision
		msum = self.mass + other.mass
		denom = msum * dist * dist
		vdiff = other.vel - self.vel
		overlap = self.radius + other.radius - dist
		self.mov -= dir * overlap * (other.mass/msum)

		num = 2 * other.mass * vdiff.dot(diff)
		self.acc += diff * num/denom * (self.elasticity+1)/2
		
		# merging
		if self.merging and dist < self.radius:
			if not self.exist: return
			other.exist = False
			self.mass += other.mass
			self.radius = self.mass**0.5


	def display(self):
		col = (min(self.R, 255), min(self.G, 255), min(self.B, 255))
		pygame.draw.circle(self.screen, col, (int(self.pos.x), int(self.pos.y)), self.radius)
