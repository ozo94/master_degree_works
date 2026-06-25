# coding=utf-8
import xlrd
import re
from dataDisplay.flaskapp.sums_models.rules.column_convert import convert_table_name

def get_sums_rule(filepath):
    '''
    获取每张总结表中的表头，其属性对应其他基础表中的哪些属性
    包括对应基础的表名，在该表中的年份英文名，判断条件（conditons）
    以及总结表中自身属性之间的联系
    :param filepath:
    :return:
    '''
    sums_rule = {}

    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    nrows = table.nrows

    for index in range(1, nrows, 10):
        re_tab_names = []
        re_year_names = []
        condition_names = []
        condition_vals = []
        do_set = []
        operations = []
        relationships = []

        # 对应的excle的sheet表名字，以及对应的数据库table名
        names = table.row_values(index)[0].split('.')
        sheet_name = names[1]
        table_name = 'sums' + '_' + re.findall(r'\d+', names[0])[0]

        # 计算对应表头的长度，不然会默认为excle中最大的表头长度
        length = 0
        for data in table.row_values(index+1):
            if data.strip():
                length += 1

        for i in range(1, length):
            re_tab_name = table.row_values(index+2)[i]
            re_year_name = table.row_values(index+3)[i]
            condition_name = table.row_values(index+4)[i]
            condition_val = table.row_values(index + 5)[i]
            set_flag = table.row_values(index+6)[i]
            operation = table.row_values(index+7)[i]
            relationship = table.row_values(index+8)[i]

            # 将规则中的各类数据中文名映射成对应的英文
            if re_tab_name.strip():
                # print re_tab_name
                re_tab_name, re_year_name, condition_name, set_flag, operation = convert_table_name(re_tab_name, re_year_name, condition_name, set_flag, operation)

            re_tab_names.append(re_tab_name)
            re_year_names.append(re_year_name)
            condition_names.append(condition_name)
            condition_vals.append(condition_val)
            do_set.append(set_flag)
            operations.append(operation)
            relationships.append(relationship)

        # print ','.join(re_tab_names)

        sums_rule.update({table_name:[re_tab_names, re_year_names, condition_names, condition_vals, do_set, operations, relationships]})

    return sums_rule