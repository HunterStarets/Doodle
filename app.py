from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/view-post')
def index():
    return render_template('view-post.html')
