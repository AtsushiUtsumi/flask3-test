from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import logging

from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id):
        self.id = id
# 引数user_idにセッション内に登録されているIDが入ります
# LoginManagerをインスタンス化する
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = ""

@login_manager.user_loader# これ忘れてエラーだったっぽい
def load_user(user_id):
    return User(user_id)

csrf = CSRFProtect()

# create_app関数を作成する
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
    app.logger.setLevel(logging.DEBUG)
    login_manager.init_app(app)
    @app.route("/")
    def index():
        return render_template("home.html")
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    return app


# 登録したエンドポイント名の関数を作成し、404や500が発生した際に指定したHTMLを返す
def page_not_found(e):
    """404 Not Found"""
    return render_template("404.html"), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template("500.html"), 500
