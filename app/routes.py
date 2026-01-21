from app import app

@app.route("/")# 這裡告訴 Flask：當使用者造訪首頁時（/），第一層標籤
@app.route("/index")#造訪 /index 時，第二層標籤

def index():# # 只要上面任一標籤被觸發，就執行這個「視圖函式」
    return "Hello, world!"