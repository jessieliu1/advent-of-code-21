from util.util import file_to_string_list
import sys

def compute_power_consumption(filename):
    binary_list = file_to_string_list(filename)
    if len(binary_list) == 0:
        return 0
    ints_by_position = [[] for i in range(len(list[position]))]
    for num in list:
        for i in range(0, len(num)):
            ints_by_position[i].append(int(num[i]))
    sums = [sum(list_index) for list_index in ints_by_position]
    gamma_rate_bin = ['1' if val >= len(binary_list)/2 else '0' for val in sums]
    epsilon_rate_bin = ['0' if val >= len(binary_list)/2 else '1' for val in sums]
    gamma_rate = int("".join(gamma_rate_bin), 2)
    epsilon_rate = int("".join(epsilon_rate_bin), 2)
    return gamma_rate * epsilon_rate

def compute_life_support_rating(filename):
    binary_list = file_to_string_list(filename)
    oxygen_rating = find_rating(binary_list, 0, lambda ints, list: 1 if (sum(ints) >= len(list) / 2) else 0)
    scrubber_rating = find_rating(binary_list, 0, lambda ints, list: 0 if (sum(ints) >= len(list) / 2) else 1)
    return scrubber_rating * oxygen_rating

def find_rating(binary_list, position, most_common_fn):
    if len(binary_list) == 1:
        return int(binary_list[0],2)
    ints_at_position = []
    for num in binary_list:
        ints_at_position.append(int(num[position]))
    most_common = most_common_fn(ints_at_position, binary_list)
    filtered_list = [binary_list[i] for i, val in enumerate(ints_at_position) if val == most_common]
    return find_rating(filtered_list, position+1, most_common_fn)

def main():
    if (sys.argv[1] == "life"):
        print(compute_life_support_rating(sys.argv[2]))
    else:
        print(compute_power_consumption(sys.argv[1]))

main()
