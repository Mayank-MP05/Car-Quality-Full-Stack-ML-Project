from flask import Flask, render_template, redirect, request

# Form Code
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# class MyForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/submit', methods=('GET', 'POST'))
def getAllData():
    profile = {}
    if request.method == "POST":
        profile['username'] = request.form["name"]
        profile['buying'] = request.form["buying"]

    return render_template('sucess.html', profile=profile)


@app.route('/')
def ello_world():
    return render_template('home.html')
