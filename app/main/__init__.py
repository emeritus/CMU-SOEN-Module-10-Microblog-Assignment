from flask import Blueprint

bp = Blueprint('main', __name__)
# flake8: noqa
from app.main import routes
