from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return '<h1>Hello from Flask! 🎉 Your app is running.</h1>'
