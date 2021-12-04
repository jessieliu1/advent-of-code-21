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
