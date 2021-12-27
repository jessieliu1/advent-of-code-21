from util.util import read_manual_instructions
import sys
import numpy as np

def first_fold(filename):
    paper, instructions = read_manual_instructions(filename)
    return int(np.sum(fold(paper, instructions[0])))

def fold(paper, instruction):
    hamburger = instruction[0] == "y"
    fold_pos = instruction[1]
    for idx, val in np.ndenumerate(paper):
        if paper[idx[0]][idx[1]] == 1:
            if hamburger:
                if idx[0] > fold_pos:
                    paper[idx[0]][idx[1]] = 0
                    paper[fold_pos - abs(idx[0]-fold_pos)][idx[1]] = 1
            else:
                if idx[1] > fold_pos:
                    paper[idx[0]][idx[1]] = 0
                    paper[idx[0]][fold_pos - abs(idx[1]-fold_pos)] = 1
    if hamburger:
        paper = paper[0:fold_pos, :]
    else:
        paper = paper[:, 0:fold_pos]
    return paper

def fold_all(filename):
    paper, instructions = read_manual_instructions(filename)
    for instruction in instructions:
        paper = fold(paper, instruction)
    paper = np.where(paper == 0, ".", paper)
    paper = np.where(paper == '1.0', "#", paper)
    return paper

def main():
    np.set_printoptions(linewidth=np.inf)
    if sys.argv[1] == "p1":
        print(first_fold(sys.argv[2]))
    else:
        print(fold_all(sys.argv[1]))

main()
