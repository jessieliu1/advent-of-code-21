import re
import numpy as np

def file_to_int_list(filename):
   with open(filename, 'r') as file:
     input_lines = [int(line.strip()) for line in file]
     file.close()
     return input_lines

def csv_to_int_list(filename):
   with open(filename, 'r') as file:
     input_lines = file.readline().split(',')
     input_lines = [int(x) for x in input_lines]
     file.close()
     return input_lines

def file_to_tuple_list(filename):
    with open(filename, 'r') as file:
      input_lines = [tuple(line.strip().split()) for line in file]
      file.close()
      return input_lines

def file_to_string_list(filename):
    with open(filename, 'r') as file:
      input_lines = [line.strip() for line in file]
      file.close()
      return input_lines

def file_to_bingo(filename):
    with open(filename, 'r') as file:
      input_lines = [line.strip() for line in file]
      bingo_numbers = []
      boards = []
      current_board = []
      for i, line in enumerate(input_lines):
          if i == 0:
              bingo_numbers = line.split(',')
          if i > 1:
              if line == "":
                  boards.append(current_board)
                  current_board = []
              else:
                  current_board.append(re.split('\s+', line))
      boards.append(current_board)
      file.close()
      return [bingo_numbers, boards]

def file_to_vents(filename):
    with open(filename, 'r') as file:
      input_lines = [parse_vent(line.strip()) for line in file]
      file.close()
      return input_lines

def parse_vent(line):
    coords = line.split(' -> ')
    coord_list = []
    for coord in coords:
        segment = coord.split(',')
        int_segment = [int(x) for x in segment]
        coord_list.append(tuple(int_segment))
    return tuple(coord_list)

def read_signal_patterns(filename):
    with open(filename, 'r') as file:
        input_lines = [parse_note(line.strip()) for line in file]
        signal_patterns = []
        output_digits = []
        for line in input_lines:
            signal_patterns.append(line[0].split(' '))
            output_digits.append(line[1].split(' '))
        file.close()
        return (signal_patterns, output_digits)

def parse_note(line):
    note = line.split('|')
    return (note[0].strip(), note[1].strip())

def file_to_int_matrix(filename):
    with open(filename, 'r') as file:
        input_lines = [[int(char) for char in line.strip()] for line in file]
        file.close()
        return input_lines

def file_to_caves(filename):
    with open(filename, 'r') as file:
        adjacency = {}
        for line in file:
            line = line.strip()
            nodes = line.split("-")
            if nodes[0] not in adjacency:
                adjacency[nodes[0]] = set()
            adjacency[nodes[0]].add(nodes[1])
            if nodes[1] not in adjacency:
                adjacency[nodes[1]] = set()
            adjacency[nodes[1]].add(nodes[0])
        file.close()
        return adjacency

def read_manual_instructions(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        coords = []
        instructions = []
        max_x = 0
        max_y = 0
        while line.strip() != "":
            y, x = line.strip().split(',')
            coords.append((int(x), int(y)))
            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)
            line = file.readline()

        paper = np.zeros((max_x+1, max_y+1))
        for coord in coords:
            paper[coord[0]][coord[1]] = 1

        line = file.readline()
        while line:
            dir, num = line.strip()[11:].split("=")
            instructions.append((dir, int(num)))
            line = file.readline()
        file.close()
        return paper, instructions


def read_polymer_input(filename):
    with open(filename, 'r') as file:
        template = file.readline().strip()
        file.readline()
        rules = {}
        line = file.readline()
        while line:
            pair, insert = line.strip().split(" -> ")
            rules[pair] = insert
            line = file.readline()
        file.close()
        return template, rules
