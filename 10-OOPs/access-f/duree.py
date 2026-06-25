class Duree:
    def __init__(self, minutes, secondes):
        if secondes > 59:
            minutes += secondes // 60
            self._secondes = secondes % 60
            self._minutes = minutes
        else:
            self._minutes = minutes
            self._secondes = secondes
    
    def __repr__(self):
        return f"Duree(minutes={self._minutes}, secondes={self._secondes})"
    
    def __str__(self):
      return f"{self._minutes:02d}m {self._secondes:02d}s"
    
    def __add__(self, autre):
        if not isinstance(autre, Duree):
            return NotImplemented
        
        return Duree(self._minutes+autre._minutes, self._secondes+autre._secondes)
        
        
    

x = Duree(2, 95)
print(x)
print(repr(x))
y = Duree(1, 73)
print(x+y)