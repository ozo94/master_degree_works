# coding=utf-8
'''
    1.读取待抽取表头，并生成对应的英文索引
'''

import xlrd
import os
import re
from dataDisplay.flaskapp.sums_models.rules.methods import  convert_column, get_table_name

def extract_columns():
    '''
    读取科室清单表目录，建立对应的联系
    :return:
    '''
    all_extract_lists = {}

    filepath = 'dataDisplay/flaskapp/sums_models/analysis/extract'
    extract_file = {'成果科抽取.xlsx',
                    '专利科抽取.xlsx',
                    '合作交流科抽取.xlsx',
                    '法规科抽取.xlsx',
                    '高新科抽取.xlsx',
                    '农社科抽取.xlsx'
                    }

    reflect_table = {'专利科': 'patent',
                     '农社科': 'farm_socity',
                     '合作交流科': 'cop_ex',
                     '法规科': 'law',
                     '成果科': 'result',
                     '高新科': 'high_new_tec',
                     }

    for file in extract_file:
        # print file
        ks_name = file.replace('抽取.xlsx', '')
        data = xlrd.open_workbook(os.path.join(filepath , unicode(file, 'utf-8')))
        table = data.sheets()[0]
        nrows = table.nrows

        for index in range(2, nrows, 4):
            column_names = []
            column_vals = []

            # 将中文表名映射成英文名
            table_name = table.row_values(index)[1].replace('\n', '').strip()
            table_name = get_table_name(reflect_table[ks_name], table_name)

            # 将规则中的各类数据中文表头映射成对应的英文
            column_ref = convert_column(table_name)

            for i in range(1, len(table.row_values(index + 1))):
                column_name = table.row_values(index + 1)[i].strip()
                try:
                    column_val = table.row_values(index + 2)[i].strip()
                except:
                    column_val=''

                # 将对应中文表头转换为英文表头，多个之间用’,‘隔开
                column_name_ref = []
                if  column_name.strip():
                    column_name = column_name.split(',')
                    for column in column_name:
                        try:
                            column = column_ref[column]
                            column_name_ref.append(column)
                        except:
                            print u'对应抽取属性不存在: ',table_name, column
                            column_name = ''
                    column_name = ','.join(column_name_ref)
                else:
                    column_name = ''

                column_names.append(column_name)
                column_vals.append(column_val)

            all_extract_lists.update({table_name:[column_names, column_vals, ks_name]})

    return all_extract_lists


def data_pro(index, data, value):
    '''
    根据不同的格式，处理不同的数据
    :param index:p_id,p_name,lev,c_com,year,area,money,deadline,category,
    :param data:
    :return:
    '''
    # 去除中英文空格以及换行符号
    data = data.replace(' ', '').replace('\n', '').replace('  ', '')

    try:
        if index ==2:
            # 这里只调整column非空下的，级别栏对应的数据格式，缺省的在规则表中就要标准化（省级。。）
            if data:
                if unicode('省','utf-8') in data:
                    data = '省级'
                elif unicode('苏','utf-8') in data:
                    data = '苏州'
                elif unicode('昆','utf-8') in data:
                    data = '昆山'
                else:
                    data = '国家'

        elif index == 4:
            data  = judge_year(re.findall('\d+', data))[0]
            if len(data) == 2:
                if int(data) > 50:
                    data = '19' + data
                else:
                    data = '20' + data

        elif index == 5:
            if data:
                if unicode('高新', 'utf-8') in data or unicode('玉山', 'utf-8') in data:
                    data = '高新区'
                elif unicode('周市', 'utf-8') in data:
                    data = '周市'
                elif unicode('周庄', 'utf-8') in data:
                    data = '周庄'
                elif unicode('巴城', 'utf-8') in data:
                    data = '巴城'
                elif unicode('开发', 'utf-8') in data:
                    data = '开发区'
                elif unicode('张浦', 'utf-8') in data:
                    data = '张浦'
                elif unicode('淀山', 'utf-8') in data:
                    data = '淀山湖'
                elif unicode('花桥', 'utf-8') in data:
                    data = '花桥'
                elif unicode('锦溪', 'utf-8') in data:
                    data = '锦溪'
                elif unicode('陆家', 'utf-8') in data:
                    data = '陆家'
                elif unicode('千灯', 'utf-8') in data:
                    data = '千灯'
                elif unicode('市', 'utf-8') in data:
                    data = '市属'
                else:
                    data = ''

        elif index == 6:
            data = float(re.findall('\d+\.?\d*', data)[0])
            if value:
                data = str(data/10000)
            else:
                data = str(data)

        elif index == 7:
            data = judge_year(re.findall('\d+', data.replace(r'.\d*', '')))[-1]
            if len(data) == 2:
                if int(data) > 50:
                    data = '19' + data
                else:
                    data = '20' + data

    except Exception,e:
        if data:
            print 'index',index,',missing_value: ',data
            print 'error:', e
            data = ''

    return  data

def judge_year(datas):
    new_datas = []
    for data in datas:
        if len(data) == 2 or len(data) == 4:
            new_datas.append(data)

    return new_datas

