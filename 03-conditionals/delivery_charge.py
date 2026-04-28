distance = int(input("Fill your distance(Km): "))

if distance <= 2:
    print("Delivery charge: 0")
elif 2 < distance <= 5:
    print("Delivery charge: 30")
elif 5 < distance <= 10:
    print("Delivery charge: 50")
elif distance > 10:
    print("Delivery not available for your location.")
else:
    print("Please check distance!")