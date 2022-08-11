'''Use Flask to host a basic web server.'''
#OCR 
import pandas as pd
import numpy as np
#Translate
from bs4 import BeautifulSoup
from urllib.error import HTTPError 
from typing import Text
import string 
import pickle 
import deepl
from pdf2image import convert_from_path
import easyocr
import numpy as np
from PIL import ImageDraw
from IPython.display import display, Image
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import os
from tkinter import LAST
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import csv

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])
LAST_UPLOAD = 'last_upload.txt'

# Create the Flask app.
app = Flask(__name__)
app.secret_key = "6c4114e5-49e5-7e61-2cd5-98d898d2a9a2:fx"
# from https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


'''OCR'''
def OCRModule():
    reader = easyocr.Reader(['en'])
    images= convert_from_path('uploads\simple one page rental agreement 02.pdf')
    for x in range(len(images)):
        display(images[x])
    bounds = reader.readtext(np.array(images[0]), min_size=0, slope_ths=0.2, ycenter_ths=0.7, height_ths=0.6, width_ths=0.8,decoder='beamsearch', beamWidth=10)
    def draw_boxes(image, bounds, color='yellow', width=2):
        draw = ImageDraw.Draw(images[0])
        for bound in bounds:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
        return image

    draw_boxes(images[0], bounds)
    text=''
    for i in range(len(bounds)):
        text = text + bounds[i][1] +'\n'

    sentences = sent_tokenize(text)
    text = []
    k = 0

    for i in sentences:
        text.append([i, k, ""])
        k = k + 1

    np.savetxt("Output.csv", 
            text,
            delimiter =", ", 
            fmt ='% s')
    with open('Output.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(text)


'''TRANSLATE MODULE'''
def Translate():
    f = open("combinedDict.pkl", "rb")
    dictionary = pickle.load(f)

        #dictionary1 = str(dictionary)
    def scan_csv(sample):
        definition = {}

        text = sample.read()
        text = text.translate(str.maketrans('','', string.punctuation))
        words = text.split()
        #' '.join(words) to make back into sentences

        for word in words:
            if word in dictionary:
                definition[word] = dictionary[word]
        return(definition) 

    doc1 = open("uploads/1098-.txt", "r")

    auth_key = "6155b4e1-0259-6e8f-2e92-e3439f845696:fx"  # Replace with your key
    translator = deepl.Translator(auth_key)

    result = translator.translate_text("Hello, world!", target_lang="ES")


def count_words(file_location):
    '''Return a dictionary of word counts for each word in the file.'''
    # Open the file.
    with open(file_location, 'r', encoding='unicode_escape') as f:
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
        def thing(sample):
            f = open("combinedDict.pkl", "rb")
            dictionary = pickle.load(f)
            definition = {}
            text = sample.read()
            text = text.translate(str.maketrans('','', string.punctuation))
            words = text.split()
            #' '.join(words) to make back into sentences
            for word in words:
                if word in dictionary:
                    definition[word] = dictionary[word]
            return(definition) 
        return redirect(url_for('display_word_counts', name=filename))
    return render_template('viewCSVoutput.html')

if __name__ == '__main__':
    app.run(debug=True)