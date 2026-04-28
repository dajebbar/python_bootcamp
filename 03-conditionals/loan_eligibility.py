user_age = int(input("How old are you ? "))
income = float(input("Put your income: "))

if user_age >= 21:
    if income >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible: Income too low")
else:
    print("Not eligible: Age must be 21 or above")