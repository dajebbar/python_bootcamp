from abc import ABC, abstractmethod

class MoyenPaiement(ABC):
    @abstractmethod
    def effectuer_paiement(self, montant):
        pass
    @abstractmethod
    def annuler_paiement(self, reference):
        pass

class CarteBancaire(MoyenPaiement):
    def __init__(self, numero, solde_disponible=1000):
        self._numero = numero
        self._solde = solde_disponible
    
    def effectuer_paiement(self, montant):
        if montant > self._solde:
            return False
        if montant <= 0:
            return False
        self._solde -= montant
        print(f"Paiement de {montant}€ effectué. Nouveau solde : {self._solde}€")
        return True
            
    def annuler_paiement(self, reference):
        print(f"Annulation du paiement {reference} sur la carte {self._numero}")


class PayPal(MoyenPaiement):
    def __init__(self, email):
        self._email = email
    
    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant}€ via PayPal ({self._email})")
        return True
    
    def annuler_paiement(self, reference):
        print(f"Annulation du paiement {reference} sur PayPal ({self._email})")

#di = CarteBancaire("0979654")
#try:
    #print(di.effectuer_paiement(25))
    #di.annuler_paiement("anno-5050432")
#except TypeError as e:
   # print(e)
    
cb = CarteBancaire("12323473")
pypl = PayPal("rob@gmc.com")

print(cb.effectuer_paiement(10))
cb.annuler_paiement("alice-18062026")

print(pypl.effectuer_paiement(45.55))
pypl.annuler_paiement("rob-10052026")

