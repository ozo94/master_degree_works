# coding=utf-8
from dataDisplay.flaskapp.sums_models.rules.methods import *

def get_area_dict():
    '''
    包含区镇的统计表格以及所对应的栏目
    :return:
    '''
    file = 'dataDisplay/flaskapp/sums_models/area_sel/area_dict.txt'
    area_data = open(file , 'r')
    all_tables = page_tables()

    area_dict = {}
    for data in area_data:
        if data.strip():
            data = data.strip().split(',')
            org_name, org_column = unicode(data[0], 'utf-8'), unicode(data[1], 'utf-8')
            # print org_name, org_column
            tabel_name = all_tables[org_name].strip()
            area_name = convert_column(tabel_name)[org_column]
            # print tabel_name, area_name
            area_dict.update({tabel_name:area_name})

    return area_dict

