# -*- coding: utf-8 -*-
"""
# @Time    :2017/9/7 下午3:23
# @Author  :Xuxian
"""

def get_chart_datas(chart_id):
    pass


def show_columns(table_id):
    """
    读取存储好的文件中所有栏目表
    :return: columsn_table字典，返回原始栏目名和对应的数据库中映射表名
    """
    data = open('datadisplay/flaskapp/data/all_tables.txt', 'r').readlines()
    columns_table = {}
    for index in range(0, len(data), 3):
        try:
            table_name = data[index].strip()
            org_columns = data[index + 1].strip()
            ref_columns = data[index + 2].strip()
            columns_table.update({table_name: [org_columns, ref_columns]})
        except Exception, e:
            print 'show_columns-----------------', table_name
            print e

    return columns_table[table_id]


def get_table_name(name):
    """
    读取数据库表名对应的中文名
    :param name:
    :return: string 表名
    """
    data = open('datadisplay/flaskapp/data/page_table.txt', 'r').readlines()
    for lis in data:
        tmp = lis.split(',')
        if tmp[1].strip() == name:
            return tmp[0].strip()
    return


def is_allowed(department, table_id):
    dic = {'department1': 'farm_socity',
           'department2': 'petent',
           'department3': 'law',
           'department4': 'cop_ex',
           'department5': 'high_new_tec',
           'department6': 'result',
           }
    print dic[department]
    lenth = len(dic[department])
    if table_id[:lenth] == dic[department]:
        return True
    return False


def myfunc():
    n, k = [int(x) for x in raw_input().strip().split()]
    raw = [1] * k

    for _ in range(n - 1):
        tmp = [sum(raw)] * k
        for i in range(0, k/2):
            list = raw[i * 2 + 1::i + 1]
            tmp[i] -= sum(list)
        raw = tmp
    print sum(tmp) % 1000000007


if __name__ == '__main__':
    myfunc()
