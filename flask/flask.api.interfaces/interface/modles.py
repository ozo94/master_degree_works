# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from interface import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

class R2(db.Model):
    __tablename__ = 'r2'

    account = db.Column(db.VARCHAR, primary_key=True)
    password = db.Column(db.VARCHAR)
    Guid = db.Column(db.VARCHAR)
    FieIDName = db.Column(db.VARCHAR)
    DispOrder = db.Column(db.INT)

def verificate(account, password):
    data = R2.query.filter_by(account = account).first()

    if data:
        if data.password == password:
            return True
    return False

if __name__ == '__main__':
    # 在数据库中创建新的表，根据上文的代码类产生对应的table
    db.create_all()