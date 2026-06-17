class Imprimante:
    def imprimer(self, texte):
        print(f"Impression : {texte}")

class Scanner:
    def scanner(self):
        return "Contenu numérisé"

class Photocopieuse(Imprimante, Scanner):
  
    def copier(self):
        super().imprimer(super().scanner())
        

pc = Photocopieuse()
pc.copier()

print(Photocopieuse.mro())