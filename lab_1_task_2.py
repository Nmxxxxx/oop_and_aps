class Pyramid:

    total_h = 0
    def __init__(self, max_h, bricks_count=0):
        self.bricks = max_h
        self.bricks_count = bricks_count

    def add_bricks(self, num):

        try:
            if num <= 5:
                self.total_h += 1
            elif num > 5:
                print("Нельзя добавить более 5 кирпичей! \nПостройка разрушена!")
        except Exception as e:
            print("Ошибка:", e)
        
        
        self.bricks_count += num

    def get_height(self):
        print(f"Высота пирамиды: {self.total_h}")

    def is_done(self):
        self.res = (self.max_h / self.total_h) * 100
        if self.res == 100:
            exit(0)
        return self.res
    

class Builder:
    def __init__(self, bricks, my_pyramid):
        self.bricks = bricks
        self.my_pyramid = Pyramid(15)

    def buy_bricks(self):
        if self.bricks <= 0:
            bricks += 5

    def build_pyramid(self, n ):
        if self.bricks >= n:
            self.bricks -= n
            self.my_pyramid.add_bricks(n)
        else:
            print("Недостаточно кирпичей!")
            


        self.my_pyramid.add_bricks(self.bricks)
        self.my_pyramid.get_height()

    def work_day(self):   
        self.build_pyramid(5)
        self.my_pyramid.is_done()
        self.buy_bricks()
    
