"""Demo file showing off a model for BLOGLY."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(30),
                     nullable=False)

    last_name = db.Column(db.String(30),
                     nullable=False)

    image_url = db.Column(db.String(256), nullable=True, default=DEFAULT_IMAGE_URL)
    
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        """Show info about pet."""

        p = self
        return f"<User {p.id} {p.first_name} {p.last_name} {p.image_url}>"

    def edit(self, first_name, last_name, image_url):

        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    
class Post(db.Model):
    """ Posts """

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(30),
                     nullable=False)

    content = db.Column(db.String(256),
                     nullable=False)

    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

    tags =db.relationship('Tag', secondary='posttags', backref='posts')

    def edit(self, title, content):

        self.title = title
        self.content = content


class Tag(db.Model):
    """ Tag """

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(30),
                     nullable=False)


    def edit(self, name):

        self.name = name


class PostTag(db.Model):
    """ PostTag """

    __tablename__ = "posttags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True, nullable=False)

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True, nullable=False)

