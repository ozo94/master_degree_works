# coding=utf-8
__author__ = 'zhang jian'
__date__ = '2017-6-20'

from tfidf_LDA import do_lda
from svm_model import do_svm
from gensim import corpora

def lda_svm(topic_num, rate, cv):
    '''
        对于全新的文本库，需要进行预处理操作
        执行data_processing, 将所有的文本读入一个result.txt文件中去
        执行build_corpus, 生成对应的维度词典以及语料库
        LDA生成主题模型，投入对应的SVM模型中去
        期间所有的中间文件，存储在data_mining_learning/data下
    '''

    # 给出LDA主题模型，自己定义LDA的主题数目
    corpus_url = 'build_corpus/temp/vectors.mm'
    corpus = corpora.MmCorpus(corpus_url)

    do_lda.to_ldaModel(corpus, topic_num)

    # 投入svm模型中去（LDA的主题分布函数，则为SVM模型的属性）
    x_file = 'data/train_x.csv'
    y_file = 'data/train_y.csv'

    do_svm.do_svm(x_file, y_file, rate, cv)


if __name__ == '__main__':

    # 给定参数, 当选用交叉验证时，rate参数则是没有用的
    topic_num = 20
    test_rate = 1/4.0
    cv = 5

    topic_nums = [10, 20, 30, 50, 80, 100, 200]
    for topic_num in topic_nums:
        lda_svm(topic_num, test_rate, cv)