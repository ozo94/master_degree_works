# coding=utf-8
import pandas as pd

# 读取文本的分布（包括文档数和标签值）
def fileDis(fileroot):
    file_dis = open('data/file_distribution.txt', 'r')

    file_distribution = []
    for each in file_dis:
        elements = each.split(',')
        label = elements[0]
        pages = elements[1]
        file_distribution.append([int(label), int(pages)])

    return file_distribution

def give_train_Y(file_dis):
    train_y = open('../data/train_y.csv', 'w')
    for dis in file_dis:
        for i in range(0, dis[1]):
            train_y.write(str(dis[0])+ '\n')

if __name__ == '__main__':

    file_root = 'data/file_distribution.txt'
    file_dis = fileDis(file_root)
    give_train_Y(file_dis)