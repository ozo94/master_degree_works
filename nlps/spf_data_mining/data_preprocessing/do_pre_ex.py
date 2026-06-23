# coding=utf-8
import os

# os.walk方法以最小的子文件夹为单位，读取该文件夹下所有的内容
# 文件路径，好像不区分正反斜杠（默认反斜杠）
rootdir = '../data_01/'
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        path = os.path.join(parent,filename)
        print path