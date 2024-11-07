import pygame

class Sprite:
	def __init__(self, path, dim, frameCount=1, frameRate=1):
		self.N = frameCount
		self.R = frameRate
		self.dim = dim
		if self.N == 1:
			self.image = [pygame.image.load(f'assets/{path}.png')]
			self.image[0] = pygame.transform.scale(self.image[0], dim)
		else:
			self.image = [None]*frameCount
			for i in range(frameCount):
				self.image[i] = pygame.image.load(f'assets/{path}{i}.png')
				self.image[i] = pygame.transform.scale(self.image[i], dim)
	

	def display(self, screen, x, y, F):
		I = (F // self.R) % self.N
		screen.blit(self.image[I], (x-self.dim[0]/2, y-self.dim[1]/2))
