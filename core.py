import pygame
import sys

from button import Button
from menu import Menu


class Core:
	def __init__(self, screen):
		# init each window/focus
		self.menu = Menu(screen, self)
		self.window = self.menu # the active/running window/focus

		self.mouseTarget = None
		self.voidButton = Button(screen, self, (0,0), (1600,900), None, None) # does nothing itself. improves click detection


	def process(self, keyheld, keypressed):
		if keypressed == "escape":
			if self.window != self.menu:
				self.window = self.menu
			else:
				pygame.quit()
				sys.exit()
		self.window.process(keyheld, keypressed)
		self.voidButton.process()


	def display(self):
		self.window.display()
