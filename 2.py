from util.util import file_to_tuple_list
import sys

def calculate_depth_vector_length(filename):
    directions = file_to_tuple_list(filename)
    parsed = [get_direction(x) for x in directions]
    horiz_sum = sum([y[0] for y in parsed])
    depth_sum = sum([y[1] for y in parsed])
    return horiz_sum * depth_sum

def calculate_depth_vector_length_aim(filename):
    directions = file_to_tuple_list(filename)
    aim = 0
    horizontal = 0
    depth = 0
    for dir in directions:
        change = get_direction_aim(dir, aim)
        horizontal += change[0]
        depth += change[1]
        aim += change[2]
    return horizontal * depth


# Return (horizontal change, depth change)
def get_direction(dir):
    match dir[0]:
        case "forward":
            return (int(dir[1]), 0)
        case "down":
            return (0, int(dir[1]))
        case "up":
            return (0, -int(dir[1]))
    return (0, 0)

# Return (horizontal change, depth change, aim change)
def get_direction_aim(dir, aim):
    match dir[0]:
        case "forward":
            return (int(dir[1]), int(dir[1])*aim, 0)
        case "down":
            return (0, 0, int(dir[1]))
        case "up":
            return (0, 0, -int(dir[1]))
    return (0, 0, 0)

def main():
    if sys.argv[1] == "aim":
        print(calculate_depth_vector_length_aim(sys.argv[2]))
    else:
        print(calculate_depth_vector_length(sys.argv[1]))

main()
