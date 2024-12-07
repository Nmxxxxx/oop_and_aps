
class StartSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
    
    def __len__(self):
        return len(self.planets)
    
    def __add__(self, other):
        planets_1 = self.planets[:]
        planets_1.append(other)
        return StartSystem(planets_1, self.name)
    
    def __radd__(self, other):
        planets_1 = self.planets[:]
        planets_1.insert(0, other)
        return StartSystem(planets_1, self.name)
    
    def __iadd__(self, other):
        self.planets.append(other)
        return self
    
    def __bool__(self):
        return len(self.planets) > 0
    
    def __str__(self):
        return f"StartSystem('{self.name}'): {self.planets}"
    
    def __getitem__(self, index):
        return self.planets[index]
    
    def __sub__(self, other):
        planets_1 = self.planets[:]
        planets_1.remove(other)
        return StartSystem(planets_1, self.name)
    
    def __rsub__(self, other):
        planets_1 = self.planets[:]
        planets_1.insert(0, other)
        return StartSystem(planets_1, self.name)
    
    def __isub__(self, other):
        self.planets.remove(other)
        return self

    

system = StartSystem(['Earth', 'Mars', 'Venus'], 'Solar System')

# Test the __len__ method

print(len(system))  

# Test the __add__ method

system = system + 'Jupiter'

print(system.planets)

# Test the __radd__ method

system = "TON_618" + system

print(system.planets)

# Test the __iadd__ method
system_1 = StartSystem(['Mercury', 'Uranus'], 'Giant Planet System')

system_1 += 'Neptune'
print(system_1.planets)


# Test the __bool__ method

print(bool(system))

print(bool(StartSystem([], 'Empty System')))

# Test the __str__ method

system_1 = StartSystem(['Mercury', 'Uranuasds'], 'Giant Planet System')
print(system_1)

# Test the __getitem__ method

print(system_1[0])

print(system_1[1])

print(system_1[-1])

# Test the __sub__ method

system_1 -= 'Mercury'
print(system_1.planets)

# Test the __rsub__ method

system_1 = StartSystem(['Mercury', 'Uranus'], 'Giant Planet System')

system_1 -= 'Uranus'
print(system_1.planets)

# Test the __isub__ method

system_1 = StartSystem(['Mercury', 'Uranus'], 'Giant Planet System')

system_1 -= 'Mercury'
print(system_1.planets)
