#coding:utf8
#以入口网页为参数，爬取相关的网页
from baike_spider import html_downloader
from baike_spider import html_output
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.ouput=html_output.HtmlOutput()

    #爬虫的调度程序
    def craw(self, root_url):
        #记录当前爬取得是哪个URL
        count=1
        #将入口网页添加进URL管理器
        self.urls.add_new_url(root_url)


        while self.urls.has_new_url():
            try:
                #从URL管理器中获取一个新的URL，下载相应内容
                new_url=self.urls.get_new_url()
                print 'craw%d :%s'%(count,new_url)
                html_cont=self.downloader.download(new_url)


                #爬取新网页中的新内容（URL,网页内容）
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.ouput.collect_data(new_data)

                count=count+1
                if count==10:
                    break
            except:
                print 'craw failed'

        self.ouput.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/item/Python"
    obj_spider= SpiderMain()
    obj_spider.craw(root_url)
