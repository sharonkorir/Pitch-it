from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[DataRequired()])
    category = SelectField('Select category:', choices=[('general', 'general'), ('business', 'business'), ('dad jokes', 'dad jokes'), ('books/movies', 'books/movies'), ('pick-up', 'pick-up')] ,validators=[DataRequired()])

    content = TextAreaField('Your pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('comment', validators=[DataRequired()])
    submit = SubmitField('Submit')