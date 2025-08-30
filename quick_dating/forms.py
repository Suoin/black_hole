from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, NumberRange

class AdForm(FlaskForm):
    gender = StringField('Пол', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(min=18)])
    country = StringField('Страна', validators=[DataRequired()])
    region = StringField('Край/Регион', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    text = TextAreaField('Текст объявления', validators=[DataRequired()])
    submit = SubmitField('Отправить на модерацию')

class ResponseForm(FlaskForm):
    text = TextAreaField('Ваш ответ', validators=[DataRequired()])
    email = StringField('Ваш email для ответа', validators=[DataRequired(), Email()])
    submit = SubmitField('Отправить ответ')

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class EmailForm(FlaskForm):  # Для popup верификации
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Подтвердить')