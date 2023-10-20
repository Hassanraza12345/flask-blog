import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# from flask import Blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2947018c79a13e3e0d73d0afea70c35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='userlogin'
login_manager.login_message_category='info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use the correct SMTP server for your email provider
app.config['MAIL_PORT'] = 465  # Use the correct port (e.g., 465 for SSL/TLS)
app.config['MAIL_USE_TLS'] = False  # Set to True if using TLS
app.config['MAIL_USE_SSL'] = True  # Set to True if using SSL
app.config['MAIL_USERNAME'] = 'h9034093@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'Hassan@542876391'  # Your email password or App Password

mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
