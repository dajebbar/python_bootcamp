import time

def timer_chrono(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        res = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} a pris {fin-debut:.4f} secondes")
        return res
    return wrapper
    
@timer_chrono
def tache():
    time.sleep(.06 * 60)
    return "Terminé!"

print(tache())