from util.util import file_to_int_matrix
import sys
import numpy as np

def count_flashes(filename, steps):
    grid = np.array(file_to_int_matrix(filename))
    flash_count = 0
    for _ in range(steps):
        new_grid, new_count = grid_step(grid)
        flash_count += new_count
        grid = new_grid
    print(grid)
    return flash_count

def all_flash_step(filename):
    grid = np.array(file_to_int_matrix(filename))
    step = 0
    while True:
        step += 1
        new_grid, new_count = grid_step(grid)
        if new_count == grid.size:
            return step
        grid = new_grid

def grid_step(grid):
    flash_count = 0
    flashed = set()
    old_grid = np.copy(grid)
    iteration = 0
    while True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if iteration == 0:
                    grid[i][j] += 1
                if grid[i][j] > 9:
                    grid[i][j] = 0
                    flashed.add((i, j))
                    grid = flash_neighbors(grid, i, j, flashed)
                    flash_count += 1
        if np.array_equal(grid, old_grid):
            break
        old_grid = np.copy(grid)
        iteration += 1
    return (grid, flash_count)

def flash_neighbors(grid, row, col, flashed):
    if row - 1 >= 0 and (row-1, col) not in flashed:
        grid[row-1][col] += 1
    if row + 1 < len(grid) and (row+1, col) not in flashed:
        grid[row+1][col] += 1
    if col - 1 >= 0 and (row, col-1) not in flashed:
        grid[row][col-1] += 1
    if col + 1 < len(grid[row]) and (row, col+1) not in flashed:
        grid[row][col+1] += 1
    if row - 1 >= 0 and col - 1 >= 0 and (row-1, col-1) not in flashed:
        grid[row-1][col-1] += 1
    if row + 1 < len(grid) and col + 1 < len(grid[row]) and (row+1, col+1) not in flashed:
        grid[row+1][col+1] += 1
    if row - 1 >= 0 and col + 1 < len(grid[row]) and (row-1, col+1) not in flashed:
        grid[row-1][col+1] += 1
    if row + 1 < len(grid) and col - 1 >= 0 and (row+1, col-1) not in flashed:
        grid[row+1][col-1] += 1
    return grid

def main():
    if sys.argv[1] == "count":
        print(count_flashes(sys.argv[2], int(sys.argv[3])))
    else:
        print(all_flash_step(sys.argv[1]))

main()
