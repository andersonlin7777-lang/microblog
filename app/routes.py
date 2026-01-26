from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")# 這裡告訴 Flask：當使用者造訪首頁時（/），第一層標籤
@app.route("/index")#造訪 /index 時，第二層標籤
def index():# # 只要上面任一標籤被觸發，就執行這個「視圖函式」
    user = {"username": "Miguel"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

#定義：這裡接收 GET 和 POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #在還沒連動資料庫之前，我們先用 flash() 確保資料確實從前端（HTML 表單）
        #成功傳到了後端（Python 函式）
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        #查詢：我想去首頁，請幫我查 'index' 函式的網址是什麼，url_for('index') 會幫你算出 "/index"
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)