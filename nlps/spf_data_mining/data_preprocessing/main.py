# coding:utf-8
__author__ = 'zhangxiao'
__date__ = '2017-03-14'

from sentence import Sentence

if __name__ == '__main__':
    url_text = 'ml.txt'

    sentence = Sentence()

    f = open(url_text, 'r')
    txt_string = f.read().strip().decode('utf-8').replace('\n', ' ')

    # 获取中文内容
    step_1 = sentence.filter_chinese_character(txt_string)
    # 移除停用词
    step_2 = sentence.remove_stop_word(step_1)
    # 移除重复词
    step_3 = sentence.remove_repeat_word(step_2)

    print step_3