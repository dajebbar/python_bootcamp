with open("numbers.txt", "w", encoding="utf-8") as f:
    for idx in range(10):
        f.write(f"{idx+1}\n")

def sum_in_file(path):
    int_lst = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                int_lst.append(int(line))
    except(TypeError, FileNotFoundError, PermissionError) as e:
        print(f"An Error was occured -- {e}")
    else:
        return sum(int_lst)

print(sum_in_file('numbers.txt'))

def recorder():
    score = input("Enter notes (Decimal numbers)[fin to exit] >>> ")
    while True:
        if score == "fin":
            break
        else:
            try:
                score_float= float(score)
                with open("notes.txt", "a", encoding="utf-8") as f:
                    f.write(f"{score_float} \n")
                print(f"{score_float} enregistred.\n")

                score = input("Enter notes (Decimal numbers)[fin to exit] >>> ")
                
            except ValueError:
                print(f"{score} is not a decimal number")
                score = input("Enter notes (Decimal numbers) >>> ")

recorder()


def sum_in_file(path):
    lst = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                lst.append(float(line))
    except(TypeError, FileNotFoundError, PermissionError) as e:
        print(f"An Error was occured -- {e}")
    else:
        return f"{sum(lst) / len(lst):.2f}"

print(sum_in_file("notes.txt"))

def recorder():
    score = input("Enter notes (Decimal numbers)[fin to exit] >>> ")
    while True:
        if score == "fin":
            break
        else:
            try:
                score_float= float(score)
                with open("notes.txt", "a", encoding="utf-8") as f:
                    f.write(f"{score_float} \n")
                print(f"{score_float} enregistred.\n")

                score = input("Enter notes (Decimal numbers)[fin to exit] >>> ")
                
            except ValueError:
                print(f"{score} is not a decimal number")
                score = input("Enter notes (Decimal numbers) >>> ")
                
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error: {e}")

recorder()