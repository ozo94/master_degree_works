# coding=utf-8
import datetime
from dataDisplay.flaskapp.sums_models.rules.methods import page_tables, show_columns

log_path = 'datadisplay/flaskapp/data/logs.txt'



def convert_table_name(xls_sheet, year_name, conditions_name, re_flag= '', operation= ''):
    '''
    获取对应sheet表,所对应的mysql数据库中的表名
    :param xls_sheet:
    :return: str,所有的都是字符串形式的（多个值','隔开）
    '''
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs = open(log_path, 'a')

    # （1）对应科室，sheet表转化
    # 读取pagetable.txt文件，建立中英文名的对照字典
    table_names = page_tables()

    # print xls_sheet
    xls_name = xls_sheet.split(',')[0].strip()
    sheet_name = xls_sheet.split(',')[1].strip()

    try:
        table_name = table_names[sheet_name].strip('\n')
    except Exception,e:
        error =  u'规则中定义了不存在的sheet：' + xls_sheet
        table_name = ''
        print sheet_name
        logs.write(time + ' error:' +'('+ error + ')\n')

    # （2）决定年份的属性，以及要查询的条件属性（year,condition_names）
    columns = show_columns()

    column = columns[table_name]
    org_column = column[0]
    ref_column = column[1]

    column_ref = {}
    for index in range(len(org_column)):
        key = unicode(org_column[index], 'utf-8')
        column_ref.update({key: ref_column[index]})
    # print ','.join(column_ref.keys())

    try:
        # print year_name
        year_ref = column_ref[year_name]
    except Exception,e:
        year_ref = ''
        if year_name:
            error =  xls_name + u'.xls中的' + sheet_name + '(' + table_name + ')' + u'没有对应的属性:' + year_name
            print error
        # logs.write(time + 'error:'  + error + ')\n')



    condition_ref = []
    if conditions_name.strip():
        conditions = conditions_name.split(',')
        for condition in conditions:
            try:
                ref_name = column_ref[condition.strip()]
                condition_ref.append(ref_name)
            except Exception, e:
                print u'筛选条件出错：', sheet_name, u'中没有', condition

    condition_ref = ','.join(condition_ref)

    # （3）要求数据去重时的变量名set_flag
    if re_flag:
        flag_ref = column_ref[re_flag]
    else:
        flag_ref = ''

    # （5）采用何种方式统计，计算查询到的条目数，还是计算对应属性下值
    if operation:
        operation = column_ref[operation]
    else:
        operation = ''

    return table_name, year_ref, condition_ref, flag_ref, operation


