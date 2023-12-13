from flask import Flask
from flask_login import LoginManager
from app.bcrypt_extension import bcrypt
from app.user import load_user
from app.login import login, dashboard, logout, signup
from flask import Flask
from app.config import Config
from app.database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
bcrypt.init_app(app)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.user_loader(load_user)

app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])
app.add_url_rule('/dashboard', 'dashboard', dashboard)
app.add_url_rule('/logout', 'logout', logout)

if __name__ == '__main__':
    app.run()
