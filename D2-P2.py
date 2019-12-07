import random

output = 19690720

instruction_pointer = 0
num1_index = 1
num2_index = 2
replace_index = 3

intcode_org = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

#noun and verb
noun = 12
verb = 2

intcode[1] = noun
intcode[2] = verb

length = len(intcode)

opcode = intcode[instruction_pointer]
param = 0


#Read until we see halt

while intcode[0] != output:
            opcode = intcode[instruction_pointer]
            #if we see a 1 we add
                # Get the next two params
            p1 = intcode[num1_index]
            p2 = intcode[num2_index]

            param1 = intcode[p1]
            param2 = intcode[p2]

            # Add them if opcode is 1
            if opcode ==1:
                print('Multiply')
                param = param1 + param2
                print('Add')
            # Multiple them if opcode is 2
            elif opcode ==2:
                param = param1 * param2
                print('Multiply')
            elif opcode ==99 or length < p1 or p2 or instruction_pointer or replace_index:
                print('HALT')
                intcode = intcode_org
                noun  = random.randint(0, 99)
                verb = random.randint(0, 99)

                intcode[1] = noun
                intcode[2] = verb

                instruction_pointer = 0
                num1_index = 1
                num2_index = 2
                replace_index = 3
            else:
                print('Invalid opcode')

            # Replace the result
            intcode[intcode[replace_index]] = param

            # Move ahead 4 and reset the system
            if length < p1 or p2 or instruction_pointer or replace_index:
                print('OUT OF RANGE')
                intcode = intcode_org
                noun  = random.randint(0, 99)
                verb = random.randint(0, 99)

                intcode[1] = noun
                intcode[2] = verb

                instruction_pointer = 0
                num1_index = 1
                num2_index = 2
                replace_index = 3
            else:
                instruction_pointer += 4
                num1_index = instruction_pointer + 1
                num2_index = instruction_pointer + 2
                replace_index = instruction_pointer + 3

            # Replace the result
            intcode[intcode[replace_index]] = param

            if intcode[0] == output:
                print('Got it')

            print(intcode)

print('The total at position 0 is: {}'.format(intcode[0]))

print('The noun is: {}, the verb is: {}'.format(noun,verb))
answer = 100 * noun + verb
print('The answer is: {}'.format(answer))
