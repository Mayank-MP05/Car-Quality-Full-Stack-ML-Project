from flask import Flask, render_template, redirect, request, abort

# Form Code
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

import pickle as pkl
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# class MyForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/submit', methods=('GET', 'POST'))
def getAllData():
    carProfile = {}
    # Only POST request Allowed
    if request.method == "POST":
        carProfile['buying'] = request.form["buying"]
        carProfile['maint'] = request.form["maint"]
        carProfile['doors'] = request.form["doors"]
        carProfile['persons'] = request.form["persons"]
        carProfile['lug_boot'] = request.form["lug_boot"]
        carProfile['safety'] = request.form["safety"]

        # Importing the ML model
        model = pkl.load(open('model/DecisionTree.pickle', 'rb'))
        # print(model)

        # Building Dataframe
        carTest = pd.DataFrame({
            'buying': [carProfile['buying']],
            'maint': [carProfile['maint']],
            'doors': [carProfile['doors']],
            'persons': [carProfile['persons']],
            'lug_boot': [carProfile['lug_boot']],
            'safety': [carProfile['safety']]
        })
        pred = model.predict(carTest)
        carProfile["carPred"] = pred
        return render_template('sucess.html', profile=carProfile)
    else:
        return abort(400)


@app.route('/')
def ello_world():
    return render_template('home.html')
