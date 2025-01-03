def factorial(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Нужно неотрицательное целое число")
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(2))
except ValueError as e:
    print(e)
