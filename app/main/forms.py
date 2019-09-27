from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required


class BlogForm(FlaskForm):
   title = StringField('Blog Title',validators=[Required()])
   description = TextAreaField('Blog Description', validators=[Required()])
   submit = SubmitField('Submit')
   
class CommentForm(FlaskForm):
	description = TextAreaField('Write your comment : ',validators=[Required()])
	submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')