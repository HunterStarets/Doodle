from flask import Flask, render_template, request, abort, redirect
from post import Post

app = Flask(__name__)

posts = [
    Post("Post Title 1", "user1", "r/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"]),
    Post("Post Title 2", "user1", "r/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"]),
    Post("Post Title 3", "user1", "r/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"]),
]

@app.route('/')
def index():
    user = None 
    user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    return render_template('index.html', user=user, posts=posts)

@app.get('/view-post')
def view_post():
    return render_template('view-post.html')
