from flask import Blueprint

lesson_1 = Blueprint('lesson_1', __name__)

@lesson_1.route('/')
def hello_world():
  return 'Hello world!'

@lesson_1.route('/about')
def about():
  return 'About page content.'

@lesson_1.route('/contact')
def contact():
  return 'Contact page content.'
