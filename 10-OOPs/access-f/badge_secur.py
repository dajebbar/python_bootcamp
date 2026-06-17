class DechiffrableMixin:
    def cle_secrete(self):
        return self._identifiant[::-1]

class CoffreFort(DechiffrableMixin):
    def __init__(self, identifiant, tresor):
        self._identifiant = identifiant
        self._tresor = tresor

class PorteBlindee(DechiffrableMixin):
    def __init__(self, identifiant, couleur):
        self._identifiant = identifiant
        self._couleur = couleur

coffre = CoffreFort("CF-990", "1000 pièces")
port = PorteBlindee("DOOR-A", "Gris")

print(coffre.cle_secrete())
print(port.cle_secrete())