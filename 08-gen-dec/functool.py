from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def addition(a, b): 
    """Retourne la somme""" 
    return a + b

res = addition(12, -4)
print(res)
print(addition.__doc__)
print(addition.__name__)