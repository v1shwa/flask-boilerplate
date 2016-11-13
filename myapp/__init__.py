# -*- coding: utf-8 -*- 
from flask import Flask
from config import configure_app

# Import blueprints
from home.controller import home

app = Flask(__name__)
configure_app(app)

# register blue prints
app.register_blueprint(home, url_prefix='')