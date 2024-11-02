import numpy as np


class Ball:

    def __init__(self, end_time, color):
        self.color = color
        self.time = np.arange(0, end_time, 0.1)

    def move_ball(self, vx, vy):
        self.x = vx * self.time
        self.y = vy * self.time
        print(f'Координаты объекта \n(x: {self.x}, \n y: {self.y})')

class Football(Ball):

    def __init__(self, aerodynamics, color):
        super().__init__(end_time=10, color=color)
        self.aerodynamics = aerodynamics

    def fly(self):
        if self.aerodynamics == 'circle':
            print('True fly')
        else:
            print('Not play')


ball = Football(aerodynamics='circle', color='red')

ball.fly()

ball.move_ball(vx=10, vy=5)