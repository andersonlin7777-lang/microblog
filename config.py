import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #先去電腦的「環境變數」（像是藏在牆壁裡的隱藏式保險箱）裡尋找真正的密碼。
    #如果找不到，它就會使用'you-will-never-guess' 作為臨時備用鑰匙。
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # SQLALCHEMY_DATABASE_URI 是資料庫的「通訊地址」
    # 優先嘗試從系統環境變數中取得 'DATABASE_URL'
    # 如果找不到（例如在開發環境），則使用後方的 SQLite 備用路徑
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es', 'zh_TW']
    
