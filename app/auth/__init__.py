from flask import Blueprint

bp = Blueprint('auth', __name__)
# flake8: noqa
from app.auth import routes
