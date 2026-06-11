store = [
    {
        "name":"Jellaba",
        "price": 1100,
        "category": "Couture"
    },
    {
        "name":"Benson",
        "price":1700,
        "category": "Monkes"
    },
    {
        "name":"Felix",
        "price": 13000,
        "category": "Watch"
    },
    {
        "name":"Caftan",
        "price": 4500,
        "category": "Couture"
    },
    {
        "name":"Benson",
        "price":2400,
        "category": "Monkes"
    },
    ]

'''for i in range(len(store)):
    if store[i]["price"] > 1500:
       print(store[i]["name"])
'''
      
      
article_name_great_than_1500 = [store[i]["name"] for i in range(len(store)) if store[i]["price"] > 1500]
print(article_name_great_than_1500)

uniq_categories = {store[i]["category"] for i in range(len(store))}
print(uniq_categories)

name_price = {store[i]["name"]:store[i]["price"] for i in range(len(store))}
print(name_price)

gen_of_price_discount = (store[i]["price"]-store[i]["price"]*0.3 for i in range(len(store)) if store[i]["price"] > 3000)
print(list(gen_of_price_discount))

