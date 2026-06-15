class CompteSimple:
    devise = "EUR"
    nb_comptes = 0
    
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial
        CompteSimple.nb_comptes += 1
    
    def deposer(self, montant):
        if montant < 0:
            print("Vous ne pouvez pas déposer un montant négatif")
        else:
            print(f"Votre solde initial est de {self.solde}€. {montant}€ seront ajoutées à votre compte")
            self.solde += montant
    
    def retirer(self, montant):
        if self.solde < montant:
            print("Solde insuffisant")
        elif montant < 0:
            print("Vous ne pouvez pas retirer un montant négatif")
        else:
            self.solde -= montant
            print(f"{montant} est retiré. Votre nouveau solde est {self.solde}")
    
    def afficher_solde(self):
        return f"Solde du titulaire {self.titulaire} est {self.solde} {CompteSimple.devise}"

compte1 = CompteSimple("daj", 3000)
compte2 = CompteSimple("boz")

compte1.retirer(-400)
compte2.deposer(400)
compte1.deposer(-650)
compte2.retirer(30.45)
print(compte1.afficher_solde())
print(compte2.afficher_solde())
print(CompteSimple.nb_comptes)
