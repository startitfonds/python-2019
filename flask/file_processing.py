# a - Will append to the end of the file
# w - Will overwrite any existing content
# + - Will create a file if it does not exist 

file_name = 'file.txt'

def rewrite_file(lines):
  f = open(file_name, 'w')
  for line in lines:        
      f.write(line)
  f.close()

def write_file(param):
  f = open(file_name, 'a')
  f.write(param + '\n')
  f.close()

def read_file():
  f = open(file_name, 'r')
  if f.mode == 'r':
    contents = f.read()
  else:
    contents = f"Couldn't read from file {file_name}"

  return contents
    
def read_lines():
  with open(file_name) as f:
    lines_array = f.readlines()
  return lines_array