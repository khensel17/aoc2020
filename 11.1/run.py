#!/usr/bin/env python3

import copy

def show_grid(grid):
    output = ""
    for i in range(0, len(grid)):
        line = ""
        for j in range(0,(len(grid[i - 1]))):
            line = line + grid[i][j][0]
        line = line + "\n"
        output = output + line
    return output

def apply_rules(grid):
    newgrid = copy.deepcopy(grid)
    # print(newgrid)
    X = len(grid) - 1
    Y = len(grid[0]) - 1

    neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                for y2 in range(y-1, y+2)
                                if (-1 < x <= X and
                                    -1 < y <= Y and
                                    (x != x2 or y != y2) and
                                    (0 <= x2 <= X) and
                                    (0 <= y2 <= Y))]
    for i in range(0, len(grid)):
        for j in range(0,(len(grid[i - 1]))):
            # print(neighbors(i, j))
            surr_seats_taken = 0
            for neighbor in neighbors(i, j):
                # print(neighbor[0])
                # print(neighbor[1])
                # print(grid[neighbor[0]][neighbor[1]])
                # print(grid[neighbor[0]][neighbor[1]])
                if "#" in grid[neighbor[0]][neighbor[1]]:
                    surr_seats_taken += 1
            # print(surr_seats_taken)
            if "L" in grid[i][j] and surr_seats_taken == 0:
                newgrid[i][j] = ["#"]
            elif "#" in grid[i][j] and surr_seats_taken >= 4:
                newgrid[i][j] = ["L"]
    return newgrid

def isDiff(a,b):
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] != b[x][y]:
                return True
    return False

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    grid = []
    for i, value_i in enumerate(data):
        grid.append([])
        for value_j in list(value_i):
            grid[i].append([value_j])
    return grid

def main():
    # grid = parse_input('example')
    grid = parse_input('input')

    # # print(grid)
    # print(show_grid(grid))
    # print("################################")

    new_grid = apply_rules(grid)
    # print(show_grid(new_grid))
    counter = 1
    while True:
        old_grid = copy.deepcopy(new_grid)
        new_grid = apply_rules(new_grid)
        # print(show_grid(new_grid))
        if isDiff(old_grid,new_grid):
            counter += 1
        else:
            print("Times generated: {}".format(counter))
            break

    num_seats_occupied = 0
    for x in range(len(new_grid)):
        for y in range(len(new_grid[x])):
            if "#" in new_grid[x][y]:
                num_seats_occupied += 1

    print("Total seats occupied: {}".format(num_seats_occupied))

if __name__=="__main__":
    main()