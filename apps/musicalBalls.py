from util.ball import Ball
import util.SFX as SFX


class MusicalBalls:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(1,46):
			self.balls.append(Ball(screen,
						  pos=(10,20*i-10),
						  vel=(i/3,0)
						  ))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			walls = ball.wallCollide()
			if walls[0]: SFX.note(ball.vel.magnitude()*50, 0.1, 0.5, 1)
			if walls[1]: SFX.note(ball.vel.magnitude()*50, 0.1, 0.5, 0)
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		sx, sy = self.screen.get_size()
		for ball in self.balls:
			ball.R, ball.G, ball.B = (ball.pos.x/sx*255, 255-max(ball.pos.x/sx,ball.pos.y/sy)*255, ball.pos.y/sy*255)
			ball.display()