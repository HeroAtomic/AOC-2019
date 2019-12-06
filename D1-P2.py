# Read the puzzle input into a file
f = open('D1-P1-input.txt', 'r')
module_masses = f.readlines()

index = 0
total_fuel = 0

for mass in module_masses:
    # Strip the \n out
    mass = mass.strip('\n')
    # Replace that value with the stripped value and increment the index
    module_masses[index] = int(mass)
    index += 1

for mass in module_masses:
    # As long as the mass is greater than 0
    while mass >= 0:
        # Fuel is mass/3 rounded down - 2
        fuel = int(int(mass)/3) - 2
        if fuel > 0:
            total_fuel += fuel
        mass = fuel

print('Total sum of fuel is: {}'.format(total_fuel))