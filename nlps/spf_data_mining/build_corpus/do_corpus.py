# coding=utf-8
from gensim import corpora

# 产生对应格式的texts
def to_texts(file):
    datas = open(file, 'r')
    texts = [[word for word in data.split(',')]
             for data in datas]
    return texts

# 统计维度，并生成对应的字典（去除停用词以及仅出现一次词的id）
def tokens(texts):
    dictionary = corpora.Dictionary(texts)
    dictionary.save('temp/tokens.dict')

    # 停用词
    # stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
    #             if stopword in dictionary.token2id]

    # 出现一次的低频词
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems()
                if docfreq == 1]

    # 删除停用词和低频词，并去除不连续的缺口
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()

    # for index,data in dictionary.token2id.items():
    #     print index,data

    return dictionary

# 产生稀疏文档向量
def to_vectors(dictionary, texts):
    corpus = [dictionary.doc2bow(text) for text in texts]

    # 存入硬盘备用
    corpora.MmCorpus.serialize('temp/vectors.mm', corpus)

    # for data in corpus:
    #     print data


    return corpus

# 不同的语料库格式
def corpus_formate(corpus):
    #存储为不同的语料
    corpora.SvmLightCorpus.serialize('data/corpus.svmlight', corpus)
    corpora.BleiCorpus.serialize('data/corpus.lda-c', corpus)
    corpora.LowCorpus.serialize('data/corpus.low', corpus)

    #载入语料库
    corpus = corpora.MmCorpus('temp/vectors.mm')


if __name__ == '__main__':
    import logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    file = 'data/result.txt'
    texts= to_texts(file)
    dictionary = tokens(texts)
    corpus = to_vectors(dictionary, texts)
    corpus_formate(corpus)