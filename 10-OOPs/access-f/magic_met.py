class Sac:
    def __init__(self, **kwargs):
        self._contenu = {}
        for k,v in kwargs.items():
            self._contenu[k] = v
    
    def __repr__(self):
        elements = ','.join(f"{k} = {v}" for k,v in self._contenu.items())
        return f"Sac({elements})"
    
    def __str__(self):
        if not self._contenu:
            return "Sac vide"
        elements = ','.join(f"{k} x{v}" for k,v in self._contenu.items())
        return f"Contenu : {elements}"
    
    def __getitem__(self, nom):
        return self._contenu.get(nom, 0)
    
    def __setitem__(self, nom, quantite):
        if quantite <= 0:
            if nom in self._contenu:
                del self._contenu[nom]
        else:
            self._contenu[nom] = quantite
    
    def __delitem__(self, nom):
        if nom in self._contenu:
            del self._contenu[nom]
    
    def __len__(self):
        return sum(self._contenu.values())
    
    def __add__(self, autre_sac):
        if not isinstance(autre_sac, Sac):
            return NotImplemented
        nouveau = Sac()
        for k, v in self._contenu.items():
            nouveau[k] = v
            
        for k, v in autre_sac._contenu.items():
            nouveau[k] = nouveau[k] + v
        return nouveau
    
    def __iter__(self):
        return iter(self._contenu.keys())


# Test complet
s1 = Sac(pomme=3, banane=2)
s2 = Sac(pomme=1, orange=4)

print(repr(s1))          # Sac(pomme=3, banane=2)
print(s1)                # Contenu : pomme x3, banane x2

s3 = s1 + s2
print(repr(s3))          # Sac(pomme=4, banane=2, orange=4)

print(len(s1))           # 5

s1["pomme"] = 5
print(s1["pomme"])       # 5

for nom in s1:
    print(nom)           # pomme, banane

del s1["banane"]
print(s1)                # Contenu : pomme x5