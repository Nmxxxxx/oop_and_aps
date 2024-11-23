class Businessman:

    def_name = 'Вася Пупкин'
    def_age = 30

    def __init__(self, name=None, age=None):
        self.name = self.def_name
        self.age = self.def_age
        self.__money = 50_000_000
        self.__business = None
    
    def info(self):
         print(f'Имя: {self.name}, Возраст: {self.age}, Деньги: {self.__money}, Бизнес: {self.__business}')
    
    @staticmethod
    def def_info():
         print(f'Стандратное Имя: {Businessman.def_name}, Стандартный Возраст: {Businessman.def_age}')
    
    def __make_deal(self, business, price):
        if self.__business is None:
            self.__business = business
            self.__money -= price
            print(f'Вы успешно сделали сделку с {business} за {price} рублей.')
        else:
            print('Вы уже сделали сделку с другим бизнесом.')
        
    def earn_money(self):
        if self.__business is not None:
            self.__money += 1000000
            print(f'Вы заработали 1кк рублей, и у вас стало {self.__money} рублей.')
        else:
            print('Вы не сделали ни одной сделки.')
        
    def buy_business(self, business, discount):
        price = business.final_price(discount)
        if self.__money >= price:
            self.__make_deal(business, price)
        else:
            print(f'Недостаточно денег для покупки бизнеса {business}')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)
    
class Business:
    def __init__(self):
        self._area = 0
        self._price = 0

    def final_price(self, discount):
        return self._price * (1 - discount)

class RestarauntBusiness(Business):
    def __init__(self, area=0, price=0):
        super().__init__()
        self._area = area
        self._price = price 
        self._profit = 50_000_000

Businessman.def_info()

businessman = Businessman()
businessman.info()

house = House(area=100, price=30000)
restaurant = RestarauntBusiness(area = 100, price=500_000)

businessman.buy_business(restaurant, discount=0.1)

businessman.earn_money()

businessman.info()

