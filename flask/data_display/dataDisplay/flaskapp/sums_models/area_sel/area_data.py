# coding=utf-8
from dataDisplay.flaskapp.sums_models.methods import *

def get_area_data(table_name, area_name):
    '''
    调用，返回对应区镇的数据
    :param table_name:
    :param area_name:
    :return:
    '''
    area_dict = data_by_area(table_name, area_name)
    return area_dict