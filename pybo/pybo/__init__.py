from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)

# ORM
db.init_app(app)
migrate.init_app(app, db)

import pybo.models

import pybo.main_views
import pybo.question_views

app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)