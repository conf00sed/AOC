import time

with open("day12.txt", "r") as fp:
    lines = [(move.strip()[0], int(move.strip()[1:])) for move in fp.readlines()]



##### PART 1 #####

# split lines into set
directions = {'E':0,'S':0,'W':0,'N':0}
heading = ['E', 'S', 'W', 'N','E', 'S', 'W', 'N','E', 'S', 'W', 'N', 'E', 'S', 'W', 'N','E', 'S', 'W', 'N','E', 'S', 'W', 'N', 'E', 'S', 'W', 'N','E', 'S', 'W', 'N','E', 'S', 'W', 'N']

# track current heading
f = 0

# iterate through notations
for move in lines:
    print()
    print(move, ' ', directions)

    # Forward
    if move[0] == 'F':
        directions[heading[f]] += move[1]
        print(f'facing: {heading[f]}')
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # Left
    elif move[0] == 'L':
        change = move[1] // 90
        f -= change
        print(f'facing: {heading[f]}')
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # Right
    elif move[0] == 'R':
        change = move[1] // 90
        f += change
        print(f'facing: {heading[f]}')
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # North
    elif move[0] == 'N':
        directions[move[0]] += move[1]
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # South
    elif move[0] == 'S':
        directions[move[0]] += move[1]
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # East
    elif move[0] == 'E':
        directions[move[0]] += move[1]
        print(f'new pos: {directions}')
        #time.sleep(5)
    
    # West
    elif move[0] == 'W':
        directions[move[0]] += move[1]
        print(f'new pos: {directions}')
        #time.sleep(5)

print(directions)
print(f" E - W = {directions['E'] - directions['W']}")
print(f" S - N = {directions['S'] - directions['N']}")
print(f"(E-W) + (S-N) = {abs(directions['E'] - directions['W']) + abs(directions['S'] - directions['N'])}")

import math

def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

coord = {'x': 0, 'y': 0}
waypoint = {'x': 10, 'y': 1}
for line in lines:
    instruction, n = line
    if instruction == 'N':
        waypoint['y'] += n
    elif instruction == 'S':
        waypoint['y'] -= n
    elif instruction == 'E':
        waypoint['x'] += n
    elif instruction == 'W':
        waypoint['x'] -= n
    elif instruction == 'F':
        coord['y'] += waypoint['y'] * n
        coord['x'] += waypoint['x'] * n
    elif instruction in ['L', 'R']:
        if instruction == 'R':
            n = -n
        waypoint['x'], waypoint['y'] = rotate(
            (0, 0), (waypoint['x'], waypoint['y']), math.radians(n)
        )
val = abs(coord['x']) + abs(coord['y'])