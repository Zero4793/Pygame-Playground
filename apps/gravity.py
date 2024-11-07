from util.ball import Ball

class Gravity:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(1,5):
			self.balls.append(Ball(screen))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()