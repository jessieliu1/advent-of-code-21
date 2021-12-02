def file_to_list(filename):
   with open(filename, 'r') as file:
     input_lines = [line.strip() for line in file]
     return input_lines
