from flask import render_template, url_for, flash, redirect
from FlaskPractice import app
from FlaskPractice.forms import RegistrationForm, LoginForm
from FlaskPractice.models import User, Post











posts = [

    {
        'author' : 'farhan',
        'title' : 'blog post 1',
        'content' : 'Blog 1 content',
    },

    {
        'author' : 'Omi',
        'title' : 'blog post 2',
        'content' : 'Blog 2 content',
    }
]


@app.route("/")
def home_page():
    return render_template('Home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('About.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accounted created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('Register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '_password_':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)