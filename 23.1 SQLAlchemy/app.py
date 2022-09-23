"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
connect_db(app)
db.create_all()


from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/")
def redirection():
    return redirect("/users")


@app.route("/users")
def list_users():
    """List users """
    users = User.query.order_by(User.first_name).all()
    posts = Post.query.order_by(Post.created_at.desc()).limit(5)
    return render_template("users.html", users=users, posts=posts)



@app.route("/users/new")
def new_user():
    """New user form """
    return render_template("new_user.html")

@app.route("/users/new", methods = ['POST'])
def handle_new_user():
    """Add new user """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect("/users")



@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)



@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Edit user """
    user = User.query.get_or_404(user_id)

    return render_template("edit_user.html", user=user)



@app.route("/users/<int:user_id>/edit", methods = ['POST'])
def handle_edit_user(user_id):
    """Add new user """
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User.query.get(user_id)
    user.edit(first_name, last_name, image_url)
    # db.session.add(user)
    db.session.commit()
    return redirect(f"/users/{user_id}")



@app.route("/users/<int:user_id>/delete", methods = ['POST'])
def handle_delete_user(user_id):
    """Add new user """

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return redirect("/users")


@app.route("/users/<int:user_id>/posts/new")
def new_post(user_id):
    """New post form """
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template("new_post.html", user=user, tags=tags)


@app.route("/users/<int:user_id>/posts/new", methods = ['POST'])
def handle_new_post(user_id):
    """Add new post """
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
    tag_ids = [int(tag) for tag in request.form.getlist('tags')]
    tags=Tag.query.filter(Tag.id.in_(tag_ids)).all()

    post = Post(title=title, content=content, user=user, tags=tags)
    db.session.add(post)
    db.session.commit()


    return redirect(f"/users/{user_id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show info on a single post."""

    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)




@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
    """Edit user """
    post = Post.query.get_or_404(post_id)

    return render_template("edit_post.html", post=post)



@app.route("/posts/<int:post_id>/edit", methods = ['POST'])
def handle_edit_post(post_id):
    """Edit post """
    title = request.form['title']
    content = request.form['content']

    post = Post.query.get_or_404(post_id)
    post.edit(title, content)

    db.session.commit()
    return redirect(f"/posts/{post_id}")


@app.route("/tags")
def list_tags():
    """List tags """
    tags = Tag.query.all()
    return render_template("tags.html", tags=tags)


@app.route("/tags/<int:tag_id>")
def show_tag_detail(tag_id):
    """Tag Detail """
    tag = Tag.query.get_or_404(tag_id)
    tag_posts = tag.posts
    return render_template("tag_detail.html", tag_posts=tag_posts, tag=tag)


@app.route("/tags/<int:tag_id>/delete", methods = ['POST'])
def handle_delete_tag(tag_id):
    """Delete tag """

    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    return redirect(f"/tags")


@app.route("/tags/<int:tag_id>/edit")
def edit_tag(tag_id):
    """Edit tags """
    tag = Tag.query.get_or_404(tag_id)
    return render_template("edit_tag.html", tag=tag)


@app.route("/tags/<int:tag_id>/edit", methods = ['POST'])
def handle_edit_tag(tag_id):
    """Edit tag """
    name = request.form['name']

    tag = Tag.query.get_or_404(tag_id)
    tag.edit(name)

    db.session.commit()
    return redirect(f"/tags/{tag_id}")


@app.route("/tags/new")
def new_tag():
    """New tag form """
    return render_template("new_tag.html")


@app.route("/tags/new", methods = ['POST'])
def handle_new_tag():
    """Add new post """
    name = request.form['name']

    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return redirect("/tags")


