import re

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

def file_to_heightmap(filename):
    with open(filename, 'r') as file:
        input_lines = [[int(char) for char in line.strip()] for line in file]
        file.close()
        return input_lines
