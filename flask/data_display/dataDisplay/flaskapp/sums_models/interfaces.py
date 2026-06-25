# coding=utf-8
'''
    extract_data(): 抽取所有表格，生成汇总表，耗时长
    get_area_data(table_name, area_name): 返回对应区镇的数据
    insert_db(path, xls_name, ks_name): 导入excel文件，对应科室增量更新
    update_db(path, xls_name): 根据Excel模板，按id新增、更新(id为主键)
    update_all(): 自动更新所有满足条件的汇总表数据,统计规则不完善，慎用
'''

from dataDisplay.flaskapp.sums_models.analysis.creat_extrat_table import extrat_data
from dataDisplay.flaskapp.sums_models.area_sel.area_data import get_area_data
from update import insert_db, update_db
from dataDisplay.flaskapp.sums_models.calculation.update import update_all

