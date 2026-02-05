from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    #確保資料庫中絕對不會有兩筆完全一樣的 ID
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    #index=True建立了索引，資料庫就能瞬間找到該使用者，unique=True：拒絕重複
    #sa負責的是與資料庫底層最直接相關的定義，定義實體的物理規格
    #so負責「對映（Mapping）」，讓 Python 知道這個變數要對應到資料庫的哪一欄
    #so.Mapped[...]：這是給 Python 看的，告訴開發工具這個屬性是一個「被對映的欄位」。
    #so.mapped_column(...)：這是銜接 sa 建材的「掛鉤」，它把物理規格（如 String）掛載到 Python 的屬性上。
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped["Posts"] = so.relationship(back_populates="author")
    
    #Python 方法。終端機印出一個 User 物件時，不會顯示難懂的 <User object at 0x...>
    #而是顯示清晰的 <User sally>。這對Debugging有幫助
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Posts(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates="posts")

    def __repr__(self):
        return '<Posts {}>'.format(self.body)