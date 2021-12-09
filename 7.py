from util.util import csv_to_int_list
import sys

def minimum_fuel_position(filename):
    positions = csv_to_int_list(filename)
    pos_dict = {}
    min_value = positions[0]
    max_value = positions[0]
    for x in positions:
        if x in pos_dict:
            pos_dict[x] += 1
        else:
            pos_dict[x] = 1
        if x > max_value:
            max_value = x
        if x < min_value:
            min_value = x

    l_cost = 0
    r_cost = sum((k-min_value)*v for k,v in pos_dict.items())

    min_fuel = r_cost
    l_set_size = pos_dict[min_value]
    r_set_size = len(positions) - l_set_size
    min_position = 0

    for i in range(min_value + 1, max_value + 1):
        l_cost += l_set_size
        r_cost -= r_set_size
        if i in pos_dict:
            l_set_size += pos_dict[i]
            r_set_size -= pos_dict[i]
        if (l_cost + r_cost) < min_fuel:
            min_fuel = l_cost + r_cost
            min_position = i
    return min_fuel

def gaussian_cost(n):
    return ((n+1)*n)//2

def main():
    print(minimum_fuel_position(sys.argv[1]))

main()
