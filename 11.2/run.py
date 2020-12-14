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

def get_neighbors(grid, x_value, y_value):
    X = len(grid) - 1
    Y = len(grid[0]) - 1
    neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                for y2 in range(y-1, y+2)
                                if (-1 < x <= X and
                                    -1 < y <= Y and
                                    (x != x2 or y != y2) and
                                    (0 <= x2 <= X) and
                                    (0 <= y2 <= Y))]
    output = neighbors(x_value, y_value)
    return output

def find_closest_seat(grid, neighbors, x, y):
    remove_indexes = []
    for index, neighbor in enumerate(neighbors):
        item = list(neighbor)
        while "." in grid[item[0]][item[1]] and (item[0] >= 0 and item[1] >= 0) and (item[0] <= len(grid) - 1 and item[1] <= len(grid[0]) - 1):
            if item[0] < x and item[0] >= 0 and item[0] <= len(grid) - 1:
                item[0] -= 1
            elif item[0] > x and item[0] >= 0 and item[0] <= len(grid) - 1:
                item[0] += 1
            if item[1] < y and item[1] >= 0 and item[1] <= len(grid[0]) - 1:
                item[1] -= 1
            elif item[1] > y and item[1] >= 0 and item[1] <= len(grid[0]) - 1:
                item[1] += 1
            neighbors[index] = tuple(item)
            if (item[0] < 0 or item[0] > len(grid) - 1) or (item[1] < 0 or item[1] > len(grid[0]) - 1):
                remove_indexes.append(index)
                break
    if len(remove_indexes) > 0:
        count = 0
        for i in remove_indexes:
            neighbors.pop(i - count)
            count += 1
    return neighbors

def apply_rules(grid):
    newgrid = copy.deepcopy(grid)
    for i in range(0, len(grid)):
        for j in range(0,(len(grid[i - 1]))):
            if "." not in grid[i][j]:
                neighbors_list = get_neighbors(grid, i, j)
                closest_seats = find_closest_seat(grid, neighbors_list, i, j)
                surr_seats_taken = 0
                for neighbor in closest_seats:
                    if "#" in grid[neighbor[0]][neighbor[1]]:
                        surr_seats_taken += 1
                if "L" in grid[i][j] and (surr_seats_taken == 0):
                    newgrid[i][j] = ["#"]
                elif "#" in grid[i][j] and (surr_seats_taken >= 5):
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

    print(show_grid(grid))
    print("################################")

    new_grid = apply_rules(grid)
    print(show_grid(new_grid))
    counter = 1
    while True:
        old_grid = copy.deepcopy(new_grid)
        new_grid = apply_rules(new_grid)
        print(show_grid(new_grid))
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