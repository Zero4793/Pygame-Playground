import pygame
import sys
import os

from util.button import Button
from menu import Menu


# fix working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame and main screen
pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Pygame Playground')
clock = pygame.time.Clock()

def main():
	keyheld = set()
	game = Main(screen)

	while True:
		# Handle events
		keypressed = None
		events = pygame.event.get()
		for event in events:
			# Quit the game
			if event.type == pygame.QUIT:
				return
			# track held and pressed keys
			if event.type == pygame.KEYDOWN:
				keyheld.add(pygame.key.name(event.key))
				keypressed = pygame.key.name(event.key)
			if event.type == pygame.KEYUP and pygame.key.name(event.key) in keyheld:
				keyheld.remove(pygame.key.name(event.key))

		# update and render
		game.process(keyheld, keypressed)   
		screen.fill(0)
		game.display()
		pygame.display.flip() 
		clock.tick(60)


class Main:
	def __init__(self, screen):
		# init each window/focus
		self.menu = Menu(screen, self)
		self.window = self.menu # the active/running window/focus

		self.mouseTarget = None
		self.voidButton = Button(screen, self, (0,0), (1600,900), None, None) # does nothing itself. improves click detection
		self.exitButton = Button(screen, self, (1430,10), (160,40), ["Exit","Quit to menu","Are you sure?","Goodbye"], [(150,100,100), (250,150,150), (250,50,50), (250,0,0)])


	def process(self, keyheld, keypressed):
		if keypressed == "escape":
			if self.window != self.menu:
				self.window = self.menu
			else:
				pygame.quit()
				sys.exit()
		self.window.process(keyheld, keypressed)
		if self.window != self.menu:
			self.exitButton.process()
			if self.exitButton.active:
				self.exitButton.active = False
				self.window = self.menu
		self.voidButton.process()


	def display(self):
		self.window.display()
		if self.window != self.menu:
			self.exitButton.display()


main()
pygame.quit()
sys.exit()