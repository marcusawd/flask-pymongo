from authlib.integrations.flask_client import OAuth
from flask import current_app as app

oauth = OAuth(app)


# In OpenID Connect, the discovery document is a JSON document that contains metadata about the OpenID Connect provider, including endpoints, supported features, and other configuration details. The discovery document allows clients to dynamically discover and interact with the OpenID Connect provider's endpoints without hardcoding URLs.
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)
