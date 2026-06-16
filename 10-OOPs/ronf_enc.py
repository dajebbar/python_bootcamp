# Contexte : Vous gérez une classe Temperature. 
# La température interne doit toujours être stockée en degrés Celsius 
# (dans un attribut privé __celsius). Mais l’utilisateur doit pouvoir lire et modifier
# la température en Celsius ou en Fahrenheit, comme il le souhaite, via des propriétés.

# Consignes :

# Créez une classe Temperature avec :

# Un attribut privé __celsius (initialisé à 0 par défaut).

# Un getter @property pour celsius qui retourne __celsius.

# Un setter @celsius.setter qui :

# Accepte un nombre (int ou float).

# Lève ValueError si la valeur est inférieure à -273.15 (zéro absolu).

# Une propriété fahrenheit (getter et setter) :

# Getter : retourne (self.celsius * 9/5) + 32.

# Setter : reçoit une valeur en Fahrenheit, 
# la convertit en Celsius (formule inverse : (fahrenheit - 32) * 5/9) 
# et la stocke dans __celsius en passant par le setter de celsius 
# (c’est-à-dire en faisant self.celsius = valeur_en_celsius) 
# pour bénéficier de la validation du zéro absolu.

class Temperature:
    def __init__(self, degree=0):
        self.__celsius = degree
    
    #Lire la Temperature en celsius
    @property
    def celsius(self):
        return self.__celsius
    
    #Ecrire la Temperature en celsius
    @celsius.setter
    def celsius(self, new_temp):
        if not isinstance(self.__celsius, (int, float)) or self.__celsius < -273.15:
            raise ValueError ("La temperature ne peut dépasser le zéro absolu")
        self.__celsius = new_temp
    
    #Lire la Temperature en fahrenheit
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    #Ecrire la Temp en fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, fahren):
        self.celsius = (fahren - 32) * 5/9


