# coding=utf-8
'''
    1.读取清单数据生成规则
    2.判断科室下所包含的表格
'''

import xlrd
from dataDisplay.flaskapp.sums_models.rules.column_convert import convert_table_name

def read_ks_column(filepath):
    '''
    读取科室清单表目录，建立对应的联系
    :param filepath:
    :return:
    '''
    ks_column = {}

    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    nrows = table.nrows
    # print directory_name

    for index in range(0, nrows, 7):
        ids = []
        table_names = []
        condition_names = []
        condition_vals = []
        add_columns = []

        directory_name = table.row_values(index)[0].strip('\n').strip()

        # print len(table.row_values(index+1)), table.row_values(index+1)
        for i in range(1, len(table.row_values(index+1))):

            id = table.row_values(index+1)[i]
            table_name = table.row_values(index+2)[i]
            condition_name = table.row_values(index+3)[i]
            condition_val = table.row_values(index + 4)[i]
            add_column = table.row_values(index+5)[i]
            # print id,table_name,condition_name,condition_val,add_column

            # 将规则中的各类数据中文名映射成对应的英文
            if table_name.strip():
                table_name, add_column, condition_name, re_falg, operation =  convert_table_name(table_name, add_column, condition_name)
            # print id, table_name, condition_name, condition_val, add_column

            ids.append(id)
            table_names.append(table_name)
            condition_names.append(condition_name)
            condition_vals.append(condition_val)
            add_columns.append(add_column)

        ks_column.update({directory_name:[ids, table_names, condition_names, condition_vals, add_columns]})

    return ks_column

def judge_table(table_name, ks_name):
    '''
    判断是不是当前科室下的表格
    :param table_name:
    :param ks_name:
    :return:
    '''
    dicts_code = open('dataDisplay/flaskapp/data/sheets_dict.txt').read()
    exec(dicts_code)
    ks ={}
    exec('ks = ' + ks_name + '.copy()')

    if table_name in ks.values():
        return True
    else:
        return False
