#!/usr/bin/env python3

import sys

def checkTree(grid, x, y):
    if "#" in grid[x][y]:
        return True
    return False

def checkNextPosition(curr_x, curr_y):
    print("Check next")

def main():
    gridFile = open('grid', 'r')
    gridX = gridFile.read().splitlines()

    tree_counter = 0

    # Generate grid: two-dimensional array
    grid = []
    for i, value_i in enumerate(gridX):
        grid.append([])
        for value_j in list(value_i):
            grid[i].append([value_j])

    col = 0
    for index, row in enumerate(grid):
        print(col)
        if col > (len(grid[index]) - 1):
            col = (col - len(grid[index]))
        print("Position x: {} y: {} | value: {}".format(index, col, grid[index][col]))
        if checkTree(grid, index, col):
            tree_counter += 1
        col += 3

    print("Total tree hits: {}".format(tree_counter))
    gridFile.close()

if __name__== "__main__":
  main()