class CompteSimple:
    devise = "EUR"
    nb_comptes = 0
    
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self._solde = solde_initial
        CompteSimple.nb_comptes += 1
    
    def deposer(self, montant):
        test_montant = CompteSimple.est_montant_valide(montant)
        if test_montant:
            print(f"Votre solde initial est de {self._solde}{CompteSimple.devise}. {montant}{CompteSimple.devise} seront ajoutées à votre compte")
            self._solde += montant
        else:
            print("Vous ne pouvez pas déposer un montant négatif")
            
    
    def retirer(self, montant):
        test_montant = CompteSimple.est_montant_valide(montant)
        if montant > self._solde:
            print(f"Votre solde de {self._solde}{CompteSimple.devise} est insuffisant pour l'opération")
        elif test_montant:
            self._solde -= montant
            print(f"{montant} {CompteSimple.devise} est retiré. Votre nouveau solde est {self._solde} {CompteSimple.devise}")
           
        else:
            print("Vous ne pouvez pas retirer un montant négatif")
            
    
    def afficher_solde(self):
        return f"Solde du titulaire {self.titulaire} est {self._solde} {CompteSimple.devise}"
    
    @classmethod
    def obtenir_nb_comptes(cls):
        return cls.nb_comptes
    
    @classmethod
    def modifier_devise(cls,nouvelle_devise):
        cls.devise = nouvelle_devise
    
    @staticmethod
    def est_montant_valide(montant):
        if montant > 0:
            return True
        return False
    
    @property
    def solde(self):
        return self._solde
    
    @property
    def titulaire(self):
        return self._titulaire
    
    @titulaire.setter
    def titulaire(self, new_titulaire):
        if not new_titulaire or not new_titulaire.strip():
            raise ValueError("Le nom du titulaire est requis")
        self._titulaire = new_titulaire
        

c1 = CompteSimple("Aleina", 430)
c2 = CompteSimple("Amandine")

print(c1.solde)
try:
    c2.solde = 1000
except AttributeError as e:
    print(e)
    
try:
    c1.titulaire = " "
except ValueError as e:
    print(e)

c1.retirer(6)
c2.deposer(100)
print(c2.afficher_solde())

