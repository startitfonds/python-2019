from flask import Blueprint, request, jsonify, render_template
from file_processing import write_file, read_file, read_lines, rewrite_file

lesson_5 = Blueprint('lesson_5', __name__)

@lesson_5.route('/post_request', methods = ['POST'])
def post_request():
  return request.args

@lesson_5.route('/write_to_file', methods = ['POST'])
def write_to_file():
  # value = request.args.get('value', default=0, type=int)
  # value = request.args.get('value', type=int)

  # value = request.args.get('value', default='string', type=str)
  value = request.args.get('value', type=str)

  received = value if value else "wrong"

  write_file(received)
  return f"Parameter '{received}' written to file!"

@lesson_5.route('/read_from_file')
def read_from_file():
  file_content = read_file()
  return file_content

@lesson_5.route('/read_and_write_to_file', methods = ['GET', 'POST'])
def read_and_write_to_file():
  if request.method == 'GET':
    return read_from_file()
  if request.method == 'POST':
    return write_to_file()

@lesson_5.route('/file_content_to_table')
def file_content_to_table():
  file_chars = read_from_file()
  file_lines = read_lines()

  # for char in file_chars:
  #   print(f"{char}")

  # for line in file_lines:
  #   print(f"{line}")

  # return file_chars
  # return file_lines

  # return jsonify(file_chars)
  # return jsonify(file_lines)

  return render_template(
   'lesson_4/with_params.html',
   args = file_lines
  )

@lesson_5.route('/line_from_file')
def line_from_file():
  file_lines = read_lines()
  line = int(request.args.get('line')) - 1

  print(len(file_lines))
  print(line <= len(file_lines))

  if line < len(file_lines) and line > 0:
    return file_lines[line]
  else:
    return 'Line does not exist'
  
@lesson_5.route('/delete_from_file', methods = ['DELETE'])
def put_to_file():
  file_lines = read_lines()
  line = int(request.args.get('line')) - 1

  if line < len(file_lines) and line > 0:
    file_lines.pop(line)
    rewrite_file(file_lines)
    return f"Line '{line + 1}' deleted from file!"
  else:
    return 'Line does not exist'
