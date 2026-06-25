# coding=utf-8
'''
    1.excle的读取
    2.数据库表的索引
    3.中英文表头的对照
'''
import xlrd
import os
from dataDisplay.flaskapp.myfunc import *


def page_tables():
    '''
    所有excles中sheets表,在mysql中对应的表名
    :return:
    '''
    filepath = 'dataDisplay/flaskapp/data/page_table.txt'
    ref_names = {}

    for data in open(filepath , 'r'):
        data = unicode(data, 'utf-8')
        data = data.strip('\n').split(',')
        ref_names.update({data[0]: data[1]})

    return ref_names


def show_columns():
    """
    读取存储好的文件中所有栏目表
    :return: columsn_table字典，返回原始栏目名和对应的数据库中映射表名
    """
    data = open('datadisplay/flaskapp/data/all_tables.txt', 'r').readlines()
    columns_table = {}
    for index in range(0, len(data), 3):
        try:
            table_name = unicode(data[index].strip(), 'utf-8')
            org_columns = data[index + 1].strip().split(',')
            ref_columns = data[index + 2].strip().split(',')
            columns_table.update({table_name: [org_columns, ref_columns]})
        except Exception, e:
            print u'对应表的中英文表头读取失败:', table_name
            print e

    return columns_table


def convert_column(table_name):
    '''
    对应某张表中，中文属性名对应的英文属性名
    :param table_name:
    :return: 一个中英文对照字典
    '''
    columns = show_columns()
    column = columns[table_name]
    org_column = column[0]
    ref_column = column[1]

    column_ref = {}
    for index in range(len(org_column)):
        key = unicode(org_column[index], 'utf-8')
        column_ref.update({key: ref_column[index]})

    return column_ref


def give_sheet(path, xls_name):
    '''
    读取一个excels中所有的sheets的内容
    :param path:
    :param xls_name:
    :return:excel文件中的所有的sheet名，以及对应的数据字典
    '''
    data = xlrd.open_workbook(os.path.join(path, xls_name))

    # 读取所有sheets中的内容
    all_datas = {}
    sheet_names = []

    for index in range(len(data.sheets())):
        table = data.sheets()[index]
        sheet_name = table.name
        sheet_names.append(sheet_name)
        nrows = table.nrows

        datas = read_sheet(table, 1, nrows)
        all_datas.update({sheet_name:datas})

    return  all_datas, sheet_names


def read_sheet(table, begin, end):
    '''
    根据指定的序号，读取excle中的数据，行列存放到二维数组中
    :param table:
    :param begin:
    :param end:
    :param columns: 表格对应的栏目（属性）
    :return:
    '''
    all_datas = []

    for i in range(begin, end):
        data = table.row_values(i)
        row_data = []
        for cell in data:
            content = cell
            row_data.append(content)

        all_datas.append(row_data)

    return all_datas


def get_table_name(ks_name, table_name):
    '''
    根据科室的名字以及对应的sheet名，返回对应英文表名，解决sheet重名问题
    :param ks_name: 英文映射
    :param table_name: 中文sheet
    :return:
    '''
    dict_path = 'dataDisplay/flaskapp/data/sheets_dict.txt'
    table_dicts = open(dict_path).read().decode('utf-8')
    exec(table_dicts)

    cmd = ks_name + '[table_name]'
    table_name = eval(cmd)

    return table_name