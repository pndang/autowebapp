import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)
condition = []
app.secret_key='w98fw9ef8hwe98fhwef'; 

@app.route('/')
def renderMain():
    return render_template('home.html') 

@app.route('/welcome')
def renderWelcome():
    return render_template('welcome.html')

@app.route('/question1')
def renderQuestion1():
    return render_template('question1.html')

@app.route('/question2')
def renderQuestion2():
    return render_template('question2.html')

@app.route('/question3_over_25')
def renderQuestion3_over_25():
    return render_template('question3_over_25.html')

@app.route('/question3_under_25')
def renderQuestion3_under_25():
    return render_template('question3_under_25.html')

@app.route('/welcome',methods=['GET','POST'])
def renderWelcomeResult():
    session["name"]=request.form['name']
    return render_template('welcome.html')

@app.route('/question1',methods=['GET','POST'])
def renderQuestion1Result():
    session["age1"]=request.form['age1']
    if session["age1"] == 'True':
        return render_template('question2.html')
    if session["age1"] == 'False':
        return render_template('question3_under_25.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2Result():
    session["age2"]=request.form['age2']
    return render_template('question3_over_25.html') 

@app.route('/question3_over_25',methods=['GET','POST'])
def renderQuestion3_over_25Result():
    session["experience"]=request.form['experience']
    return render_template('question4_over_25.html')






if __name__=="__main__":
    
    app.run(host='0.0.0.0')
