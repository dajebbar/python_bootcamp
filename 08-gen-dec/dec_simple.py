def simple_decorator (func):
    def wrapers(*args, **kwargs):
        print("Avant decorators")
        res = func(*args, **kwargs)
        print("Après decorators")
        return res
    return wrapers

@simple_decorator
def addition(x,y,z):
    return x+y+z
    
@simple_decorator
def greeting(name="Alba", age=32):
    if age < 18:
        return "Nop!"
    return f"Hi {name} your age is {age} ! welcome to club"


add1 = addition(45,-70, 12)
print(add1)

greet1 = greeting("daj", 12)
print(greet1)