import random
from functools import wraps

def max_fois(max_attemps):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for i in range(max_attemps):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_err = e
                    print(f"Essai {i + 1} échoué... On réessaie.")
            raise last_err
        return wrapper
    return deco


@max_fois(3)
def test(seuil = .9):
    if random.random() < seuil:
        raise ValueError("Échec du tirage !")
    return "Succès !"

for i in range(5):
    print(f"\n--- TEST N°{i+1} ---")
    try:
        print(test(0.7))
    except ValueError as err:
        print(f"Le décorateur a abandonné après 3 essais. Erreur finale : {err}")
