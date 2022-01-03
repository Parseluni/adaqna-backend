from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate     # companion package to SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_login import LoginManager
import os

# Sets up db and migrate, which are conventional variables that give us access to database operations
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

# def create_app(test_config=None):
app = Flask(__name__)
test_config = None

#if not in test mode
if not test_config:
    # Configures the app to include two new SQLAlchemy settings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
else:
    # test configuration is on
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

# Connects db and migrate to our Flask app
db.init_app(app)
migrate.init_app(app, db)



### LOGIN DIGITAL OCEAN ###
# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



## LOGIN MEDIUM ###
# # Create a Login Manager instance
# login_manager = LoginManager()
# # Define the redirection path when login required and attempt to access
# login_manager.login_view = "auth.login"
# # Configure for login
# login_manager.init_app(app)

# from api.models import Person

# # reload the person object from the person id stored in the session
# @login_manager.user_loader
# def load_person(person_id):
#     return Person.query.get(int(person_id))

# # blueprint for auth routes in our app to organize flask app
# from auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint)

# # blueprint for non-auth parts of app
# from main import main as main_blueprint
# app.register_blueprint(main_blueprint)



# Make the models available here
from api.models import Person
from api.models import Question
# from api.models import Answer
# from api.models import Comment

# return app

@app.route('/')
def hello():
    return 'Hello World!'


