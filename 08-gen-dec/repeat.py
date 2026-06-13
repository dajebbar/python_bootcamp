from functools import wraps

def repeter(n):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i+1}")
                res = func(*args, **kwargs)
            return res
        return wrapper
    return deco


@repeter(3)
def greeting(name):
    print(f"Hello {name}")

greeting("Alice")
print(greeting.__name__)

