# coding:utf-8
__author__ = 'zhangxiao'
__date__ = '2017-03-14'

import re
import jieba.posseg as pseg


class Sentence(object):
    # 停用词表的文件路径
    url_stopwords = 'data/stopwords.txt'

    def __init__(self):
        pass

    # 获取当前文本中的汉字内容
    def filter_chinese_character(self, string):
        regex = u"([\u4e00-\u9fa5]+)"
        pattern = re.compile(regex)
        results = pattern.findall(string)
        return ''.join(results)

    # 移除当前文本中的停用词
    def remove_stop_word(self, string):
        # 生成停用词的字典键值列表
        stop_words = {}.fromkeys([line.rstrip() for line in open(self.url_stopwords)])
        all_words = pseg.cut(string)
        filter_words = ''
        for word in all_words:
            if ((word.flag == 'n' or word.flag == 'v') and len(word.word) > 1):
                if word.word not in stop_words:
                    filter_words += word.word.encode('utf-8') + ','
        return filter_words

    # 移除当前文本中的重复词
    def remove_repeat_word(self, string):
        tmp_list = string.split(',')
        word_set = list(set(tmp_list))
        result = ','.join(word_set)
        return result.strip(',')
