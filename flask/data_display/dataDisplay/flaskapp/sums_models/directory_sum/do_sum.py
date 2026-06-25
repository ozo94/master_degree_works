# coding=utf-8
from dataDisplay.flaskapp.sums_models.rules import methods
from dataDisplay.flaskapp.models import *
from dataDisplay.flaskapp.sums_models.rules import  column_convert
from sqlalchemy import func
from . methods import read_ks_column


def show_ks_sums(directory_name):
    '''
    根据条件给出各科室目录的两类统计结果
    :param directory_name:
    :return:
    '''
    all_conditions = read_ks_column('dataDisplay/flaskapp/sums_models/directory_sum/sum.xlsx')
    # print  all_conditions
    # print directory_name, all_conditions.keys()[0]
    conditions = all_conditions[directory_name]

    ids = conditions[0]
    table_names = conditions[1]
    condition_names = conditions[2]
    condition_vals = conditions[3]
    add_columns = conditions[4]

    results = {}
    for index in range(len(ids)):
        id = ids[index]
        table_name = table_names[index]
        condition_name = condition_names[index]
        condition_val = condition_vals[index]
        add_column = add_columns[index].strip().strip('\n')
        # print id,table_name,condition_name,condition_val,add_column

        # 返回表单中对应数据库的数据集合，对应数据条目，对应的值累加计算
        result, result1, result2 = None, 0, 0

        if table_name.strip():
            if condition_name.strip():
                condition_name = condition_name.split(',')
                condition_val = condition_val.split(',')
                cmd = 'result = ' + table_name + '.query.filter('
                for i in range(len(condition_name)):
                    cmd +=  table_name + '.' + condition_name[i] + ".like('" + condition_val[i] + "')" + ','
                cmd += ').all()'
                print index, cmd
                exec(cmd)
            else:
                cmd = 'result = ' + table_name + '.query.all()'
                print index, cmd
                exec(cmd)
            result1 = len(result)

            if add_column:
                # 计算对应栏目的数值之和
                result_num = 0
                val = ''
                for data in result:
                    exec('val = data.' + add_column)
                    try:
                        result_num += float(val)
                    except:
                        print table_name, u'中，对应', add_column, u'属性值，存在', str(val), u'不合法！'
                result2 = result_num

        results.update({id:[result1, result2]})

    return results