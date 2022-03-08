from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[DataRequired()])
    category = StringField('Select category: (dad jokes, general, business/tech, books/movies, pick-up)', validators=[DataRequired()])
    content = TextAreaField('Your pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Leave a comment:', validators=[DataRequired()])
    submit = SubmitField('Submit')