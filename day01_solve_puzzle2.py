"""
So, for each module mass, calculate its fuel and add it to the total. 
Then, treat the fuel amount you just calculated as the input mass and repeat the process, 
continuing until a fuel requirement is zero or negative.
"""

def calculate_fuel(mass):
    return int(mass / 3) - 2

def calculate_fuels_fuel(mass):
    fuel = calculate_fuel(mass)
    if fuel > 0:
        return fuel + calculate_fuels_fuel(fuel)
    else:
        return 0


assert calculate_fuels_fuel(14) == 2
assert calculate_fuels_fuel(1969) == 966
assert calculate_fuels_fuel(100756) == 50346

with open("input01.txt") as f:
    lines = f.readlines()
    result = sum([calculate_fuels_fuel(int(mass)) for mass in lines])

print(result)