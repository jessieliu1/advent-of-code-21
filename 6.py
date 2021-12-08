from util.util import csv_to_int_list
import sys

def count_lanternfish(filename, days):
    lanternfish = csv_to_int_list(filename)
    for i in range(int(days)):
        lanternfish = simulate_day(lanternfish)
    return lanternfish

def simulate_day_brute_force(fish_list):
    add_fish = 0
    for i,fish in enumerate(fish_list):
        if fish == 0:
            fish_list[i] = 6
            add_fish += 1
        else:
            fish_list[i] -= 1
    for fish in range(add_fish):
        fish_list.append(8)
    return fish_list

def count_lanternfish_faster(filename, days):
    fish_list = csv_to_int_list(filename)
    fish_stats = [0 for _ in range(9)]
    for fish in fish_list:
        fish_stats[fish] += 1
    for j in range(int(days)):
        new_fish_stats = [0 for _ in range(9)]
        for i in range(len(fish_stats)-1, -1, -1):
            if i != 0:
                new_fish_stats[i - 1] = fish_stats[i]
            else:
                new_fish_stats[8] = fish_stats[0]
                new_fish_stats[6] += fish_stats[0]
        fish_stats = new_fish_stats
    return sum(fish_stats)

def main():
    print(count_lanternfish_faster(sys.argv[1], sys.argv[2]))

main()

# fish formula
# input: age, days
# days - initial days / 7 += 1
