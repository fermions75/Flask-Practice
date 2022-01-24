from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello_world():
    return render_template('Home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('About.html', title='About')


app.run(debug=True)
