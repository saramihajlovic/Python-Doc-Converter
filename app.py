from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from converter import convert_file
import uuid

# create Flask app
app = Flask(__name__)

# configurations
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
ALLOWED_EXTENSIONS = {'txt', 'md', 'docx', 'html'}
OUTPUT_FORMATS = {'pdf', 'docx', 'html', 'txt', 'md'}

#apply configurations to Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def allowed_file(filename):
    # Check if the file has an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # renders the index.html main page to display uploaded file
    return render_template('index.html', formats=OUTPUT_FORMATS)

if __name__ == '__main__':
    app.run(debug=True)