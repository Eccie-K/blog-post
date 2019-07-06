from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Type your title',validators=[Required()])
    author = StringField('Type your name',validators=[Required()])
    category = SelectField('Type',choices=[('politics','Politics blog'),('business','Business blog'),('lifestyle','Lifestyle blog'),('health', 'Health blog')],validators=[Required()])
    blog= TextAreaField('write your content', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')

