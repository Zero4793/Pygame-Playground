import pygame
from util.button import Button

class Clicker:
	def __init__(self, screen, main):
		self.screen = screen
		self.score = 0
		self.T = 0

		self.scoreButton = Button(self.screen, main, (800,450), (160,80), ['Score']*4, [(100,200,100), (150,250,150), (50,250,50), (0,250,0)])
		self.buttons = [Button(self.screen, main, (20+180*i,20), (160,80), [f'{i}']*4, [(100,200,100), (150,250,150), (50,250,50), (0,250,0)]) for i in range(8)]
		self.numbers = [0]*8
		self.costs = [10**(i+1) for i in range(8)]


	def process(self, keyheld, keypressed):
		self.T += 1
		if self.T % 1 == 0:
			self.T = 0
			self.score += self.numbers[0]/1000
			for i in range(7):
				self.numbers[i] += self.numbers[i+1] / 1000 #(10**(i+1))

		self.scoreButton.process()
		if self.scoreButton.active:
			self.scoreButton.active = False
			self.score += 1
		for i in range(len(self.buttons)):
			self.buttons[i].process()
			if self.buttons[i].active:
				self.buttons[i].active = False
				if self.score >= self.costs[i]:
					self.numbers[i] += 1
					self.score -= self.costs[i]


	def display(self):
		font = pygame.font.Font(None, 36)
		text = font.render(f"Score: {self.score:,.3f}", True, (250,250,250))
		self.screen.blit(text, (800-text.get_width()/2, 250))

		self.scoreButton.display()
		for i in range(len(self.buttons)):
			self.buttons[i].display()
			text = f'${self.costs[i]:,}'
			text = font.render(str(text), True, (200,200,200))
			self.screen.blit(text, (20+180*i,120))
			text = f'{self.numbers[i]:,.3f}'
			text = font.render(str(text), True, (200,200,200))
			self.screen.blit(text, (20+180*i,150))