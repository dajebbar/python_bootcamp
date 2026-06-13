from functools import wraps

def cache_results(func):
    cache_result = dict()
    @wraps(func)
    def wrapper(*args, **kwargs):
        cle_cache = args
        if cle_cache in cache_result:
            resultat_cache = cache_result[cle_cache]
            return f"From cache {resultat_cache}"
            
        result = func(*args, **kwargs)
        cache_result[cle_cache] = result
        return f"New calcul: {result}"
        
        
    return wrapper

@cache_results
def multiply(a, b):
    return a * b

print(multiply(5, 3))
print(multiply(12, 3))
print(multiply(5, 3))
        
        