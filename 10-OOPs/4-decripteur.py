class PositiveNumber:
    def __init__(self, name):
        self._name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Le solde doit être un montant positif")
        instance.__dict__[self._name] = value

class Compte:
    solde = PositiveNumber("solde")

c = Compte()

try:
    c.solde = 100.50
    print(c.solde)
    
except ValueError as e:
    print(f"Erreur inattendue: {e}")

try:
    c.solde = 0
    print(c.solde)
    
except ValueError as e:
    print(f"Refusé: {e}")

try:
    c.solde = -50
    print(c.solde)
    
except ValueError as e:
    print(f"Refusé: {e}")