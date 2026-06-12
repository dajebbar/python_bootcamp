def silence(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except:
            return None
        return res
    return wrapper

@silence
def div_by_zero(a,b):
    return a / b
    
a = 1
b = 0
print(div_by_zero(a,b))