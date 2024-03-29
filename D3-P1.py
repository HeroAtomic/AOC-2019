# Me: Use functions you moron and don't just spagetti nest everything :)
# Me: Ok
import csv
from copy import deepcopy
from datetime import datetime

start_time = datetime.now()

def import_list(filename):
    with open (filename, 'r') as file:
        wire = []
        reader = csv.reader(file)
        for row in reader:
            wire.append(row)
        wire = wire[0]
    return wire

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
        print('Wire 1 path traced')
    return current_positions

def find_intersections():
    intersections = []

    for i in w1:
        if i in w2:
            print('Intersection found at:', i)
            intersections.append(i)
    return intersections

def find_manhattan():
    distances = []

    for i in intersections:
        dist = abs(i[0]) + abs(i[1])
        distances.append(dist)

    distances.sort()
    return distances[0]

wire1 = import_list('wire1_input_test.txt')
wire2 = import_list('wire2_input_test.txt')

# wire1 = ['R8', 'U5', 'L5', 'D3']
# wire2 = ['U7', 'R6', 'D4', 'L4']

# find the turning point of each wire
print('Finding path')
wire1_path = find_path(wire1)
wire2_path = find_path(wire2)

# Find the full path with every grid point
print('Tracing wires')
w1 = find_full_path(wire1_path)
w2 = find_full_path(wire2_path)

# Get the intersection points
print('Getting intersection points:')
intersections = find_intersections()
# Get the manhattan distance (the sum of the absolute values)
shortest_distance = find_manhattan()

print('\n')
print('Shortest path found!!')
print('The shortest distance to the intersection point is: {}'.format(shortest_distance))
end_time = datetime.now()
print('Start time: {}'.format(start_time))
print('End time: {}'.format(end_time))