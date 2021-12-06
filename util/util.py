import re

def file_to_int_list(filename):
   with open(filename, 'r') as file:
     input_lines = [int(line.strip()) for line in file]
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
