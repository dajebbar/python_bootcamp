from abc import ABC, abstractmethod

class MoyenPaiement(ABC):
    @abstractmethod
    def traiter_paiement(self, montant):
        pass

class CarteCredit(MoyenPaiement):
    def __init__(self, numero_carte):
        self.numero_carte = numero_carte
    
    def traiter_paiement(self, montant):
        print(f"Débit de {montant}€ sur la carte {self.numero_carte}.")

class Paypal(MoyenPaiement):
    def __init__(self, email):
        self.email = email

cb = CarteCredit("123-3453")
cb.traiter_paiement(10)
try:
    pypl = Paypal("email@email.com")
except TypeError as e:
    print(f"Une erreur est surgit: {e}")

def encaisser_achat(moyen_de_paiement, total):
    moyen_de_paiement.traiter_paiement(total)

visa = encaisser_achat(CarteCredit("4970-XXXX-XXXX-XXXX"), 150)
visa
    