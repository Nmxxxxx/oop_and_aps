class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.total_h = 0

    def add_bricks(self, num):
        while num > 0:
            required_bricks = self.max_h - self.total_h
            
            if self.total_h < self.max_h:
                if num >= required_bricks:
                    num -= required_bricks
                    self.bricks_count += required_bricks
                    self.total_h += 1
                else:
                    self.bricks_count += num
                    break  
            else:
                break

    def get_height(self):
        return self.total_h  # Возвращаем текущую высоту пирамиды

    def is_done(self):
        total_bricks = (self.max_h * (self.max_h + 1)) // 2
        res_bricks = (self.bricks_count / total_bricks) * 100
        return res_bricks


class Builder:
    def __init__(self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(15)

    def buy_bricks(self):
        self.bricks += 5
        print(f"Куплено 5 кирпичей. Теперь у строителя {self.bricks} кирпичей.")

    def build_pyramid(self, n):
        if self.bricks >= n:
            self.bricks -= n
            return n
        else:
            print("Недостаточно кирпичей!")
            return 0

    def work_day(self):
        needed_bricks = min(5, self.bricks + 5)  # Пытаемся использовать до 5 кирпичей
        added_bricks = self.build_pyramid(needed_bricks)
        

        if added_bricks > 0:
            self.my_pyramid.add_bricks(added_bricks)
        
        print(f"Строили пирамиду: добавлено {added_bricks} кирпичей.")
        print(f"Остаток кирпичей у строителя: {self.bricks}.")
        

        readiness = self.my_pyramid.is_done()
        print(f"Готовность пирамиды: {readiness:.2f}%.")  
        print(f"Высота пирамиды: {self.my_pyramid.get_height()}.")

        if readiness == 100:  
            print("Пирамида завершена!")
            exit(0)

        
        if added_bricks == 0:
            self.buy_bricks()


b = Builder(13)
day = 1

while True:
    print(f"День {day}:")
    b.work_day()
    day += 1