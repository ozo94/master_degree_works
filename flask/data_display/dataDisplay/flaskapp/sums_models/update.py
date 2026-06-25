# coding=utf-8
'''
    更新数据库，插入、更新
    更新数据库，增量更新
    汇总表数据更新
'''

from dataDisplay.flaskapp.sums_models.methods import *
from dataDisplay.flaskapp.sums_models.rules.methods import *
from dataDisplay.flaskapp.sums_models.directory_sum.methods import judge_table
import datetime

log_path = 'datadisplay/flaskapp/sums_models/source_logs.txt'
log_path2 = 'datadisplay/flaskapp/sums_models/calculation/sums_logs.txt'

def update_db(path, xls_name):
    '''
    增加、更新数据库，同时进行。
    缺点：需要自己基于总数据，自增id值
    :param path:
    :param xls_name:
    :return:
    '''
    # 待更新excle文件，同步到数据库中
    # 获取文件中的所有的sheets，以及对应数据库中的英文表名
    all_datas, sheet_names = give_sheet(path, xls_name)
    ref_names = page_tables()
    columns = show_columns()

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs = open(log_path, 'a')
    logs.write(time + ': 科室数据更新结果\n')

    for sheet in sheet_names:
        logs.write('sheet:' + sheet + '\n')

        datas = all_datas[sheet]
        ref_name = ref_names[sheet]
        column = columns[ref_name][1]

        for e in datas:
            # 逐条读取单个sheet中的数据，要重新构建成二位list，直接用list函数不行
            data = []
            data.append(e)

            fail_lists = []
            fail_sums = 0
            try:
                insert(ref_name, data, column)
            except:
                # 原来表
                id = data[0]
                try:
                    update_data(ref_name, id, data, column)
                except:
                    fail_lists.append(id)
                    fail_sums += 1

        logs.write('数据上传结束！\n')
        if fail_sums:
            logs.write('有部分数据未能完成更新，序号为：' + ','.join(fail_lists) + '\n')
        else:
            logs.write('所有数据更新完成！\n')

        logs.close()


def insert_db(path, xls_name, ks_name):
    '''
    导入工作表，数据库表只增加，不更新。可以接受同一科室下的多张更新表（一个excel文件中对应的多个sheet表）。
    更新情况记录在source_logs.txt中
    :param path:
    :param xls_name:
    :param ks_name: 接收对应的英文名，对应表情况如下:
                    reflect_table = {'专利科':'patent',
                                    '农社科':'farm_socity',
                                    '合作交流科':'cop_ex',
                                    '法规科':'law',
                                    '成果科':'result',
                                    '高新科':'high_new_tec',
                                    '总结':'sums'}
    :return:
    '''

    # 待更新excle文件，导入到到数据库中
    # 获取文件中的所有的sheets，以及对应数据库中的英文表名
    all_datas, sheet_names = give_sheet(path, xls_name)
    ref_names = page_tables()
    columns = show_columns()

    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs = open(log_path, 'a')
    logs.write('------'+time + ' 新增数据导入 ------ \n')

    for sheet in sheet_names:
        logs.write('对应sheet->' + sheet.encode('utf-8') )
        datas = all_datas[sheet]
        ref_name = ref_names[sheet]
        column = columns[ref_name][1]

        if judge_table(ref_name, ks_name):
            # 自动增量更新，去除数据首位的id属性（主键）
            del column[0]
            raw_data = []
            for e in datas:
                if type(e[0]) == float:
                    del e[0]
                    raw_data.append(e)

            # 插入对应数据，并统计失败的项目，缩略记录到日志中
            fail_lists, duplicate_data = insert(ref_name, raw_data, column)
            fail_sums =len(fail_lists)
            if fail_sums or duplicate_data:
                logs.write('->有部分数据未能完成导入，内容为：\n' )
                logs.write('错误数据：\n')
                logs.write('\n'.join(fail_lists))
                logs.write('重复数据：\n')
                logs.write('\n'.join(duplicate_data))
            else:
                logs.write('->所有数据导入完成！\n')

        else:
            logs.write('->当前表，本科室无权导入！\n')
        logs.write('\n------ 所有表上传结束 ------\n')
        logs.close()

    return fail_lists, duplicate_data


def update_sums(table_name, sums, columns):
    '''
    更新数据汇总表
    :param table_name:
    :param sums:
    :param columns:
    :return:
    '''

    logs = open(log_path2, 'a')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs.write(time + ': 汇总表自动统计数据更新\n')

    for data in sums:
        # 定位可以更新的部分，部分属性是手工统计的, 部分结果为0，不予以更新
        update_lists = []
        for index in range(0, len(data)):
            if  data[index] :
                update_lists.append(index)

        new_data, new_datas, new_column = [], [], []
        for index in update_lists:
            new_column.append(columns[index])
            new_data.append(data[index])
        new_datas.append(new_data)

        insert(table_name, new_datas, new_column)
        update_data(table_name,  new_datas, new_column)

    logs.write('数据上传结束！\n')


