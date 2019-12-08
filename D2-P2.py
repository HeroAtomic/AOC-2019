# This code sucks...BUT IT WORKS
import random

# Startin intcode, we will have to reset to this. We want it to be a tuple so we cannot change it in error
starting_incode = (1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0)

def restart():
    intcode = list(starting_incode)

    inst_pointer = 0
    par1_index = 1
    par2_index = 2
    replace_index = 3
    return intcode, inst_pointer, par1_index, par2_index, replace_index

def new_check():
    # For fun :D
    noun = random.randint(0,99)
    verb = random.randint(0, 99)
    return noun, verb

def fix_intcode(intcode, inst_pointer, par1_index, par2_index, replace_index):
    opcode = 0

    while opcode != 99:
        opcode = intcode[inst_pointer]

        intcode[1] = noun
        intcode[2] = verb

        # if we see a 1 we add
        # Get the next two values
        param1 = intcode[intcode[par1_index]]
        param2 = intcode[intcode[par2_index]]

        # Add them if opcode is 1
        if opcode == 1:
            #print('Adding')
            value = param1 + param2
        # Multiple them if opcode is 2
        elif opcode == 2:
            #print('Multiplying')
            value = param1 * param2

        # Replace the result
        intcode[intcode[replace_index]] = value

        # Move ahead 4 and reset the system
        inst_pointer += 4
        par1_index = inst_pointer + 1
        par2_index = inst_pointer + 2
        replace_index = inst_pointer + 3

        #print(intcode)

        result = intcode[0]
    return result

solution = 19690720



noun, verb = new_check()
intcode, inst_pointer, par1_index, par2_index, replace_index = restart()
result = fix_intcode(intcode, inst_pointer, par1_index, par2_index, replace_index)

while result != solution:
    noun, verb = new_check()
    intcode, inst_pointer, par1_index, par2_index, replace_index = restart()
    result = fix_intcode(intcode, inst_pointer, par1_index, par2_index, replace_index)
    print('Result:{} Noun:{} Verb:{}'.format(result, noun, verb))

print('\n')
print('This code is bent, never use this as an example')
print('We got the answer {}'.format(result))
print("The noun is: {} and the verb is {}".format(noun, verb))
print('The answer to the question 100*noun+verb is {}'.format(100*noun+verb))