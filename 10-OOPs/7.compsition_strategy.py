# Composition
class Moteur:
    def demarrer(self):
        print("Moteur démarré")

class Voiture:
    def __init__(self):
        self._moteur = Moteur()
    
    def demarrer(self):
        self._moteur.demarrer()


bmw = Voiture()
bmw.demarrer()

# pattern Stratégie
class PaiementPaypal:
    def paiement(self, montant):
        print(f"Vous avez payé {montant} via paypal.")

class PaiementCarte:
    def paiement(self, montant):
        print(f"Vous avez payé {montant} via CB.")

class Commande:
    def __init__(self, strategie_paiement):
        self. _strategie = strategie_paiement
    
    def effectuer_paiement(self, montant):
        return self. _strategie.paiement(montant)

commande = Commande(PaiementCarte())
commande.effectuer_paiement(100)

commande2 = Commande(PaiementPaypal())
commande2.effectuer_paiement(50)

        