from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, url_for, abort, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.user import get_user, load_user, create_user
from app.bcrypt_extension import bcrypt



class LoginForm(FlaskForm):
    user_email = StringField('User Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def set_submit_label(self, label):
        self.submit.label.text = label

def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_email = login_form.user_email.data
        password = login_form.password.data
        user = get_user(user_email)
        if(user == None):
            flash('User does not exist', 'danger')
        else:
            is_valid = bcrypt.check_password_hash(user.password, password)
            if(is_valid):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                 flash('Invalid user_email or password', 'danger')
    return render_template('login.html', form=login_form)

def signup():
    signup_form = LoginForm()
    signup_form.set_submit_label('Sign Up')
    if signup_form.validate_on_submit():
        user_email = signup_form.user_email.data
        password = signup_form.password.data
        response = create_user(user_email, password)
        if(response == 409):
            flash('User Already exists', 'danger')
        elif(response == 500):
            flash("Error while creating the user. Please Try Again later")
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=signup_form, is_signup=True)

@login_required
def dashboard():
    return f'Hello, {current_user.id}! This is the dashboard.'

@login_required
def logout():
    logout_user()
    return 'You have been logged out.'
