try:
    with open("inexistant_file.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")