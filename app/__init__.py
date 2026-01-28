from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 建立 Flask 應用程式物件，__name__ 幫助 Flask 找到資源路徑
app = Flask(__name__)
app.config.from_object(Config)
#初始化了 SQLAlchemy，稱為 ORM (Object-Relational Mapper)。
#資料庫（如 SQLite 或 MySQL）只聽得懂 SQL 語言。SQLAlchemy 負責溝通
db = SQLAlchemy(app)
#初始化 Flask-Migrate
#處理資料庫結構的變更（例如：增加或刪除欄位）
migrate = Migrate(app, db) 

# 最佳實踐：在最後才導入 routes，以避免「你等我、我等妳」的循環導入問題
# routes 模組此時已經可以使用上面定義好的 app 變數了
from app import routes, models
