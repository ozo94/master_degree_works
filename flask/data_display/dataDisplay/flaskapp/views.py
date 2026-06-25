# -*- coding: utf-8 -*-
"""main view"""
from flask import Blueprint, render_template
from flask_login import login_required

from dataDisplay.flaskapp.sums_models.calculation import update
from dataDisplay.flaskapp.decorators import *
from dataDisplay.user.models import Role, User
from dataDisplay.flaskapp.sums_models.methods import *
from dataDisplay.flaskapp.sums_models.interfaces import *

blueprint = Blueprint('data', __name__, static_folder='../static/flaskapp')


@blueprint.route('/test')
@login_required
@minister_required
def display():
    '''
    模块的更新测试
    :return:
    '''

    # 汇总表自动更新模块
    # update.update_all()

    # 科室目录模块
    # sheet_names = [u'技术经纪人']
    # result = do_sum.row_sum(sheet_names)
    # print result


    # result = do_sum.show_ks_sums(u'成果科认定项目汇总表')
    # print result

    # results = update.update_directory()
    # print results

    insert_db('dataDisplay/flaskapp', 'test.xlsx', 'cop_ex')


    # extrat_data()

    # dict = get_area_dict()
    # for table in dict.iterkeys():
    #     get_area_data(table, [u'高新区'])
    return '----------模块测试页面------------\n'


@blueprint.route('/index')
@login_required
def dashboard():
    return render_template('flaskapp/index.html')


@blueprint.route('/charts/<string:department>')
@login_required
def show_charts(department):
    """show charts"""
    # datas = get_chart_datas(chart_id)
    if department == 'department2':
        datas = [385, 656.5, 150, 100]
        # 获取数据
        return render_template('flaskapp/charts_2.html', datas=datas)
    if department == 'department3'or 'department1':
        datas = [16880, 38210, 34450]
        # 获取数据
        return render_template('flaskapp/charts_3.html', datas=datas)


@blueprint.route('/tables/<string:table_id>')
@login_required
def show_tables(table_id):
    """show dataTables"""
    if current_user.roles[0].permissions < 7 and not is_allowed(current_user.department, table_id):
        abort(401)
    info = eval(table_id).query.all()
    table_name = get_table_name(table_id)
    # print table_name
    columns = show_columns(table_id)
    column_0 = columns[0].split(',')[1:]
    column_1 = columns[1].split(',')[1:]
    # if table_name == '汇总表':
    #     columns = []
    #     for x in range(len(column_0)):
    #         print column_0[x]
    #         columns.append([column_0[x],column_1[x]])
    # return render_template('flaskapp/tables1.html', info=info, columns=columns, table_name=table_name)

    columns = [column_0, column_1]
    return render_template('flaskapp/tables.html', info=info, columns=columns, table_name=table_name)


@blueprint.route('/addrole')
@admin_required
def add_role():
    """Add a role to a user."""

    # role = Role(name='admi')
    role = Role(permissions=3)
    # role.update()
    user = User.get_by_id(6)
    if len(user.roles) == 0:
        user.roles.append(role)
    else:
        user.roles[0] = role
    user.update()
    return '123'
