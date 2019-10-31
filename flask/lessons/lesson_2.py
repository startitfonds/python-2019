from flask import Blueprint, render_template

lesson_2 = Blueprint('lesson_2', __name__)

@lesson_2.route('/about_html')
def about():
  return render_template('lesson_2/about.html')

@lesson_2.route('/contact_html')
def contact():
  return render_template(
    'lesson_2/contact.html',
    parameter = "Passed parameter!"
  )
