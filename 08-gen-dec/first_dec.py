def mon_decorateur(func):
    def wrapper():
        print("Avant")
        func()
        print("Après")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")