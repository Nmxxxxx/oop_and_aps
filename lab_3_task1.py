class Businessman:

    def_name = 'Вася Пупкин'
    def_age = 30

    def __init__(self, name=None, age=None):
        self.name = self.def_name
        self.age = self.def_age
        self.__money = 1000000
        self.__business = None
    
    def info(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Деньги: {self.__money}, Бизнес: {self.__business}'
