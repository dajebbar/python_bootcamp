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
        return instance.__dict__.get(self._stock, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, str) :
            raise ValueError("Le type doit être une chaîne de caractères.")
        
        value = value.strip()

        if not value:
           raise ValueError("La chaîne ne peut pas être vide.")
        
        instance.__dict__[self._stock] = value

class Personne:
    
    nom = NonEmptyString("nom")
    prenom = NonEmptyString("prenom")

    @property
    def nom_complet(self):
        return f"{self.nom} {self.prenom}"

p = Personne()
p.prenom = "  Alice  "  # doit stocker "Alice" (après strip)
p.nom = "Martin"
print(p.nom_complet)    # Alice Martin

try:
    p.nom = ""
except ValueError as e:
    print(e)  # erreur

try:
    p.prenom = "   "
except ValueError as e:
    print(e)  # erreur

# Bonus : testez l'accès via la classe
print(Personne.prenom)  # doit afficher le descripteur lui-même