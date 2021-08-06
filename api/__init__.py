from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate     # companion package to SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
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

# Make the models available here
from api.models import User
# from api.models import Question
# from api.models import Answer
# from api.models import Comment

# return app

@app.route('/')
def hello():
    return 'Hello my Love!'


