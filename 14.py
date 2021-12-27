from util.util import read_polymer_input
import sys
from collections import defaultdict

def n_steps(filename, n):
    template, rules = read_polymer_input(filename)
    pairs = defaultdict(int)
    letter_count = defaultdict(int)
    for i in range(len(template)):
        letter_count[template[i]] += 1
        if i > 0:
            if template[i-1:i+1] in rules:
                pairs[template[i-1:i+1]] += 1
    for _ in range(n):
        pairs, letter_count = step(template, rules, pairs, letter_count)

    return max(letter_count.values()) - min(letter_count.values())

def step(template, rules, pairs, letter_count):
    next_pairs = defaultdict(int)
    for pair, value in pairs.items():
        insertion = rules[pair]
        letter_count[insertion] += value
        if pair[0]+insertion in rules:
            next_pairs[pair[0]+insertion] += value
        if insertion+pair[1] in rules:
            next_pairs[insertion+pair[1]] += value
    return next_pairs, letter_count


def main():
    print(n_steps(sys.argv[1], int(sys.argv[2])))

main()
