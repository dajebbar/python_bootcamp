class Employe:
    def __init__(self, nom, salaire_base):
        self._nom = nom
        self._salaire_base = salaire_base
    
    def calculer_paie(self):
        return self._salaire_base

class Manager(Employe):
    def __init__(self, nom, salaire_base, bonus):
        super().__init__(nom, salaire_base)
        self._bonus = bonus
    
    def calculer_paie(self):
        return super().calculer_paie() + self._bonus


m = Manager("Bob", 45000, 1400)
print(m.calculer_paie())