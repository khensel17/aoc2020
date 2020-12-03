#!/usr/bin/env python3

import sys

def checkTree(grid, x, y):
    if "#" in grid[x][y]:
        return True
    return False

def checkPath(grid,steps_down,steps_right):
    tree_counter = 0
    col = 0
    nextrow = 0
    for index, row in enumerate(grid):
        # Check only even rows to skip a row
        if (index != nextrow):
            continue
        if col > (len(grid[index]) - 1):
            col = (col - len(grid[index]))
        if checkTree(grid, index, col):
            tree_counter += 1
        col += steps_right
        nextrow = index + steps_down
    return tree_counter

def main():
    gridFile = open('grid', 'r')
    gridX = gridFile.read().splitlines()

    # Generate grid: two-dimensional array
    grid = []
    for i, value_i in enumerate(gridX):
        grid.append([])
        for value_j in list(value_i):
            grid[i].append([value_j])

    total_trees_1_1 = checkPath(grid, 1, 1)
    total_trees_1_3 = checkPath(grid, 1, 3)
    total_trees_1_5 = checkPath(grid, 1, 5)
    total_trees_1_7 = checkPath(grid, 1, 7)
    total_trees_2_1 = checkPath(grid, 2, 1)

    print("Right 1, down 1.: {}".format(total_trees_1_1))
    print("Right 3, down 1.: {}".format(total_trees_1_3))
    print("Right 5, down 1.: {}".format(total_trees_1_5))
    print("Right 7, down 1.: {}".format(total_trees_1_7))
    print("Right 1, down 2.: {}".format(total_trees_2_1))

    gridFile.close()

if __name__== "__main__":
  main()