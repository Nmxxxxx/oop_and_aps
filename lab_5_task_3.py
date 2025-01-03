values = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]


res = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, values)))
print(res)