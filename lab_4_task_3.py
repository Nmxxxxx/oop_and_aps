
import numpy as np

class ClassVector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)
    

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    

    def __repr__(self):
        return f"ClassVector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return ClassVector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return ClassVector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return ClassVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __radd__(self, scalar):
        return ClassVector(self.x + scalar, self.y + scalar, self.z + scalar)
    
    def __rsub__(self, scalar):
        return ClassVector(scalar - self.x, scalar - self.y, scalar - self.z)
    
    def __rmul__(self, scalar):
        return ClassVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __pow__(self, power):
        return ClassVector(self.x**power, self.y**power, self.z**power)
    


