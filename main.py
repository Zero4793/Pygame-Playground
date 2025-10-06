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


# Main program core
class Main:
	def __init__(self, screen):
		# init each window/focus
		self.menu = Menu(screen, self)
		self.window = self.menu # the active/running window/focus

		# buttons
		self.mouseTarget = None
		self.voidButton = Button(screen, self, (0,0), (1600,900), None, None) # does nothing itself. improves click detection
		self.exitButton = Button(screen, self, (1430,10), (160,40), ["Exit","Quit to menu","Are you sure?","Goodbye"], [(150,100,100), (250,150,150), (250,50,50), (250,0,0)])

		# keys
		self.keyheld = set()


	def process(self):
		# Handle events
		self.keypressed = None
		events = pygame.event.get()
		for event in events:
			# Quit the game
			if event.type == pygame.QUIT:
				return
			# track held and pressed keys
			if event.type == pygame.KEYDOWN:
				self.keyheld.add(pygame.key.name(event.key))
				self.keypressed = pygame.key.name(event.key)
			if event.type == pygame.KEYUP and pygame.key.name(event.key) in self.keyheld:
				self.keyheld.remove(pygame.key.name(event.key))
		if self.keypressed == "escape":
			if self.window != self.menu:
				self.window = self.menu
			else:
				pygame.quit()
				sys.exit()
		
		# run window
		self.window.process(self.keyheld, self.keypressed)

		# exit button
		if self.window != self.menu and dist(pygame.mouse.get_pos(),(1400,0))<250:
			self.exitButton.process()
			if self.exitButton.active:
				self.exitButton.active = False
				self.window = self.menu
		self.voidButton.process()


	def display(self):
		screen.fill(0)
		self.window.display()
		if self.window != self.menu and dist(pygame.mouse.get_pos(),(1400,0))<250:
			self.exitButton.display()
		pygame.display.flip() 
		clock.tick(60)


def dist(a,b):
	return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5


main = Main(screen)
while True:
	main.process()
	main.display()