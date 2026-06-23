# coding=utf-8
from sklearn import svm, preprocessing, metrics
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
import numpy as np
import pandas as pd
import time

def do_svm(x_file, y_file, rate, cv):
    start = time.time()

    x = pd.read_csv(x_file, header=None)
    y = pd.read_csv(y_file, header=None)

    # 样本的标准化处理（这里，标签Y并不需要标准化处理）
    scaler = preprocessing.StandardScaler().fit(x)
    print scaler
    x_transform = scaler.transform(x)

    svc_model = svm.SVC(kernel= 'linear', C=1)

    # （1）传统的验证集，测试集的划分
    # train_x, test_x, train_y, test_y = train_test_split(x_transform, y, test_size=rate, random_state= 11)
    #
    # svc_model.fit(train_x, train_y)
    # result = svc_model.score(test_x, test_y)
    #
    # prediction = svc_model.predict(test_x)
    # result = metrics.classification_report(test_y, prediction)

    # （2）交叉验证法（cross_val_score）,用法好像有点问题
    y = y.values[: , 0]
    svc_model = svm.SVC(kernel= 'linear', C=1)
    result = cross_val_score(svc_model, x_transform, y, cv=cv)


    end = time.time()

    print '---------- svm model leaning ---------- \ntime cost: %0.2f' % (end-start),  \
        "\nAccuracy: %0.2f (+/- %0.2f)" % (result.mean(), result.std() * 2), '\n'



if __name__ =='__main__':

    x_file = '../tfidf_LDA/data/train_x.csv'
    y_file = 'data/train_y.csv'

    do_svm(x_file, y_file, rate=1/3.0, cv= 5)