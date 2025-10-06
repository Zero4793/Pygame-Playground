from util.ball import Ball
import pygame
import math
import random
from pygame.math import Vector2
scale = 20

class Flow:
	def __init__(self, screen, _):
		global scale
		self.screen = screen

		w,h = screen.get_size()
		self.vel = [[Vector2(0,0) for j in range(h//scale)] for i in range(w//scale)]
		self.wind = (random.randint(0,len(self.vel)-1), random.randint(0,len(self.vel[0])-1), Vector2(random.randint(-100,100),random.randint(-100,100)))

		self.balls = [Ball(screen,pos=(50*i,40*i), vel=(0,0), spaceJelly=0.002, collide=True) for i in range(20)]


	def process(self):
		# wind
		wx,wy,wv = self.wind
		self.vel[wx][wy] += wv
		if random.randint(0,200) == 0:
			self.wind = (random.randint(0,len(self.vel)-1), random.randint(0,len(self.vel[0])-1), Vector2(random.randint(-100,100),random.randint(-100,100)))
		# random fluctiuations
		point = self.vel[random.randint(0,len(self.vel)-1)][random.randint(0,len(self.vel[0])-1)]
		unit = Vector2(10,0).rotate(random.randint(0,360))
		point += unit
		# add where click
		if pygame.mouse.get_pressed()[0]:
			x,y = pygame.mouse.get_pos()
			x = int(x/scale)
			y = int(y/scale)
			if x < len(self.vel) and y < len(self.vel[0]):
				self.vel[x][y] += wv
		
		# propagation
		avg = [[Vector2(0,0) for j in range(len(self.vel[0]))] for i in range(len(self.vel))]
		for i in range(len(self.vel)):
			for j in range(len(self.vel[i])):
				for x in range(max(0,i-1),min(len(self.vel),i+2)):
					for y in range(max(0,j-1),min(len(self.vel[i]),j+2)):
						avg[i][j] += self.vel[x][y]
				avg[i][j] /= 9
		for i in range(len(self.vel)):
			for j in range(len(self.vel[i])):
				self.vel[i][j] = avg[i][j]
		
		#Ball
		for ball in self.balls:
			bx,by = ball.pos
			bx = int(bx/scale)
			by = int(by/scale)
			ball.vel += self.vel[bx][by]/100
			ball.process()
			ball.wallCollide()
			for other in self.balls:
				if ball==other: continue
				ball.force(other)

		

	def display(self):
		global scale
		for i in range(len(self.vel)):
			for j in range(len(self.vel[i])):
				v = self.vel[i][j]
				pygame.draw.line(self.screen, (255,255,255), (i*scale+scale/2,j*scale+scale/2), (i*scale+scale/2+v.x,j*scale+scale/2+v.y), 1)
		#Ball
		[ball.display() for ball in self.balls]