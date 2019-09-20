from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What pitch ideas would you love to share?",validators=[Required()])
	category = RadioField('Label', choices=[ ('promotion pitch','promotion pitch'), ('interview pitch','interview pitch'),('business pitch','business pitch')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('What do you think?',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
    submit = SelectField('Like')


class Downvote(FlaskForm):
    submit = SelectField('Like')