from abc import ABC, abstractmethod

class CryptoSystem(ABC):
    @abstractmethod
    def chiffrer(self, texte_claire):
        pass
    
    @abstractmethod
    def dechiffrer(self, texte_chiffre):
        pass

class InversionCrypto(CryptoSystem):
    def chiffrer(self, texte_claire):
        return texte_claire[::-1]
    
    def dechiffrer(self, texte_chiffre):
        return texte_chiffre[::-1]

class FauxCrypto(CryptoSystem):
    pass

class CesarCrypto(CryptoSystem):
    def __init__(self, decalage):
        self.decalage = decalage
    
    def chiffrer(self, texte_claire):
        return CesarCrypto.chiffrer_cesar(texte_claire, self.decalage)
    
    def dechiffrer(self, texte_chiffre):
        return CesarCrypto.chiffrer_cesar(texte_chiffre, -self.decalage)
    
    @staticmethod
    def chiffrer_cesar(texte, dec):
        resultat = ""
        for caractere in texte:
            if caractere.isalpha():
                debut = ord('A') if caractere.isupper() else ord('a')
                position = ord(caractere) - debut
                nouvelle_position = (position + dec) % 26
                resultat += chr(nouvelle_position + debut)
            else:
                resultat += caractere
        return resultat

ic = InversionCrypto()
cc = CesarCrypto(3)


msg = ic.chiffrer("Hello from Mars")
print(msg)
print(ic.dechiffrer(msg))
print()
txt_chiffrer = cc.chiffrer("Bonjour, Monde !")
print(txt_chiffrer)

txt_dechiffrer = cc.dechiffrer(txt_chiffrer)
print(txt_dechiffrer)
print()

def tester_securite(systeme, message):
    chif = systeme.chiffrer(message)
    print(chif)
    print(systeme.dechiffrer(chif))

tester_securite(CesarCrypto(5), "Hello from valhala !")

#test = FauxCrypto()

