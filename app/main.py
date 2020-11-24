from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wP4xQ8hU1jJ5oI1c'
bootstrap = Bootstrap(app)

class IrisForm(FlaskForm):
    sepal_length = StringField('Sepal Length:', validators=[DataRequired()])
    sepal_width  = StringField('Sepal Width :', validators=[DataRequired()])
    petal_length = StringField('Petal Length:', validators=[DataRequired()])
    petal_width  = StringField('Petal Width :', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form   = IrisForm(request.form)
    specie = 'No-image'
    print("Call me", file=sys.stderr)
    if form.validate_on_submit():
        print("Successfully created a new book", file=sys.stderr)
        specie = 'Iris-setosa' 

    return render_template('index.html', form=form, specie=specie)