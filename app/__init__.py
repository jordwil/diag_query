from flask import Flask

app = Flask(__name__)

from app import prefix_tree
from app import routes
