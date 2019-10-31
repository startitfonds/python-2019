from flask import Blueprint, request, jsonify, render_template
from file_processing import read_file

lesson_6 = Blueprint('lesson_6', __name__)

@lesson_6.route('/get_file_content_based_on_request')
def get_file_content_based_on_request():
  request_type = request.content_type
  f = read_file()

  if (request_type == "application/json"):
    return jsonify(f)
  elif (request_type == "text/plain"):
    return f
  elif (request_type == "text/html"):
    return render_template(
      'lesson_4/with_params.html',
      args = f
    )
  else: 
    return f"Request type '{ request_type }' not supported!"
