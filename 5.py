from util.util import file_to_vents
from collections import defaultdict
import sys

def find_overlaps(filename):
    vent_coords = file_to_vents(filename)
    points = defaultdict(lambda: 0)
    for segment in vent_coords:
        ((x1, y1), (x2, y2)) = segment
        if x1 == x2 or y1 == y2:
            for i in range(0, abs(x2 - x1)+1):
                for j in range(0, abs(y2 - y1)+1):
                    delt_x = i if x2 >= x1 else -i
                    delt_y = j if y2 >= y1 else -j
                    points[(x1 + delt_x, y1 + delt_y)] += 1
    overlap_count = 0
    for _,v in points.items():
        if v > 1:
            overlap_count += 1
    return overlap_count

def find_overlaps_w_diag(filename):
    vent_coords = file_to_vents(filename)
    points = defaultdict(lambda: 0)
    for segment in vent_coords:
        ((x1, y1), (x2, y2)) = segment
        if x1 == x2 or y1 == y2:
            for i in range(0, abs(x2 - x1)+1):
                for j in range(0, abs(y2 - y1)+1):
                    delt_x = i if x2 >= x1 else -i
                    delt_y = j if y2 >= y1 else -j
                    points[(x1 + delt_x, y1 + delt_y)] += 1
        else:
            x_offset = 1 if x2 > x1 else -1
            y_offset = 1 if y2 > y1 else -1
            x_range = range(x1, x2+x_offset, x_offset)
            y_range = range(y1, y2+y_offset, y_offset)
            for coord in zip(x_range, y_range):
                points[coord] += 1
    overlap_count = 0
    for _,v in points.items():
        if v > 1:
            overlap_count += 1
    return overlap_count

def main():
    if (sys.argv[1] == "diag"):
        print(find_overlaps_w_diag(sys.argv[2]))
    else:
        print(find_overlaps(sys.argv[1]))

main()
