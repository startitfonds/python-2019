from flask import Blueprint, render_template

lesson_3 = Blueprint('lesson_3', __name__)

@lesson_3.route('/about_template')
def about_template():
  return render_template(
    'lesson_3/about.html',
    active_page = 'about'
  )

@lesson_3.route('/contact_template')
def contact_template():
  return render_template('lesson_3/contact.html')
