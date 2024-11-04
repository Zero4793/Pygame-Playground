import pygame
from button import Button

class Tile:
	def __init__(self, core, x, y, scale):
		self.button = Button(core,(x*scale+1, y*scale+1), (scale-2, scale-2), None, [(0),(50,50,50),(100,100,100),(100,250,100)])


	def process(self, x, y, scale):
		x*=scale
		y*=scale
		self.button.process()


	def display(self, screen, x, y, scale):
		x*=scale
		y*=scale
		# outline
		col = (255, 255, 255)
		pygame.draw.rect(screen, col, (x, y, scale, scale))
		self.button.display(screen)
