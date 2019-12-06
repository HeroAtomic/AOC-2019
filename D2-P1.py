inst_index = 0
num1_index = 1
num2_index = 2
replace_index = 3

intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

intcode[1] = 12
intcode[2] = 2

length = len(intcode)

opcode = intcode[inst_index]

#Read until we see halt
while opcode != 99:
    opcode = intcode[inst_index]
    #if we see a 1 we add
        # Get the next two values
    value1 = intcode[intcode[num1_index]]
    value2 = intcode[intcode[num2_index]]

    # Add them if opcode is 1
    if opcode ==1:
        value = value1 + value2
    # Multiple them if opcode is 2
    elif opcode ==2:
        value = value1 * value2

    # Replace the result
    intcode[intcode[replace_index]] = value

    # Move ahead 4 and reset the system
    inst_index += 4
    num1_index = inst_index + 1
    num2_index = inst_index + 2
    replace_index = inst_index + 3

print('The value at position 0 is: {}'.format(intcode[0]))