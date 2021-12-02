def file_to_int_list(filename):
   with open(filename, 'r') as file:
     input_lines = [int(line.strip()) for line in file]
     file.close()
     return input_lines
