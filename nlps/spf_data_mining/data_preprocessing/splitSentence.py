# coding:utf-8
__author__ = 'zhuzheng'
__date__ = '2017-03-14'

import re
import sys
import jieba
import jieba.posseg as pseg


# 分词去停用词
def splitSentence(inputFile, outputFile):
    stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt')])
    f = open(inputFile, 'r')
    txtlist = f.read().strip().decode('utf-8').replace('\n', ' ')
    xx = u"([\u4e00-\u9fa5]+)"
    pattern = re.compile(xx)
    results = pattern.findall(txtlist)
    str = ''.join(results)
    words = pseg.cut(str)
    f.close()
    count = 0
    for w in words:
        count = count + 1
        if ((w.flag == 'n' or w.flag == 'v') and len(w.word) > 1):
            if w.word.encode('gbk') not in stopwords:
                f = open(outputFile, 'a')
                f.write(w.word.encode('utf-8'))
                f.write(',')

    f.close()


# 去除重复词语
def extract(inputFile, outputFile):
    f = open(inputFile, 'r')
    txtlines = f.read().strip().decode('utf-8')
    f.close()
    txtlines = txtlines.replace('\n', '').split(u',')
    wordset = list(set(txtlines))
    count = 0
    f = open(outputFile, 'a')
    for word in wordset:
        count = count + 1
        f.write(word.encode('utf-8'))
        f.write(',')

    f.close()


splitSentence('split_test/ml.txt', 'split_test/split.txt')
extract('split_test/split.txt', 'split_test/extract.txt')
