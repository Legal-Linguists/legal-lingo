'''Use Flask to host a basic web server.'''

import os
import sys
from tkinter import LAST
from flask import Flask, render_template, request, redirect, url_for, flash
import json
# should already be installed with Flask (it's a dependency)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])
LAST_UPLOAD = 'last_upload.txt'

# Create the Flask app.
app = Flask(__name__)
app.secret_key = "super secret key"
# from https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def count_words(file_location):
    '''Return a dictionary of word counts for each word in the file.'''
    # Open the file.
    with open(file_location, 'r') as f:
        # Read the file.
        text = f.read()
        # Split the text into words.
        words = text.split()
        # Create a dictionary to hold the word counts.
        word_counts = {}
        # Loop through the words.
        for word in words:
            # If the word is in the dictionary, increment its count.
            if word in word_counts:
                word_counts[word] += 1
            # Otherwise, add the word to the dictionary with a count of 1.
            else:
                word_counts[word] = 1
        # Return the dictionary.
        return word_counts

# from https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    '''Return the index page.'''
    return render_template('index.html')

@app.route('/upload-file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # create a file holding the name of the location of the file
            # this is so that we can always find the name of the most recently uploaded file
            with open(LAST_UPLOAD, 'w') as f:
                f.write(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('display_word_counts', name=filename))
    return render_template('upload_file.html')

@app.route('/display-word-counts', methods=['GET', 'POST'])
def display_word_counts():
    if request.method == 'POST':
        # get the name of the most recently uploaded file
        with open(LAST_UPLOAD, 'r') as f:
            filename = f.read()
        # get the word counts for the file
        word_counts = count_words(filename)
        # convert the word counts to a JSON string
        word_counts_json = json.dumps(word_counts)
        # return the word counts to the browser
        return word_counts_json
    return render_template('display_word_counts.html')


if __name__ == '__main__':
    app.run(debug=True)