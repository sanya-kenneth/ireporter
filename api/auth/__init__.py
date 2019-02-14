from flask import Blueprint
from flask_cors import CORS

# user and authentication blueprint
auths = Blueprint('auths', __name__)


# enable cors for auth blueprint
CORS(auths)
