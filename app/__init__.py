from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile("../config.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager(app)
lm.login_view = 'login'

from app import routes, models