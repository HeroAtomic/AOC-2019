
inst_index = 0
num1_index = 1
num2_index = 2
replace_index = 3

opcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

opcode[1] = 12
opcode[2] = 2

length = len(opcode)

instruction = opcode[inst_index]

#Read until we see halt
while instruction != 99:
    instruction = opcode[inst_index]
    #if we see a 1 we add
    if instruction ==1:
        value1 = opcode[num1_index]
        value1 = opcode[value1]

        value2 = opcode[num2_index]
        value2 = opcode[value2]

        replace = opcode[replace_index]

        value = value1 + value2
        opcode[replace] = value

        inst_index += 4
        num1_index = inst_index + 1
        num2_index = inst_index + 2
        replace_index = inst_index + 3

    if instruction == 2:
        value1 = opcode[num1_index]
        value1 = opcode[value1]

        value2 = opcode[num2_index]
        value2 = opcode[value2]

        replace = opcode[replace_index]

        value = value1 * value2
        opcode[replace] = value

        inst_index += 4
        num1_index = inst_index + 1
        num2_index = inst_index + 2
        replace_index = inst_index + 3

print('The value at position 0 is: {}'.format(opcode[0]))