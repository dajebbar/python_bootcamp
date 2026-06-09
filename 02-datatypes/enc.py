# str = "Spécialisation".encode("utf-8").decode("utf-8")
# print(str)

import time

for number in range(4):
    print(f"Preparing chai for batch #[{number+1}]")
    if number < 3 :
        time.sleep(2 * 60)