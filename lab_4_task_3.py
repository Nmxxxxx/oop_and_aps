
import numpy as np

class ClassVector:

    def __init__(self, x, y, z):
        if all(isinstance(i, (int, float)) for i in (x, y, z)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Координаты должны быть числами (int или float).")

    def __len__(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)
    

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    

    def __repr__(self):
        return f"ClassVector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        if isinstance(other, ClassVector):
            return ClassVector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, ClassVector):
            return ClassVector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ClassVector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, ClassVector):
            return ClassVector(self.x * other.x, self.y * other.y, self.z * other.z)
        return NotImplemented
    def __radd__(self, scalar):
        return self.__add__(scalar)
    
    def __rsub__(self, scalar):
        if isinstance(scalar, ClassVector):
            return ClassVector(scalar - self.x, scalar - self.y, scalar - self.z)
        return NotImplemented
    def __rmul__(self, scalar):
        return ClassVector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __iadd__(self, other):
        if isinstance(other, ClassVector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        else:
            return NotImplemented
    
    def __isub__(self, other):
        if isinstance(other, ClassVector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        else:
            return NotImplemented
    
    def __imul__(self, scalar):
        if isinstance(scalar, (int, float)):
            self.x *= scalar
            self.y *= scalar
            self.z *= scalar
            return self
        else:
            return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, ClassVector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return NotImplemented
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __pow__(self, power):
        return ClassVector(self.x**power, self.y**power, self.z**power)


v1 = ClassVector(1, 2, 3)
v2 = ClassVector(4, 5, 6)

print(v1)            
print(repr(v1))     
print(v1 + v2)      
print(v1 - v2)     
print(v1 * 2)       
print(v1 * v2) 
