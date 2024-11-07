from util.button import Button
from apps.gravity import Gravity
from apps.musicalBalls import MusicalBalls
import pygame
import sys

class Menu:
	def __init__(self,screen,main):
		self.screen = screen
		self.main = main

		self.games = [
			("Gravity Sim", Gravity),
			("Musical Balls", MusicalBalls)
		]

		# buttons
		self.gameButtons = [Button(screen, main, (20,20+100*i), (160,80), [self.games[i][0]]*4, [(100,200,100), (150,250,150), (50,250,50), (0,250,0)]) for i in range(len(self.games))]
		self.exitButton = Button(screen, main, (1420,20), (160,80), ["Exit","Quit Game","Are you sure?","Quitting..."], [(150,100,100), (250,150,150), (250,50,50), (250,0,0)])
		# pos, dim, text[passive, hover, held, active], color[passive, hover, held, active]


	def process(self, keyheld, keypressed):
		# buttons
		for i,b in enumerate(self.gameButtons):
			b.process()
			if b.active:
				b.active = False
				self.main.window = self.games[i][1](self.screen)
		self.exitButton.process()
		# handle button actions externally
		# if self.gravSimButton.active:
		# 	self.gravSimButton.active = False
		# 	self.main.window = Gravity(self.screen)
		if self.exitButton.active:
			pygame.quit()
			sys.exit()


	def display(self):
		# buttons
		for b in self.gameButtons:
			b.display()
		self.exitButton.display()