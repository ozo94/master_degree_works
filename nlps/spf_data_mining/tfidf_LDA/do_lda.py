# coding=utf-8
from gensim import corpora, models
import time

def to_ldaModel(corpus, topic_num):
    start = time.time()

    lda = models.LdaModel(corpus, num_topics= topic_num)

    # 打印到csv文件中去，观察文件的内容格式。发现主题模型每次训练完之后，得到的主题分布结果是不一致的
    lda_file = open('data/lda_file.csv', 'w')
    train_x = open('data/train_x.csv', 'w')
    for each in lda[corpus]:
        lda_file.write(str(each)+ '\n')

        # 将主题模型存储为对应的train_x,没有主题分布的地方补充为0
        x_each = []
        attr_no = 0
        for attribute in each:
            for key  in range(attr_no, int(attribute[0])):
                x_each.append(0.0)
            x_each.append(attribute[1])
            attr_no = int(attribute[0])+1
        for key in range(attr_no, topic_num):
            x_each.append(0)

        train_x.write(str(x_each)[1:-1]+'\n')

        end =time.time()

    print '---------- build lda model ---------- ', '\ntopic_num: ', topic_num, \
            '\ntime cost: %0.2f' % (end-start)


if __name__ == '__main__':

    corpus_url = '../build_corpus/temp/vectors.mm'
    corpus = corpora.MmCorpus(corpus_url)
    to_ldaModel(corpus , topic_num= 50)