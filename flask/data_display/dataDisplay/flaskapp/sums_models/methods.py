# coding=utf-8
'''
    1.数据库的增、删、改工作
    2.个性化的查询要求
'''

from dataDisplay.flaskapp.sums_models.models import *
from dataDisplay.flaskapp.sums_models.analysis.models import *
from dataDisplay.flaskapp.models import *
from dataDisplay.flaskapp.sums_models.analysis.methods import *
from dataDisplay.flaskapp.sums_models.area_sel.methods import *
from sqlalchemy import or_


def delet_data(table_name, id):
    '''
    删除对应id行的数据
    :param table_name:
    :param id:
    :return:
    '''
    exec(table_name+ '.query.filter_by(id = id).delete()')
    db.session.commit()


def find_id(table_name, year):
    '''
    根据年份信息寻找总结表中，对应年份数据对应的id
    :param table_name:
    :param year:
    :return:
    '''
    result = None
    exec ('result=' + table_name + '.query.filter_by(year = year).first()')
    # 空查询结果不存在对应的id
    try:
        id = result.id
    except:
        id = ''
    return id


def update_data(tale_name, new_data, columns):
    '''
    更新表中的某行数据, 以id（主键）为索引目标
    :param tale_name:
    :param id:
    :param new_data:
    :param columns:
    :return:
    '''

    for data in new_data:
        values = []
        for index in range(0, len(data)):
            # 如果new_Data[index]中包含换行符，会报错, 需要保持字符串为raw string（repr, eval）
            # 接受更新值长度比原栏目长度短的情况
            cell = str(data[index]).replace('\n', ' ')
            value = tale_name + '.' + columns[index] + ':' + "'" + cell + "'"
            values.append(value)

        values = '{' + ', '.join(values) + '}'
        id = data[0]
        cmd = tale_name+'.query.filter_by(id = id).update(' + values + ')'
        exec(cmd)
        db.session.commit()


def insert(table_name, xls_data, columns):
    '''
    全表格查找，匹配表格中的所有栏目
    :param table_name:
    :param xls_data:
    :param columns:
    :return:
    '''
    # 没有成功插入的数据
    fail_lists = []
    duplicate_data = []

    for data in xls_data:
        result = None
        cmd = 'result =' +  table_name + '.query.filter('
        for index in range(0 , len(columns)):
            # 考虑数据中包含换行符号,空格符号，小数点符号等情况
            if type(data[index]) == float:
                data[index] = str(data[index])
            value = str(data[index]).replace('\n', '%').replace(' ', '%').replace('  ','%').replace('.0','%')
            if value:
                cmd +=  table_name + '.' + columns[index] + " .like('%" + value + "%'), "
        cmd += ').all()'
        try:
            exec(cmd)
        except Exception,e:
            print e

        if not result:
            content = None
            try:
                exec('content = '+ table_name + '(columns, data)')
                db.session.add(content)
            except Exception, e:
                # models没有成功初始化
                print u'数据插入失败：', table_name, u'——', data
                print u'属性数目：', len(columns), u' 数据列数：', len(data)
                fail_lists.append(','.join(data))
                print e

            try:
                db.session.commit()
            except Exception, e:
                # print 'ERROR:', e
                db.session.rollback()

        else:
            duplicate_data.append(','.join(data[:-3]))
            print data

    return fail_lists, duplicate_data


def extract_table(table_name, column_value):
    '''
    抽取数据库中对应表，对应栏目的数据
    :param table_name:
    :param column_value:
    :return:
    '''
    columns = column_value[0]
    values = column_value[1]
    ks_name = column_value[2]
    extract_list = []
    result = None
    exec('result = ' + table_name + '.query.all()')

    # 读取对应的table
    for data in result:
        temp = []
        for index in range(len(columns)):
            column = columns[index]
            value = values[index]
            if column:
                # 考虑一个单元格中包含的多个属性
                column = column.split(',')
                cell = []
                for e in column:
                    new_data = data_pro(index, eval('data.' + e), value)
                    if new_data.strip():
                        cell.append(new_data)

                # 多项金额要相加,其他的直接组合成一个字符串
                if index == 6:
                    num = 0
                    for e in cell:
                        try:
                            num += float(e)
                        except:
                            if e:
                                print e
                            num += 0
                    temp.append(str(num))
                else:
                    try:
                        temp.append(','.join(cell))
                    except:
                        # cell = [None, None ]的情况
                        temp.append('')

            elif not column and value:
                temp.append(value)

            else:
                temp.append('')

        temp.append(ks_name)
        temp.append(table_name + '.' + str(eval('data.id')))
        extract_list.append(temp)

    return extract_list


def data_by_area(table_name, area_names):
    '''
    返回对应表下对应区镇的数据
    :param table_name: 英文表名
    :param area_name: 指向哪一个取证
    :return:
    '''
    # 对应表示区镇的英文栏目名
    area = get_area_dict()[table_name]
    # print area_name

    result = None
    cmd = 'result = ' + table_name + '.query.filter( or_('
    for area_name in area_names:
        area_name = '%'.join(area_name)

        if area_name == unicode('高%新%区', 'utf-8'):
            cmd += table_name + '.' + area + ".like('%" + unicode('高%新%区', 'utf-8') + "%'), " \
                   + table_name + '.' + area + ".like('%" + unicode('玉%山', 'utf-8') + "%'),"
        else:
            cmd += table_name + '.' + area + ".like('%" + area_name + "%'),"
    cmd += ')).all()'
    # print cmd
    exec(cmd)

    for data in result:
        print data

    return  result

