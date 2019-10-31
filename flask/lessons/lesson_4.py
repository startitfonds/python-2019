from flask import Blueprint, render_template, request, jsonify

lesson_4 = Blueprint('lesson_4', __name__)

@lesson_4.route('/plain_params')
def plain_params():
  args = request.args
  return args

@lesson_4.route('/custom_object')
def custom_object():
  dictionary = { 'parameter': 'Parameter'}
  return str(dictionary)

@lesson_4.route('/custom_json')
def params_as_json():
  dictionary = { 'parameter': 'Parameter'}
  return dictionary

  return jsonify(
    parameter = 'Parameter'
  )

@lesson_4.route('/table_with_params')
def table_with_params():
  args = request.args

  for key, value in args.items():
      print(f"{key}: {value}")

  return render_template(
   'lesson_4/with_params.html',
   args = args
  )
