# render_template = allows you to render html templates
# url_for = allows you to target routes
# flash = alert
# redirect = redirect to another page
from flask import render_template, url_for, flash, redirect
from flaskblog import app
# can also import other python files
from flaskblog.forms import RegistrationForm, LoginForm
# we reorganized our models and put them in a separate .py file and imported them here
from flaskblog.models import User, Post

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
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# second argument in route is the list of accepted methods for this route
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}".format(form.username.data), "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
