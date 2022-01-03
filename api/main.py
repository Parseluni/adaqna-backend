from flask import Blueprint
from . import db


### LOGIN DIGITAL OCEAN ###

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'
