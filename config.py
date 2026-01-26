import os

class Config:
    #先去電腦的「環境變數」（像是藏在牆壁裡的隱藏式保險箱）裡尋找真正的密碼。
    #如果找不到，它就會使用'you-will-never-guess' 作為臨時備用鑰匙。
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    