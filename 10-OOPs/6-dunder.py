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




pt = Point(3,4)
print(pt)
print(repr(pt))

l = ListePersonnalisee([0,1,3])
print(len(l))
print(bool(l))

l2 = ListePersonnalisee([0,0,0, 0])
print(len(l2))
print(bool(l2))

