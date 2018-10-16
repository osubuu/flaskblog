from datetime import datetime
# changed this from flaskblog to __main__ because we defined the app running as __main__ in flaskblog.py
# now rechanged it back to flaskblog cause we organized folders
from flaskblog import db, login_manager
from flask_login import UserMixin

# decorator


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
