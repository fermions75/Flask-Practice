from flask import Flask, render_template, url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '34725824fedf7e6efd31e6bdc8f35902'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"




class Post(db.Model):

    __tablename__ = 'post'


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"












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


if __name__ == "__main__":
    app.run(debug=True)
