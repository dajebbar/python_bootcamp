class Guerrier:
    def attaquer(self):
        #print(f"from [{self.__class__.__name__}]")
        print("Donne un coup d'épée !")

class Magicien:
    def attaquer(self):
        #print(f"from [{self.__class__.__name__}]")
        print("Lance un sort de feu !")


class Paladin(Guerrier, Magicien):
    def attaquer(self):
        #print(f"from [{self.__class__.__name__}]")
        Guerrier.attaquer(self)
        Magicien.attaquer(self)
        

p = Paladin()
p.attaquer()

print(Paladin.mro())