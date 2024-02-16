from flask import Blueprint, g, session
from flask import url_for, abort, redirect
import logging
from database import db
from .oauth import oauth
from .models import User

logger = logging.getLogger('auth/views')

user_schema = User(db["users"])

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login/<name>')
def login(name):
    logger.debug("Login")
    client = oauth.create_client(name)
    if not client:
        abort(404)

    redirect_uri = url_for('auth.callback', name=name, _external=True)
    return client.authorize_redirect(redirect_uri)


@auth_bp.route('/callback/<name>')
def callback(name):
    client = oauth.create_client(name)
    if not client:
        abort(404)
    token = client.authorize_access_token()

    userinfo = {**token['userinfo']}
    user = user_schema.get_user(userinfo['email'])
    if not user:
        user_schema.create_user(userinfo)

    session['user'] = token['userinfo']
    return redirect('/')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
