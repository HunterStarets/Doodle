from flask import Flask, render_template, request, abort, redirect
#TODO move comment and post objects into appropriate folder and update imports
from post import Post
from comment import Comment

app = Flask(__name__)

#Mock Test Data


posts = [
    Post("Post Title 1", "user1", "d/community1", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
    Post("Post Title 2", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
    Post("Post Title 3", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
]

@app.route('/')
def index():
    #mock test data
    user = None 
    user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
    #final render
    return render_template('index.html', home_active=True, user=user, posts=posts)

@app.get('/view_post/<post_id>')
def view_post(post_id):
    #temporary
    post = find_post_by_id(post_id)

    #final render
    return render_template('view_post.html', post=post)

@app.get('/create_post_form')
def create_post_form():
    #final
    return render_template('create_post_form.html')

@app.get('/view_profile')
def view_profile():
    #get current user
    #get list of posts posted by that user
    # posts=users posts
    # user = current user
    #if not logged in return render_template(log_in.html)
    user = {'username': 'johndoe', 'profile_picture': 'https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg', 'summary': 'Short bio'}
    
    #mock test data
    posts = [
        Post("USER POST 1", "johndoe", "d/community132", [Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem"), Comment("user10", ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem")], ["upvote1"], ["downvote1", "downvote2"], 0, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
        Post("USER POST 2", "johndoe", "d/community13", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 1, "Malesuada proin libero nunc consequat interdum. Ac turpis egestas sed tempus urna et. Iaculis eu non diam phasellus vestibulum lorem sed. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Lorem donec massa sapien faucibus et molestie."),
        Post("USER POST 3", "johndoe", "d/community1222", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], 2, "Vitae purus faucibus ornare suspendisse sed. Eu feugiat pretium nibh ipsum consequat nisl vel. Interdum consectetur libero id faucibus nisl. Condimentum vitae sapien pellentesque habitant. Non nisi est sit amet facilisis magna etiam tempor orci."),
    ]
    
    return render_template('view_profile.html', view_profile_active=True, user=user, posts=posts)

#TEMPORARY TESTING FUNCTION
def find_post_by_id(post_id):
    post_id = int(post_id)
    try:
        post = posts[post_id]
    except:
        post = Post("Imaginary Post", "user1", "d/community1", ["comment1", "comment2"], ["upvote1"], ["downvote1", "downvote2"], -1, "Nisl condimentum id venenatis a condimentum. Enim neque volutpat ac tincidunt. At tempor commodo ullamcorper a lacus vestibulum sed. Commodo viverra maecenas accumsan lacus."),
    
    return post
