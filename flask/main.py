from flask import Flask, jsonify, request
import json

from werkzeug import secure_filename
import os

from lessons.lesson_1 import lesson_1
from lessons.lesson_2 import lesson_2
from lessons.lesson_3 import lesson_3
from lessons.lesson_4 import lesson_4
from lessons.lesson_5 import lesson_5
from lessons.lesson_6 import lesson_6

app = Flask(__name__)

app.register_blueprint(lesson_1)
app.register_blueprint(lesson_2)
app.register_blueprint(lesson_3)
app.register_blueprint(lesson_4)
app.register_blueprint(lesson_5)
app.register_blueprint(lesson_6)

uploads_dir = os.path.join(app.instance_path, 'uploads')
if not os.path.exists(uploads_dir):
  os.makedirs(uploads_dir)

@app.route('/file_upload', methods = ['POST'])
def file_upload():
  uploaded = request.files['file']
  
  uploaded.save(
    os.path.join(uploads_dir, secure_filename(uploaded.filename))
  )
  return 'File successfully uploaded!'

app.run(host='0.0.0.0', port=8020)
