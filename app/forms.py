from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField, SubmitField
from wtforms.widgets import TextArea

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()])
    description = StringField('Description', widget=TextArea())
    ingredients = StringField('Ingredients', widget=TextArea())
    instructions = StringField('Instructions', widget=TextArea())
    submit = SubmitField("Submit Recipe")
