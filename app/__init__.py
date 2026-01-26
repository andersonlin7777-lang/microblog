from flask import Flask
from config import Config
# 建立 Flask 應用程式物件，__name__ 幫助 Flask 找到資源路徑
app = Flask(__name__)
app.config.from_object(Config)

# 最佳實踐：在最後才導入 routes，以避免「你等我、我等妳」的循環導入問題
# routes 模組此時已經可以使用上面定義好的 app 變數了
from app import routes
