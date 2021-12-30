from util.util import file_to_int_matrix
from collections import defaultdict
import heapq as heap
import numpy as np
import sys
import time

def lowest_risk_path_full(filename):
    grid = create_full_grid(file_to_int_matrix(filename))
    return dijkstras(grid, (0,0))

def create_full_grid(grid):
    old_row_dim = len(grid)
    old_col_dim = len(grid[0])
    new_row_dim = old_row_dim * 5
    new_col_dim = old_col_dim * 5
    new_grid = np.empty([new_row_dim, new_col_dim])
    for row in range(new_row_dim):
        for col in range(new_col_dim):
            if row >= old_row_dim:
                new_grid[row][col] = new_grid[row - old_row_dim][col] + 1 if new_grid[row - old_row_dim][col] + 1 <= 9 else 1
            elif col >= old_col_dim:
                new_grid[row][col] = new_grid[row][col - old_col_dim] + 1 if new_grid[row][col - old_col_dim] + 1 <= 9 else 1
            else:
                new_grid[row][col] = grid[row][col]
    return new_grid

def lowest_risk_path(filename):
    grid = file_to_int_matrix(filename)
    return dijkstras(grid, (0,0))

def dijkstras(grid, start_idx):
    seen = set()
    cost = np.full((len(grid), len(grid[0])), float('inf'))
    cost[start_idx] = 0
    pq = []
    heap.heappush(pq, (0, start_idx))
    while (len(grid) - 1, len(grid[0]) - 1) not in seen:
        _, current_min_idx = heap.heappop(pq)
        i, j = current_min_idx
        if i - 1 >= 0 and (i - 1, j) not in seen:
            if grid[i-1][j] + cost[i][j] < cost[i-1][j]:
                cost[i-1][j] = grid[i-1][j] + cost[i][j]
                heap.heappush(pq, (cost[i-1][j], (i-1, j)))
        if i + 1 < len(grid) and (i + 1, j) not in seen:
            if grid[i+1][j] + cost[i][j] < cost[i+1][j]:
                cost[i+1][j] = grid[i+1][j] + cost[i][j]
                heap.heappush(pq, (cost[i+1][j], (i+1, j)))
        if j - 1 >= 0 and (i, j - 1) not in seen:
            if grid[i][j-1] + cost[i][j] < cost[i][j-1]:
                cost[i][j-1] = grid[i][j-1] + cost[i][j]
                heap.heappush(pq, (cost[i][j-1], (i, j-1)))
        if j + 1 < len(grid[i]) and (i, j + 1) not in seen:
            if grid[i][j+1] + cost[i][j] < cost[i][j+1]:
                cost[i][j+1] = grid[i][j+1] + cost[i][j]
                heap.heappush(pq, (cost[i][j+1], (i, j+1)))
        seen.add(current_min_idx)
    return cost[len(grid) - 1, len(grid[0]) - 1]

def main():
    if sys.argv[1] == "p1":
        print(lowest_risk_path(sys.argv[2]))
    else:
        print(lowest_risk_path_full(sys.argv[1]))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
