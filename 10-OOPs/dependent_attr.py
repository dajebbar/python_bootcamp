# Encapsulation & Propriétés Dépendantes (Niveau : Moyen)
# Objectif : Gérer la cohérence des données d'un objet en utilisant '
# 'des propriétés liées entre elles.Contexte : '
# 'Vous créez une classe Rectangle. Un rectangle possède une largeur'
# ' et une hauteur. '
# 'On veut pouvoir lire sa surface, mais aussi modifier la surface '
# 'directement (ce qui ajustera automatiquement la hauteur en gardant '
# 'la largeur fixe).Consignes :Créez la classe Rectangle avec deux '
# 'attributs privés __largeur et __hauteur (initialisés dans le __init__).'


# 'Créez des getters et setters pour largeur et hauteur. '
# 'Les setters doivent lever une ValueError si la valeur transmise est '
# 'inférieure ou égale à 0.
# 
# Créez une propriété @property appelée surface.Getter : '
# 'calcule et retourne la surface (largeur × hauteur).'

# 'Setter : reçoit une nouvelle surface. '
# 'Elle calcule la nouvelle hauteur nécessaire (hauteur = surface / largeur) '
# 'et met à jour l'attribut de hauteur en passant par son 
# setter (pour bénéficier de la validation > 0).

# Testez votre classe en créant un rectangle de 4 × 5 (surface = 20), 
# puis changez sa surface à 40 et vérifiez que sa hauteur est passée à 10.

class Rectangle:
    def __init__(self, largeur, hauteur):
        # avant setter
        # self.__largeur = largeur
        # self.__hauteur = hauteur
        # après setter
        self.largeur = largeur
        self.hauteur = hauteur
    
    # largeur
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self, val):
        if val <= 0:
            raise ValueError("La largeur doit être positive.")
        self.__largeur = val
    
    #hauteur
    @property
    def hauteur(self):
        return self.__hauteur
    
    @hauteur.setter
    def hauteur(self, val):
        if val <= 0:
            raise ValueError("La hauteur doit être positive.")
        self.__hauteur = val
    
    #surface
    @property
    def surface(self):
        return self.hauteur * self.largeur
    
    @surface.setter
    def surface(self, new_surface):
        self.hauteur = new_surface / self.largeur



rec = Rectangle(4, 5)
print(rec.surface)
rec.surface = 40
print(rec.hauteur)