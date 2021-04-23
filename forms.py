from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchFormDate(FlaskForm):
    customer_id = StringField('Customer ID:', validators=[DataRequired()])
    fromDate = StringField('From Date:', validators=[DataRequired()])
    toDate = StringField('To Date:', validators=[DataRequired()])
    search = SubmitField('Search')


class SearchFormDateRange(FlaskForm):
    customer_id = StringField('Customer ID:', validators=[DataRequired()])
    date1 = StringField('Date lower bound:', validators=[DataRequired()])
    date2 = StringField('Date upper bound:', validators=[DataRequired()])
    search = SubmitField('Search')
