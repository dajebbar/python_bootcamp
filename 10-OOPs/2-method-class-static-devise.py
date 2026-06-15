class CompteSimple:
    devise = "EUR"
    nb_comptes = 0
    
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        CompteSimple.nb_comptes += 1
    
    def deposer(self, montant):
        test_montant = CompteSimple.est_montant_valide(montant)
        if test_montant:
            print(f"Votre solde initial est de {self.solde}{CompteSimple.devise}. {montant}{CompteSimple.devise} seront ajoutées à votre compte")
            self.solde += montant
        else:
            print("Vous ne pouvez pas déposer un montant négatif")
            
    
    def retirer(self, montant):
        test_montant = CompteSimple.est_montant_valide(montant)
        if montant > self.solde:
            print(f"Votre solde de {self.solde}{CompteSimple.devise} est insuffisant pour l'opération")
        elif test_montant:
            self.solde -= montant
            print(f"{montant} {CompteSimple.devise} est retiré. Votre nouveau solde est {self.solde} {CompteSimple.devise}")
           
        else:
            print("Vous ne pouvez pas retirer un montant négatif")
            
    
    def afficher_solde(self):
        return f"Solde du titulaire {self.titulaire} est {self.solde} {CompteSimple.devise}"
    
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

c1 = CompteSimple("leila", 5480)
c2 = CompteSimple("rob")

print(CompteSimple.obtenir_nb_comptes())

CompteSimple.modifier_devise("MAD")
print(c1.afficher_solde())

c2.deposer(500)
print(c2.afficher_solde())

c2.retirer(50)
c1.deposer(-50)



#compte1.retirer(-400)
#compte2.deposer(400)
#compte1.deposer(-650)
#compte2.retirer(30.45)
#print(compte1.afficher_solde())
#print(compte2.afficher_solde())
#print(CompteSimple.nb_comptes)
