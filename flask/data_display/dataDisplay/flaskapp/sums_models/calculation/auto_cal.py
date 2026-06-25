# coding=utf-8
from dataDisplay.flaskapp.sums_models.rules import methods,column_convert
from dataDisplay.flaskapp.models import *
from dataDisplay.flaskapp.sums_models import methods

def select_table(table_name, conditions, year):
    '''
    根据excle表格中给定的规则来更新汇中表数据
    :param table_name:
    :param conditions:
    :param year:
    :return:
    '''

    # 读取对应sums中的规则, 每个变量都是一个list
    re_tab_names = conditions[0]
    re_year_names = conditions[1]
    condition_names = conditions[2]
    condition_vals = conditions[3]
    do_set = conditions[4]
    operations = conditions[5]
    relationships = conditions[6]


    # 设定sums中的id与year
    id = methods.find_id(table_name, year)
    result_nums = []
    result_nums.append(id)
    result_nums.append(year)

    # 获取后续的不同属性的统计结果
    for index in range(2, len(re_tab_names)):

        re_name = re_tab_names[index]
        re_year = re_year_names[index]
        condition_name =condition_names[index].split(',')
        condition_val = condition_vals[index].split(',')
        set_flag = do_set[index]
        operation = operations[index]


        # 根据sheet名，进行总结表进行更新
        if re_name:
            # 按照年份查询，年份是总结表的主要属性
            result = None
            cmd = 'result =' + re_name + '.query.filter(' + re_name + '.' + re_year + ".like('%' + str(year)+ '%')"

            # 判断查询时是否有额外的附加条件
            if ''.join(condition_name):
                for i in range(len(condition_name)):
                    cmd += ', ' + re_name + '.' + condition_name[i] + ".like('" + condition_val[i] + "')"
                cmd += ').all()'
            else:
                cmd += ').all()'
            exec(cmd)


            # 判断查询结果中是否要去重
            if set_flag:
                # print set_flag
                tmp = set()
                for i in range(len(result)):
                    exec('tmp.add(result[i].'+ set_flag + ')')

                result = list(tmp)


            # 选择何种统计方式，默认计算条目数，给出属性名时，计算该属性名下数值总和
            if operation:
                result_num = 0
                val = ''
                for data in result:
                    exec('val = data.' + operation)
                    try:
                        result_num += int(val)
                    except:
                        print table_name, u'中，对应', operation, u'属性值，存在', val, u'不合法！'

            else:
                result_num = len(result)

        else:
            result_num = ''

        result_nums.append(result_num)

    # 有些查询的结果需要加减法处理一下
    for index in range(len(relationships)):
        rel = relationships[index]
        if rel:
            sign = rel[0]

            # 将excle中的字母序号，转化成所对应的数字序号(‘AA’ = 27)
            ignore = 2
            column_id = 0
            rev_column = rel[:0:-1]
            # print rev_column
            for c_index in range(len(rev_column)):
                ch = ord(rev_column[c_index].upper())- 64
                # print ch
                column_id += ch * pow(26, c_index)
            column_id -= ignore
            # print 'column_id ', column_id

            if sign == 'm':
                result_nums[index] -= result_nums[column_id]
            elif sign == 'a':
                result_nums[index] += result_nums[column_id]

    return result_nums

