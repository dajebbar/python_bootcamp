def filter_chai(commands, target):
    target_lower = target.lower()
    for command in commands:
        # print(f"{command} from filter1")
        if target_lower in command.lower():
            # print(f"{target_lower} from fitler---1")
            yield command

def analyze_orders(commands, target):
    gen = filter_chai(commands, target)
    
    count_masala = 0
    first_other_chai = None
    
    # On parcourt le générateur UNE SEULE FOIS
    for item in gen:
        # 1. On compte si c'est exactement "Masala chai" (insensible à la casse)
        if item.lower() == "masala chai":
            count_masala += 1
        
        # 2. Si ce n'est pas "Masala chai" et qu'on n'en a pas encore trouvé d'autre
        elif first_other_chai is None:
            first_other_chai = item

    # Affichage des résultats
    print(f"Nombre de 'Masala chai' : {count_masala}")
    
    if first_other_chai:
        print(f"Première autre commande filtrée : {first_other_chai}")
    else:
        print("Aucune autre commande correspondante n'a été trouvée.")

# --- Zone de test ---
commands = ["Masala chai", "Ginger chai", "Lemon chai", "Masala chai", "Earl Grey", "Masala chai"]
target = "Masala chai" # On cherche toutes les commandes qui contiennent "chai"

analyze_orders(commands, target)