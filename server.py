'''Use Flask to host a basic web server.'''

import os
import sys
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json

# Create the Flask app.
app = Flask(__name__)

@app.route('/')
def index():
    '''Return the index page.'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)