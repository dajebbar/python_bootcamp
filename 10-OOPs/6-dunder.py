class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class ListePersonnalisee:
    def __init__(self, elements):
        self.elements = elements
    
    def __len__(self):
        return len(self.elements)
    
    def __bool__(self):
        return any(self.elements)


class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, autre):
        if not isinstance(autre, Vecteur):
            raise TypeError("Addition uniquement avec un autre Vecteur")
        return Vecteur(self.x + autre.x, self.y + autre.y)
    
    def __radd__(self, autre):
        # autre est l'opérande de gauche (ex: 5)
        return self.__add__(autre) 

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"


class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, autre):
        if isinstance(autre, Vecteur):
            return Vecteur(self.x + autre.x, self.y + autre.y)
        elif isinstance(autre, (int, float)):
            return Vecteur(self.x + autre, self.y)
        else:
            return NotImplemented
            
        
    
    def __radd__(self, autre):
        return self.__add__(autre)
    
    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"
        

v = Vecteur(2, -5)
v2 = Vecteur(3, 1)
res = v + v2
print(res)
try:
    v3 = 5 + v
    print(v3)
except TypeError as e:
    print(f"Error: {e}")



pt = Point(3,4)
print(pt)
print(repr(pt))

l = ListePersonnalisee([0,1,3])
print(len(l))
print(bool(l))

l2 = ListePersonnalisee([0,0,0, 0])
print(len(l2))
print(bool(l2))

v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)
v3 = v1 + v2

