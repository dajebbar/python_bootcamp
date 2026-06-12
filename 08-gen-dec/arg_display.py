def affiche_args(func):
    def wrappers(*args, **kwargs):
        print("Args:")
        for arg in args:
            print(f"{arg}", end=",")
        print()
        print("Kwargs:")
        
        for k,v in kwargs.items():
            print(f"{k}:{v}")
        print()
        res = func(*args, **kwargs)
        
        return res
    return wrappers

@affiche_args
def test(name="Guest", tax=280, vat=20):
    print("--" * 6)
    return f"{name} paid ${tax + (tax*.2)}"

print(test("Alice", tax=2344, vat=30))
            