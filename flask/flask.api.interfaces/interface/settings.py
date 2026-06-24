from view import app

app.config['SECRET_KEY'] = 'hard to guess'

# root:root用户&自己的密码，MySQL的默认端口是3306，最后是创建的数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/r?charset=utf8'

#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True