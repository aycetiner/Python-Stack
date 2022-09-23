"""Seed file to make sample data for pets db."""

from models import User, Post, Tag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
Sparrow = User(first_name='Jack', last_name="Sparrow", image_url='')
Anonim = User(first_name='Senin', last_name="Anonim", image_url='')
Doe = User(first_name='John', last_name="Doe", image_url='')

# Add posts
Sparrowpost1 = Post(title='first post', content='helloo1', user_id=1)
Sparrowpost2 = Post(title='second post', content='helloo2', user_id=1)
Sparrowpost3 = Post(title='third post', content='helloo3', user_id=1)
Anonimpost1 = Post(title='first_post', content='helloo1', user_id=2)

# Add tags
tag1 = Tag(name='Fun')
tag2 = Tag(name='Even More')
tag3 = Tag(name='Bloop')

# Add tags then commit
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

db.session.commit()

# Add new objects to session, so they'll persist
db.session.add(Sparrow)
db.session.add(Anonim)
db.session.add(Doe)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add posts then commit
db.session.add(Sparrowpost1)
db.session.add(Sparrowpost2)
db.session.add(Sparrowpost3)
db.session.add(Anonimpost1)

db.session.commit()

# appending tags to posts
Sparrowpost1.tags.append(tag1)
Sparrowpost1.tags.append(tag2)
Sparrowpost2.tags.append(tag1)
Anonimpost1.tags.append(tag3)

db.session.commit()