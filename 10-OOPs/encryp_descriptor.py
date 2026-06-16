# Contexte : Vous voulez réutiliser une validation de chaîne de caractères partout. 
# Créez un descripteur NonEmptyString qui garantit qu’un attribut est une chaîne 
# non vide (après suppression des espaces).

# Consignes :

# Créez le descripteur NonEmptyString :

# Il reçoit un nom dans __init__ (pour stocker la clé dans __dict__).

# Dans __set__, vérifiez que value est une instance de str et 
# que value.strip() n’est pas vide. Sinon, levez ValueError avec un message explicite.

# Stockez la valeur dans instance.__dict__[self._nom] (n’oubliez pas le getter).

# Utilisez-le dans une classe Personne qui a deux attributs : 
# prenom et nom, tous deux utilisant le descripteur NonEmptyString.

# Ajoutez une propriété nom_complet (lecture seule) qui retourne "{prenom} {nom}".



class NonEmptyString:
    def __init__(self, name):
        self._stock = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dicit__.get(self._stock, None)
    
    def __set__(self, instance, value):
        value = value.strip()
        if not value or not isinstance(value, str):
            raise ValueError("Les chaînes vides ne sont pas acceptées ainsi que les types non chaîne.")
        instance.__dict__[self._stock] = value

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    nom = NonEmptyString("nom")
    prenom = NonEmptyString("prenom")

    @property
    def nom_complet(self):
        return f"{self.nom} {self.prenom}"