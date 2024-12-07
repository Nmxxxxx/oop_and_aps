

class Cell:
    def __init__(self, n):

        if n >= 0:
            self.n = n
        else:
            raise ValueError("Number of cells must be non-negative")
    def __add__(self, other):
        return Cell(self.n + other.n)
    
    def __sub__(self, other):
        return Cell(self.n - other.n)
    
    def __mul__(self, other):
        return Cell(self.n * other.n)
    
    def __truediv__(self, other):
        return Cell(round(self.n / other.n))
    

    def __str__(self):
        return f"Cell({self.n})"
    

c1 = Cell(5)
c2 = Cell(2)

print(c1 + c2)  # Output: Cell(7)

print(c1 - c2)  # Output: Cell(3)

print(c1 * c2)  # Output: Cell(10)

print(c1 / c2)  # Output: 2.5
