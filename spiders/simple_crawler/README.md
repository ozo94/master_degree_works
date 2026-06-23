# simple-crawler 
> 简单爬虫（爬取静态网页，没有使用框架，权当对爬虫工作机制的一个了解）


## 目标分析
> 确定目标，然后对目标进行分析（选择策略），包含三个分析方向。

在页面中通过右键审查元素的方式来获取一下三个元素的信息
- URL格式：限定抓取网页的范围
- 数据格式：根据需要抓取的信息，选择抓取的标签
- 网页编码：在代码解析器中指明编码格式

## 目标

百度百科Python词条相关词条的网页 -标题和简介

入口页：http://baike.baidu.com/item/Python

#### URL格式：

词条页面URL:/view/20965.htm

![none](http://omouah54e.bkt.clouddn.com/sipder/readme/URL.bmp)

非完整URL，在代码中我们还需要进行拼接

#### 数据格式：

##### 标题：

![none](http://omouah54e.bkt.clouddn.com/sipder/readme/%E6%A0%87%E9%A2%98.bmp)

##### 简介：

![none](http://omouah54e.bkt.clouddn.com/sipder/readme/%E7%AE%80%E4%BB%8B.bmp)

#### 页面编码：

找到网页的head（审查网页任意位置），找到网页的编码UTF-8

![none](http://omouah54e.bkt.clouddn.com/sipder/readme/page_encode.bmp)
