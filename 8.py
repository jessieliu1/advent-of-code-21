from util.util import read_signal_patterns
import sys
from collections import Counter

SEGS_TO_NUM = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

FREQ_DICTIONARY = {
    6: "b",
    4: "e",
    9: "f",
}

def count_unique(filename):
    (_,output) = read_signal_patterns(filename)
    unique_list = [2, 3, 4, 7]
    unique_counter = 0
    for line in output:
        for number in line:
            if len(number) in unique_list:
                unique_counter += 1
    return unique_counter

def sum_output(filename):
    (pattern,output) = read_signal_patterns(filename)
    output_sum = 0
    for i in range(len(pattern)):
        segment_map = {}
        freq_map = Counter({})
        one = ""
        four = ""
        for number in pattern[i]:
            if len(number) == 2:
                one = number
            if len(number) == 4:
                four = number
            freq_map += Counter(number)

        for k,v in freq_map.items():
            if v in FREQ_DICTIONARY:
                segment_map[k] = FREQ_DICTIONARY[v]
            elif v == 8:
                if k in one:
                    segment_map[k] = "c"
                else:
                    segment_map[k] = "a"
            elif v == 7:
                if k in four:
                    segment_map[k] = "d"
                else:
                    segment_map[k] = "g"

        output_num = ""
        for number in output[i]:
            number = list(number)
            for i in range(len(number)):
                number[i] = segment_map[number[i]]
            output_num += SEGS_TO_NUM["".join(sorted(number))]
        output_sum += int(output_num)
    return output_sum

def main():
    if (sys.argv[1] == "p1"):
        print(count_unique(sys.argv[2]))
    else:
        print(sum_output(sys.argv[1]))

main()
