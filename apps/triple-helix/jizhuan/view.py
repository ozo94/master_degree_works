#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import render_template, request
from models import *
# from models import select_paginate
# from models import select_paginate_by_add
# from models import search_engine
from jizhuan import app


'''
    路由：index.html
    初始主页，即分页第一页
    分页显示了所有数据
'''
@app.route('/')
def blank():
    pagination = select_paginate(1)
    return render_template('index.html',title= '三螺旋', pagination= pagination)

'''
    路由：all.html
    所有数据显示
'''
@app.route('/all')
def all():
    info = select_all()
    info_list = []
    info_list.append(info)
    return render_template('all.html',title='三螺旋',pagination_list = info_list)

'''
    路由：all.html
    地区复选框功能
'''
@app.route('/search')
def search():
    info_address_list = select_address_checkbox()
    return render_template('all.html',title='三螺旋',pagination_list = info_address_list)

'''
    路由：index.html
    按page定位到第几页进行显示
'''
@app.route('/<int:page>')
def company(page):
    pagination = select_paginate(page)
    return render_template('index.html',title= '三螺旋',pagination=pagination)

'''
    路由：order_confirm.html
    跳转订单确认页面
'''
@app.route('/order_confirm')
def about():
    return render_template('order_confirm.html')

'''
    路由：order_list.html
    跳转订单列表页面
'''
@app.route('/order_list')
def order():
    return render_template('order_list.html')

'''
    路由：add.html
    按地址或公司名查询
    返回结果在add.html中显示
'''
@app.route('/<string:con>/<int:page>')
def add(con,page):
    # pagination = search_engine(area, page)
    pagination = select_paginate_by_add(con,page)
    return render_template('add.html',title="三螺旋",pagination=pagination,name=con)

'''
    路由：
    触发搜索
    返回add方法
'''
@app.route('/demand')
def demand():
    content = request.args.get('requirement')
    return add(content,1)