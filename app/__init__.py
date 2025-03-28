from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'  # You can replace this with an environment variable later

    from .routes import main
    app.register_blueprint(main)

    return app
