# coding=utf-8
from flask import jsonify, request, abort
from modles import *
from interface import app


tasks = [
    {
        'account' : 'lm',
        'password' : 'lm12345'
    },
    {
        'account' : 'ydh',
        'password' : 'ydh12345'
    }
]

#将数据库中的消息转换成对应的json文件
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# 获取对应的account的数据信息
@app.route('/todo/api/v1.0/tasks/<string:account>', methods=['GET'])
def get_task(account):
    task = filter(lambda t: t['account']== account, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# 改善404错误响应
@app.errorhandler(404)
def not_found(error):
    from flask import make_response
    return make_response(jsonify({'error':'Not Found'}), 404)

# 添加一个新的任务方法（在任务数据库中插入一个新的任务）
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'account' in request.json:
        abort(400)
    task = {
                'account' : request.json['account'],
                'password' : request.json['password']
           }
    if verificate(task['account'], task['password']):
        return jsonify({'task': task})
    return 'error'

if __name__ == "__main__":
    app.run(debug=True)


