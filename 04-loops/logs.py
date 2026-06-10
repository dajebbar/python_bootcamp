import random
import time

parcel_code = ["bar111", "bar0101", "bar4343", "DAMAGED", "barV2112", "STOP", "bar 0011"]
idx = 0
logs = []
while idx < len(parcel_code):
    bar = random.choice(parcel_code)
    if bar == "DAMAGED":
        print("Skipped damaged parcel")
        continue
    elif bar == "STOP":
        print("Critical error: Stopping scan")
        break
    else:
        print(f"Scanned parcel: <{bar}>.")
    idx += 1
    logs.append(bar)
    time.sleep(.05 * 60)

else:
    print("All parcels scanned successfully" )
print(logs)