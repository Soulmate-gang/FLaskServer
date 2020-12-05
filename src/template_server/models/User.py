"""https://www.jianshu.com/p/5282a7525e52  多对多设计"""

from passlib.context import CryptContext

from . import db

password_context = CryptContext(
    schemes=["pbkdf2_sha256", ],
    deprecated="auto",
)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # 用户主键
    username = db.Column(db.String(80))  # 用户名
    password = db.Column(db.String(128))  # 密码
