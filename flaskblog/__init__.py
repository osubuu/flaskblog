from flask import Flask
# for database
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

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
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# so when you can't access manually by URL certain pages even if you aren't logged in
login_manager.login_view = "login"
# this is just for styling purposes
login_manager.login_message_category = "info"


from flaskblog import routes
