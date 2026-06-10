def client(name):
    return f"Invoice for {name}:"

def items_menu(*items):
    result = "Items:\n"
    for item in items:
        result += f"- {item.capitalize()}\n"
    return result

def client_charges(**charges):
    result = "Charges:\n"
    for key,value in charges.items():
        result += f"- {key.capitalize()}: {value}\n"
    return result
    
def total_amount(**charges):
    res = 0
    for value in charges.values():
        res += value
    return f"Total Amount Due: {res}"
    
def generate_invoice(name="Guest", *items, **charges):
    print("# Output:")
    print(client(name))
    print(items_menu(*items))
    print(client_charges(**charges))
    print(total_amount(**charges))
    
    
    
generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0)
generate_invoice("Riya", tax=30.0)
generate_invoice()
generate_invoice("John", "Pizza", "Coke")