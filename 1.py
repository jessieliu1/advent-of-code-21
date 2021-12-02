from util.util import file_to_int_list
import sys

def count_increased_depth(filename):
    depth_list = file_to_int_list(filename)
    count_increased_depth = 0
    for i in range(1, len(depth_list)):
        if depth_list[i] > depth_list[i-1]:
            count_increased_depth+=1
    return count_increased_depth

def count_increased_window(filename):
    depth_list = file_to_int_list(filename)
    count_increased_window = 0
    previous_sum = 0
    for i in range(1, len(depth_list)-2):
        window_sum = sum(depth_list[i:i+3])
        if window_sum > previous_sum:
            count_increased_window+=1
        previous_sum = window_sum
    return count_increased_window

def main():
    if sys.argv[1] == "window":
        print(count_increased_window(sys.argv[2]))
    else:
        print(count_increased_depth(sys.argv[1]))

main()
