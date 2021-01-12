from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired(),
        Length(min=6, message="Seems a little short for an email address"),
        Email(message='That\'s not a valid email address.')
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Seems a little short for a password."),
    ])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired(),
        Length(min=6, message="Seems a little short for an email address"),
        Email(message='That\'s not a valid email address.')
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Seems a little short for a password."),
    ])
    submit = SubmitField("Log In")


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")