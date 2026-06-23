# coding=utf-8
from gensim import corpora,models



def to_Tfidmodle(corpus):
    tfidf = models.TfidfModel(corpus)
    tfidf.save('data/corpus.tfidf_model')


    # 输出所有的结果，tfidf[]中的参数值得最小单位是一个文档， 可以显示部分的结果
    # fopen = open('data/tfidf.csv', 'w')
    # for doc in tfidf[corpus]:
    #     fopen.write(str(doc)+'\n')

    # 基于上述代码生成模型后，idf已经存为模型的参数了；而tf 则是根据新给的some_doc来确定
    # some_doc = [(1590,1), (1,1)]
    # print tfidf[some_doc]


if __name__ == '__main__':
    corpus_url = '../build_corpus/temp/vectors.mm'
    corpus = corpora.MmCorpus(corpus_url)
    to_Tfidmodle(corpus)

    # 查看处理好的语料
    # fopen = open('data/corpus.csv', 'w')
    # for each in corpus:
    #     fopen.write(str(each)+'\n')
    #
    # to_Tfidmodle(corpus)
