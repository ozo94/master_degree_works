# coding=utf-8
from dataDisplay.flaskapp.sums_models.methods import *
from methods import *
from dataDisplay.flaskapp.sums_models.methods import *

def extrat_data():
    '''
    根据整理的表头，抽取对应的信息,存入extract_data_1中去
    :return:
    '''
    extract_dicts = extract_columns()

    for table_name, column_value in extract_dicts.iteritems():
        data_list = extract_table(table_name, column_value)
        print table_name, u'开始抽取'
        log_data = open('dataDisplay/flaskapp/sums_models/analysis/log_data.txt', 'a')
        miss_data = open('dataDisplay/flaskapp/sums_models/analysis/miss_data.txt', 'a')
        for data in data_list:
            log_data.write(data[4].encode('utf-8')+ ',' + data[7].encode('utf-8') + '\n')
            # print data[2]

        # 将数据插入到extract_data_1中去
        columns = 'p_id,p_name,lev,c_com,year,area,money,deadline,category,ks_name,ref_table'
        columns = columns.split(',')
        fail_lists, duplicate_data = insert('extract_data_1', data_list, columns)
        for data in fail_lists:
            miss_data.write(data + '\n')
        print table_name, u'已抽取结束'



