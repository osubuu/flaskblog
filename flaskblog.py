from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "April 20, 2018"
    },
    {
        'author': "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "April 21, 2018"
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# this conditonal is only true if we run this script directly
if __name__ == "__main__":
    app.run(debug=True)
