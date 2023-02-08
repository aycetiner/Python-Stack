from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

survey = satisfaction_survey

@app.route("/")
def index():
    """Homepage."""
    return render_template("home.html", survey = survey)

@app.route("/set_start", methods=["POST"])
def set_session_responses():
    """Sets the session for responses"""
    session["responses"] = []
    return redirect ("/questions/0")

@app.route("/questions/<int:question_id>")
def show_question(question_id):
    """Show the question for question id."""
    question = survey.questions[question_id]
    responses = session["responses"]

    if responses is None:
        return redirect("/")

    if len(responses)==len(survey.questions):
        return redirect ("/thankyou")

    if  len(responses) != question_id:
        flash(f"Invalid question id: {question_id}.")
        return redirect (f"/questions/{len(responses)}")
    
    
    return render_template("questions.html", survey = survey, question_id = question_id, question = question)

@app.route("/answers", methods=['POST'])
def handle_question():
    """Handle the answer from question"""
    new_answer = request.form.get('answerz', False)
    responses = session["responses"]
    responses.append(new_answer)
    session["responses"] = responses



    if len(responses)==len(survey.questions):
        return redirect ("/thankyou")

    else:
        return redirect (f"/questions/{len(responses)}")        

@app.route("/thankyou")
def show_thankyou():
    """Thank you."""
    return render_template("thank-you.html")