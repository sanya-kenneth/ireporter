from flask import Blueprint
from flask_cors import CORS


# user and authentication blueprint
incidents_bp = Blueprint('incidents_bp', __name__)


# set cors for incidents blueprint
CORS(incidents_bp)