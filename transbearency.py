#!/usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)
app.debug = False

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(port=8000)