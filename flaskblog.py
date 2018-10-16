from datetime import datetime
# render_template = allows you to render html templates
# url_for = allows you to target routes
# flash = alert
# redirect = redirect to another page
from flask import Flask, render_template, url_for, flash, redirect
# for database
from flask_sqlalchemy import SQLAlchemy
# can also import other python files
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# app.config is how you set config values for applications
# this was obtained by going into the CL interpreter with:
# $ python3
# $ import secrets
# $ secrets.token_hex(16)
app.config["SECRET_KEY"] = "764ee981c27e46e66fdfeafc83dbff02"

# /// specifies a relative path for SQL lite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# make instance of database
db = SQLAlchemy(app)


class User(db.Model):
    # we are creating the user structure within DB
    id = db.Column(db.Integer, primary_key=True)
    # String(x) --> x = max number of characters, nullable = cannot be null
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default="default.jpg")
    password = db.Column(db.String(60), nullable=False)

    # our posts variable has a relationship to the Post model
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return "User({}, {}, {})".format(self.username, self.email, self.image_file)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return "Post({}, {})".format(self.title, self.date_posted)


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


# this conditonal is only true if we run this script directly
if __name__ == "__main__":
    app.run(debug=True)
