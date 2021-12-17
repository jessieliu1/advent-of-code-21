from util.util import file_to_heightmap
import sys
import math

def sum_low_points(filename):
    heightmap = file_to_heightmap(filename)
    sum_low_points = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            current = heightmap[i][j]
            smaller = True
            if i - 1 >= 0:
                if heightmap[i-1][j] <= current:
                    smaller = False
            if i + 1 < len(heightmap):
                if heightmap[i+1][j] <= current:
                    smaller = False
            if j - 1 >= 0:
                if heightmap[i][j-1] <= current:
                    smaller = False
            if j + 1 < len(heightmap[i]):
                if heightmap[i][j+1] <= current:
                    smaller = False
            if smaller:
                sum_low_points += (current + 1)
    return sum_low_points

def find_low_points(heightmap):
    low_points = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            current = heightmap[i][j]
            smaller = True
            if i - 1 >= 0:
                if heightmap[i-1][j] <= current:
                    smaller = False
            if i + 1 < len(heightmap):
                if heightmap[i+1][j] <= current:
                    smaller = False
            if j - 1 >= 0:
                if heightmap[i][j-1] <= current:
                    smaller = False
            if j + 1 < len(heightmap[i]):
                if heightmap[i][j+1] <= current:
                    smaller = False
            if smaller:
                low_points.append((i, j))
    return low_points


def product_basins(filename):
    heightmap = file_to_heightmap(filename)
    low_points = find_low_points(heightmap)
    basin_sizes = []
    for point in low_points:
        basin = []
        seen = set()
        to_visit = []
        to_visit.append(point)
        seen.add(point)

        while to_visit:
            (i,j) = to_visit.pop(0)
            if heightmap[i][j] != 9:
                basin.append((i,j))
                if i - 1 >= 0 and (i-1, j) not in seen:
                    to_visit.append((i-1, j))
                    seen.add((i-1, j))
                if i + 1 < len(heightmap) and (i+1, j) not in seen:
                    to_visit.append((i+1, j))
                    seen.add((i+1, j))
                if j - 1 >= 0 and (i, j-1) not in seen:
                    to_visit.append((i, j-1))
                    seen.add((i, j-1))
                if j + 1 < len(heightmap[i]) and (i, j+1) not in seen:
                    to_visit.append((i, j+1))
                    seen.add((i, j+1))
        basin_sizes.append(len(basin))
    return math.prod(sorted(basin_sizes, reverse=True)[:3])

def main():
    print(product_basins(sys.argv[1]))

main()
