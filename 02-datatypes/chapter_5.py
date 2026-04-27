from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49
print(f"ideal temp: {ideal_temp}")
print(f"current temp: {current_temp}")
print(f"difference temp: {ideal_temp - current_temp}")

ideal_temp_dec = 95.5
current_temp_dec = 95.49
print(f"ideal temp dec: {ideal_temp_dec}")
print(f"current temp: {current_temp_dec}")
print(f"difference temp: {Decimal(ideal_temp_dec) - Decimal(current_temp_dec)}")