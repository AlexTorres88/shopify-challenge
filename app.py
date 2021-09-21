from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from config import *
from flaskr.db_setup import database as db

# App definition
app = Flask(__name__, instance_relative_config=True, template_folder='templates')

app.config['FLASK_APP'] = 'app'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.static_folder = 'static'

db.init_app(app)

# Login management
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from flaskr.models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# blueprint for auth parts of app
from flaskr.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from flaskr.main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Error hanlders
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404

@app.errorhandler(405)
def bad_request(e):
    if current_user:
        return redirect(url_for('main.home'))
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    app.run()
