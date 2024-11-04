import pygame

class Name():
	def __init__(self, core, charClass):
		self.core = core
		self.charClass = charClass
		self.text = ''


	def process(self,keyheld, keypressed):
		if keypressed and keypressed in "abcdefghijklmnopqrstuvwxyz0123456789 ":
			if "left shift" in keyheld:
				self.text += keypressed.upper()
			else:
				self.text += keypressed
		if keypressed == "backspace":
			self.text = self.text[:-1]
		if keypressed == "space":
			self.text += " "
		if keypressed == "return":
			self.core.select.charCount -= 1
			self.core.select.playerChars.append((self.text, self.charClass))
			self.core.window = self.core.select


	def display(self,screen):
		font = pygame.font.Font(None, 48)
		text = font.render("Name: {0}".format(self.text), True, (250,250,250))
		screen.blit(text, (800-text.get_width()/2, 250))