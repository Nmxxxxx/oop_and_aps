def calculate_area(shape, *args):
    if shape not in ["круг", "квадрат", "прямоугольник", "треугольник"]:
        raise ValueError("Неверное название фигуры")
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("Аргументы должны быть числами")
    
    if shape == "круг":
        if len(args) != 1:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("Нужны положительные числовые аргументы")
            
        radius = args[0]
        return 3.14 * radius ** 2
    
    elif shape == "квадрат":
        if len(args) != 1:
            raise TypeError("Неверное количество аргументов")
        side = args[0]
        return side ** 2
    
    elif shape == "прямоугольник":
        if len(args) != 2:
            raise TypeError("Неверное количество аргументов")
        length, width = args
        return length * width
    
    elif shape == "треугольник":
        if len(args) != 2:
            raise TypeError("Неверное количество аргументов")
        base, height = args
        return 0.5 * base * height
    

shapes = [
    ("круг", 5),
    ("квадрат", 4),
    ("прямоугольник", 3, 4),
    ("треугольник", 5, 6),
    ("круг", "5"),
    ("квадрат", 4, 5),
    ("прямоугольник",  -5),
    ("квадрат", 5, 6)
]

for shape in shapes:
    try:
        print(f"Площадь для {shape[0]}: {calculate_area(*shape)}")
    except Exception as e:
        print(e)