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