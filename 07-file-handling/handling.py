# write in file (erase)
with open("example.txt", "w", encoding="utf-8") as f:
    for idx in range(10):
        f.write(f"This is line {idx+1}\n")


# add line in last
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("This is line 11")

# read all content
# with open("example.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# read line by line
with open("example.txt","r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())