from util.ball import Ball

class MusicalBalls:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(1,46):
			self.balls.append(Ball(screen,(10,20*i-10),(i/5,0),10,1,0,0,(200,min(i*5,255),200)))
		#screen, pos, vel, rad, elasticity, friction, airResistance, col


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()