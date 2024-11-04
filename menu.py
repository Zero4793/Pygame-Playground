from button import Button
from gravity import Gravity
import pygame
import sys

class Menu:
	def __init__(self,screen,core):
		self.screen = screen
		self.core = core

		# buttons
		self.gravSimButton = Button(screen, core, (20,100), (160,90), ["Gravity"]*4, [(100,200,100), (150,250,150), (50,250,50), (0,250,0)])
		self.exitButton = Button(screen, core, (20,190), (160,90), ["Exit","Quit Game","Are you sure?","Quitting..."], [(150,100,100), (250,150,150), (250,50,50), (250,0,0)])
		# pos, dim, text[passive, hover, held, active], color[passive, hover, held, active]


	def process(self, keyheld, keypressed):
		# buttons
		self.gravSimButton.process()
		self.exitButton.process()
		# handle button actions externally
		if self.gravSimButton.active:
			self.gravSimButton.active = False
			self.core.window = Gravity(self.screen)
		if self.exitButton.active:
			pygame.quit()
			sys.exit()


	def display(self):
		# buttons
		self.gravSimButton.display()
		self.exitButton.display()