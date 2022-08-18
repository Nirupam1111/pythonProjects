from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message='email not valid',
                                                                         allow_empty_local='@')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(
        min=8, message='minimum 8 characters required.')])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
app.secret_key = "some-secret-string"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_from = MyForm()
    if login_from.validate_on_submit() == True:
        # login_from.validate_on_submit()
        print(login_from.email.data)
        if login_from.email.data == 'admin@email.com' and login_from.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_from)


if __name__ == '__main__':
    app.run(debug=True)
