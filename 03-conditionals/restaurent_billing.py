menus = {
    "classic":{
        "café": 1.50,
        "croissant": 3.20,
        "jus d'orange": 2.00
    },

    "energy":{
        "thé": 1.50,
        "pain complet": 0.80,
        "beurre": 0.50,
        "confiture": 0.60,
        "banane": 0.90
    },

    "gourmand":{
        "chocolat chaud": 2.20,
        "pain au chocolat": 3.40,
        "tartine beurre-confiture": 4.10,
        "kiwi": 0.80
    }
}

price_to_get_free_dessert = 5.5

breakfast = input("Please choose your breakfast:(classic, energy, gourmand)  ").lower()

print(f"Your choice was {breakfast}: {menus[breakfast]} , your total sum is: {sum(menus[breakfast].values())}€")
if sum(menus[breakfast].values()) > price_to_get_free_dessert:
    print("You get a free dessert!")
else:
    print("No free dessert this time.")