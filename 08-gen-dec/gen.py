def chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"


print(next(chai_gen()))
print(next(chai_gen()))
print(next(chai_gen()))

cup = chai_gen()
print(next(cup))
print(next(cup))
print(next(cup))