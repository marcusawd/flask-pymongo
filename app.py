import os
import logging
from flask_cors import CORS
from flask import Flask, send_from_directory, render_template, session
# Blueprints
from auth import auth_bp

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET")
app.config.from_object('config')

CORS(app)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('app')


@app.route('/')
def homepage():
    user = session.get('user')
    return render_template('home.html', user=user)


app.register_blueprint(auth_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)
