def square_root(x):
    if x < 0:
        raise ValueError("Нельзя извлекать корень из отрицательного числа")
    else:
        return x ** 0.5
    
try:
    print(square_root(-2))
except ValueError as e:
    print(e)