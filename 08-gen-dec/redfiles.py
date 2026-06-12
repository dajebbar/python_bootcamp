from collections import deque

def read_last_lines(filename, n):
    ensemble_file = deque(maxlen=n)
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            ensemble_file.append(line)
    for line in ensemble_file:
        yield line

filename="file.txt"
n = 20
gen = read_last_lines(filename, n)
for line in gen:
    print(line, end="")
