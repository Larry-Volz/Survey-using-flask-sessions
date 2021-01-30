from surveys import *
from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config['SECRET_KEY'] = 'FOO'
app.debug=True
debug=DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


responses = []
# question_idx = 0
title = satisfaction_survey.title
instructions = satisfaction_survey.instructions
questions = [question.question for question in satisfaction_survey.questions]
choices = [question.choices for question in satisfaction_survey.questions]
for i in range(len(questions)):
    print(questions[i])

# for i in range(len(satisfaction_survey.questions)):
#     print(satisfaction_survey.questions.question.values())

question_idx = 0
counter = 0
TOTAL_NUM_QUESTIONS=len(questions)


@app.route('/')
def survey_start_page():
    global question_idx
    global responses
    responses=[]
    if question_idx >= TOTAL_NUM_QUESTIONS:
        question_idx = 0
    return render_template('index.html', survey_title=title, survey_instructions=instructions)


@app.route('/questions/<int:question_idx>', methods=["GET","POST"])
def questions_page(question_idx):
    global TOTAL_NUM_QUESTIONS
    global questions
    print(f"question_idx: {question_idx}")

    if question_idx != len(responses):
        #FLASH 'incorrect address: please answer all the questions in order
        flash("incorrect address: please answer all the questions in order", 'error')
        question_idx = len(responses)
        redirect('/questions/<int:question_idx>')

    if question_idx < TOTAL_NUM_QUESTIONS:
        current_question=questions[question_idx]
        return render_template('questions.html',question_idx=question_idx, current_question=current_question, choices=choices[question_idx])

    else:
        return redirect ('/thank_you')


@app.route('/answer', methods=["GET","POST"])
def answer_page():
    # UPDATE RESPONSES HERE
    global question_idx
    responses.append(request.form["response"])
    question_idx = len(responses)
    print(f"/questions/{question_idx}")
    return redirect (f"/questions/{question_idx}")

@app.route('/thank_you')
def thank_you():
    for resp in responses:
        print("RESPONSES: ", resp)
    return render_template('thank_you.html')
