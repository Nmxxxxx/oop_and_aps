class Ball:

    def __init__(self):
        self.name = 'Oval' # public

        self._radius = 5 # private
        self.__color = 'red' # protected

    def update_name(self, name):
        self.name = name
        print(f'Ball name updated to {self.name}')

    def _update_radius(self, radius):
        self._radius = radius
        print(f'Ball radius updated to {self._radius}')

    def __update_color(self, color):
        self.__color = color
        print(f'Ball color updated to {self.__color}')



    def default_color(self):
        print('default color')
        self.__update_color('red')


ball = Ball()

print(ball.name)

print(ball._radius)
# print(ball.__color)




ball.update_name('Circle')
ball._update_radius(10)
# ball.__update_color('green')

print(dir(ball))