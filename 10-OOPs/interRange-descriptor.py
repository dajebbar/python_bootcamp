class IntegerRange:
    def __init__(self, name, min_val, max_val):
        self._key = name
        self._min_val = min_val
        self._max_val = max_val
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("The score must be integer.")
        elif not self._min_val <= value <= self._max_val:
            raise ValueError(f"The score should be btw [{self._min_val} - {self._max_val}]")
            
        instance.__dict__[self._key] = value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._key, None)
        

class NoteScolaire:
    eleve = IntegerRange("note", 0, 20)


note = NoteScolaire()

try:
    note.eleve = 15
    print(note.eleve)
except Exception as e:
    print(f"unexpected error: {e}")

try:
    note.eleve = 25
except ValueError as e:
    print(f"Error detected: {e}")

try:
    note.eleve = "excellent"
except TypeError as e:
    print(f"Error detected: {e}")
    

        
