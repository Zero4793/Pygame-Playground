from util.ball import Ball

class MusicalBalls:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(1,46):
			self.balls.append(Ball(screen,
						  pos=(10,20*i-10),
						  vel=(i/5,0),
						  col=(200,min(i*5,255),200)))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			ball.wallCollide()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()