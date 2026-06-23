# 工作流程图安排
## 目标
- 了解学习目标
        利用LDA主题模型结合SVM分类算法，实现文本小实验
- 安装python64位
        安装相关Python包，实现jieba分词

##  data precessing and built corpus
> 完成语料库的建立和字典的建立
- 将result.txt处理成.dict文件
- 将语料进一步改造成Blei’s LDA-C形式的语料库

> 主要使用gensim这个库
- 英文官方网站：http://radimrehurek.com/gensim/tut1.html
- 中文参照：http://blog.csdn.net/questionfish/article/details/46739207

## TF_IDF, LDA
> 探究TF_IDA的使用
- 基于gensim.models中 TF_IDA的调用

> 探究LDA模型
- gensim中的LDA主题模型可以傻瓜式调用（主题的权重值可以是0）


## SVM
> 了解svm分类算法
> 应用一下svm模型
- sklearn上的函数调用说明：http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html