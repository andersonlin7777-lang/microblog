from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
# 建立 Flask 應用程式物件，__name__ 幫助 Flask 找到資源路徑
app = Flask(__name__)
app.config.from_object(Config)
#初始化了 SQLAlchemy，稱為 ORM (Object-Relational Mapper)。
#資料庫（如 SQLite 或 MySQL）只聽得懂 SQL 語言。SQLAlchemy 負責溝通
db = SQLAlchemy(app)
#初始化 Flask-Migrate
#處理資料庫結構的變更（例如：增加或刪除欄位）
migrate = Migrate(app, db) 

moment = Moment(app)

login = LoginManager(app)
login.login_view = "login"

babel = Babel(app, locale_selector=get_locale)

if not app.debug:
    if app.config["MAIL_SERVER"]:
        auth = None
        if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
            auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
        secure = None
        if app.config["MAIL_USE_TLS"]:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    
    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler("logs/microblog.log", maxBytes=1024, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')   

mail = Mail(app) 

# 最佳實踐：在最後才導入 routes，以避免「你等我、我等妳」的循環導入問題
# routes 模組此時已經可以使用上面定義好的 app 變數了
from app import routes, models, errors
