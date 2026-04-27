customer = dict(name="John Doe", age=32, city="New york")
print(f"The customer info: {customer}")

customer.update(email="johndoe@gmx.com", phone="+132345")
print(f"The customer infos updated: {customer}")

print(f"customer name: {customer['name']}, customer city: {customer['city']}")


if 'name' in customer.keys():
    print(customer["name"])
else:
    print("Not found")

del customer["age"]
print(f"customer info updated: {customer}")

print(f"customer keys: {customer.keys()}")
print(f"customer values: {customer.values()}")
print(f"customer items: {customer.items()}")

last_item = customer.popitem()
print(f"This is the las item: {last_item}")

print(customer)
print(f"Is customer has a membership: {customer.get('membership', 'No membership')}")

customer.update(adress="221B Baker Street")
print()
print(customer)