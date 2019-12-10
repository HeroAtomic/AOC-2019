# Part2 solution broke part 1?

import csv
from copy import deepcopy
from datetime import datetime
import matplotlib.pyplot as plt

start_time = datetime.now()

def import_list(filename):
    with open (filename, 'r') as file:
        wire = []
        reader = csv.reader(file)
        for row in reader:
            wire.append(row)
        wire = wire[0]
    return wire
    print(wire)

    return wire1, wire2

def find_position(wire):

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

def find_full_path(wire):
    current_positions = []

    wire_path = wire
    i1 = 0
    i2 = 1
    try:
        # write every position from pos2 in path to pos 1
        for position in wire_path:

            pos1 = list(wire_path[i1])
            pos2 = list(wire_path[i2])


            #R or L
            while pos1 != pos2:
                if pos1[0] < pos2[0]:
                    pos1[0] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                elif pos1[0] > pos2[0]:
                    pos1[0] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                elif pos1[1] < pos2[1]:
                    pos1[1] += 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)
                elif pos1[1] > pos2[1]:
                    pos1[1] -= 1
                    current_pos = pos1[:]
                    current_positions.append(current_pos)

            # check next positions
            i1 += 1
            i2 += 1

    except:
        print('Wire path traced')
    return current_positions

def find_intersections():
    intersections = []
    steps = {}

    for i in w1:
        if i in w2:
            # Intersections
            print('Intersection found at:', i)
            intersections.append(i)

            # Steps to intersection
            #print(w1)
            #print(w2)
            w1_len = w1.index(i) + 1
            w2_len = w2.index(i) + 1
            total = w1_len + w2_len
            #print('Distance:', total)
            steps[str(i)] = total
    return intersections, steps

def find_manhattan():
    distances = []

    for i in intersections:
        dist = abs(i[0]) + abs(i[1])
        distances.append(dist)

    #distances.sort()
    return distances[0]


wire1 = import_list('wire1_input.txt')
wire2 = import_list('wire2_input.txt')

#wire1 = ['R8', 'U5', 'L5', 'D3']
#wire2 = ['U7', 'R6', 'D4', 'L4']

# find the turning point of each wire
#print('Finding path')
wire1_pos = find_position(wire1)
wire1_pos.insert(0, [0, 0])
#print('wire1 pos', wire1_pos)

wire2_pos = find_position(wire2)
wire2_pos.insert(0, [0, 0])
#print('wire2 pos', wire2_pos)


# Find the full path with every grid point
print('Tracing wires')
w1 = find_full_path(wire1_pos)
w2 = find_full_path(wire2_pos)

# Get the intersection points
print('Getting intersection points:')
intersections, steps = find_intersections()

key_min = min(steps.keys(), key=(lambda k: steps[k]))
steps_min = steps[key_min]

# Get the manhattan distance (the sum of the absolute values)
shortest_distance = find_manhattan()

print('\n')
print('Shortest path found!!')
print('The shortest manhattan distance to the intersection point is: {}'.format(shortest_distance))
print('Shortest amount of combined steps is: {}'.format(steps_min))

end_time = datetime.now()

print('Start time: {}'.format(start_time))
print('End time: {}'.format(end_time))
