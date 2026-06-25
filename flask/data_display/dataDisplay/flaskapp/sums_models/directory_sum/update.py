# coding=utf-8
from . import do_sum

# 六个科室的名称
directory_dict = [u'成果科汇总表', u'高新科汇总表', u'法规科汇总表', u'专利科汇总表', u'农社科汇总表', u'合作交流科汇总表']

def update_directory():
    '''
    更新六个科室所有的目录表
    :return:
    '''
    results = {}
    for directory in directory_dict:
        result = do_sum.show_ks_sums(directory)
        results.update({directory: result})

    return results