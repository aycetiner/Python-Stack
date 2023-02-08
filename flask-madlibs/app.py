from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"

debug = DebugToolbarExtension(app)


@app.route("/")
def get_home():
    """ Shows home page"""
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route("/story")
def get_story():
    """ Shows story page"""
    text = story.generate(request.args)
    return render_template('story.html', text=text)