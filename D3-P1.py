# Me: Use functions you moron and don't just spagetti nest everything :)
# Me: Ok
import csv
from copy import deepcopy

def import_list():
    with open ('wire1_input.txt', 'r') as file:
        wire1 = []
        reader = csv.reader(file)
        for row in reader:
            wire1.append(row)
        wire1 = wire1[0]

    with open ('wire2_input.txt', 'r') as file:
        wire2 = []
        reader = csv.reader(file)
        for row in reader:
            wire2.append(row)
        wire2 = wire2[0]

    return wire1, wire2

def find_path(wire):
    wire_path = []
    wire_pos = [0, 0]

    for dir in wire:
        if 'R' in dir:
            wire_pos[0] += int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'L' in dir:
            wire_pos[0] -= int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'U' in dir:
            wire_pos[1] += int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'D' in dir:
            wire_pos[1] -= int(dir[1:])
            wire_path.append(wire_pos[:])
        else:
            print("Something is wrong")

    return wire_path

def find_intersection():

    print(wire1_path)

    current_positions = []

    i1 = 0
    i2 = 1
    try:
        # write every position from pos2 in path to pos 1
        for position in wire1_path:

            pos1 = list(wire1_path[i1])
            pos2 = list(wire1_path[i2])


            #R or L
            while pos1 != pos2:
                if pos1[0] < pos2[0]:
                    pos1[0] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[0] > pos2[0]:
                    pos1[0] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[1] < pos2[1]:
                    pos1[1] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[1] > pos2[1]:
                    pos1[1] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)

                    print(current_pos)

            # check next positions
            i1 += 1
            i2 += 1

    except:
        print('end')
    return current_positions

def find_path(wire):
    wire_path = []
    wire_pos = [0, 0]

    for dir in wire:
        if 'R' in dir:
            wire_pos[0] += int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'L' in dir:
            wire_pos[0] -= int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'U' in dir:
            wire_pos[1] += int(dir[1:])
            wire_path.append(wire_pos[:])
        elif 'D' in dir:
            wire_pos[1] -= int(dir[1:])
            wire_path.append(wire_pos[:])
        else:
            print("Something is wrong")

    return wire_path

def find_intersection2():

    print(wire1_path)

    current_positions = []

    i1 = 0
    i2 = 1
    try:
        # write every position from pos2 in path to pos 1
        for position in wire2_path:

            pos1 = list(wire2_path[i1])
            pos2 = list(wire2_path[i2])


            #R or L
            while pos1 != pos2:
                if pos1[0] < pos2[0]:
                    pos1[0] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[0] > pos2[0]:
                    pos1[0] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[1] < pos2[1]:
                    pos1[1] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                    print(current_pos)
                elif pos1[1] > pos2[1]:
                    pos1[1] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)

                    print(current_pos)

            # check next positions
            i1 += 1
            i2 += 1

    except:
        print('end')
    return current_positions



wire1, wire2 = import_list()

#find the path of each and put it in a list
wire1_path = find_path(wire1)
wire2_path = find_path(wire2)

print('Path:', wire1_path)
#print(wire2_path)

w1 = find_intersection()
w2 = find_intersection2()

print('Wire 1:', w1)
print('Wire 2:', w2)

for i in w1:
    if i in w2:
        print('Intersection:', i)
