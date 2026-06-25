class Chanson:
    def __init__(self, titre, artiste):
        self._titre = titre
        self._artiste = artiste
    
    def __str__(self):
        return f"{self._titre.capitalize()} - {self._artiste.capitalize()}"

class Playlist:
    # C 1 : On sépare clairement le nom de la playlist des chansons initiales (*chansons)
    def __init__(self, nom, *chansons):
        self._nom = nom
        # On convertit le tuple d'arguments *chansons en liste
        self._chansons = list(chansons)
    
    def ajouter(self, chanson):
        self._chansons.append(chanson)
        # Bonne pratique : ne pas retourner la liste complète lors d'un simple ajout
    
    def __len__(self):
        return len(self._chansons)
    
    def __getitem__(self, index):
        return self._chansons[index]

    # C 2 : Ajout de __str__ pour que print(playlist) affiche quelque chose de lisible
    def __str__(self):
        header = f"--- Playlist : {self._nom} ({len(self)} chansons) ---\n"
        # On utilise le fait que chaque chanson possède déjà sa méthode __str__
        liste_pistes = "\n".join(f"{i+1}. {chanson}" for i, chanson in enumerate(self._chansons))
        return header + liste_pistes


# --- ZONE DE TEST CORRIGÉE ---
song1 = Chanson("titre1", "artiste1")
song2 = Chanson("titre2", "artiste2")
song3 = Chanson("titre3", "artiste3")

# On donne un nom à la playlist ("Ma Super Liste"), puis les premières chansons
playlist = Playlist("Ma Super Liste", song1, song2)
playlist.ajouter(song3)

# Test de __len__
print(f"Nombre de chansons : {len(playlist)}\n")

# Test de __str__ (Affiche proprement toute la playlist)
print(playlist)

print("\n--- Test de la boucle for (Grâce à __getitem__) ---")
# Grâce à __getitem__, votre playlist est automatiquement itérable !
for piste in playlist:
    print(f"En écoute : {piste}")
