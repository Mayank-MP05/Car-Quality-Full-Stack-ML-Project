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
    carProfile = {}
    if request.method == "POST":
        carProfile['buying'] = request.form["buying"]
        carProfile['maint'] = request.form["maint"]
        carProfile['doors'] = request.form["doors"]
        carProfile['persons'] = request.form["persons"]
        carProfile['lug_boot'] = request.form["lug_boot"]
        carProfile['safety'] = request.form["safety"]

    return render_template('sucess.html', profile=carProfile)


@app.route('/')
def ello_world():
    return render_template('home.html')
