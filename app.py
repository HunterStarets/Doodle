from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/view_post')
def view_post():
    return render_template('view_post.html')

@app.get('/create_post_form')
def view_post_form():
    return render_template('create_post_form.html')