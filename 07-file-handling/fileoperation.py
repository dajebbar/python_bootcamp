# Read file
# with open('textfiles.txt', 'r') as f:
#     content = f.read()
#     print(content)

# Read file line by line
# with open("textfiles.txt", 'r') as f:
#     for line in f:
#         print(line.strip())

# Writing in a file (overwriting)
# with open('textfiles.txt', 'w') as f:
#     f.write("Hello world !")

# with open('textfiles.txt', 'r') as f:
#     content = f.read()
#     print(content)

# Writing a list of lines in a file
lines = ["1st line\n", "2nd line\n", "3d line\n"]

with open('textfiles.txt', 'a') as f:
    f.writelines(lines)

with open('textfiles.txt', 'r') as f:
    content = f.read()
    print(content)