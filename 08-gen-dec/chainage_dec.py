from functools import wraps

def majuscules(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return str(res).upper()
    return wrapper

def accolades(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"{{ {str(res)} }}"
    return wrapper


@majuscules
@accolades
def salutation(nom):
    return (f"bonjour {nom}")
    
print("{{}} vers MAJ")
print(salutation("Alice"))

@accolades
@majuscules
def salutation(nom):
    return (f"bonjour {nom}")
    
print("MAJ vers {{}}")
print(salutation("Bob"))