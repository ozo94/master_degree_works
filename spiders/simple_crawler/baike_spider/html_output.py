#coding:utf8
class HtmlOutput(object):

    #用一个列表来维护收集的数据
    def __init__(self):
        self.datas=[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):

        fout = open('output.html','w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')

            fout.write("<td>%s</td>" % data['url'])

            #python默认编码为ascii，需要进行utf-8的转换  .encode('utf-8')
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))

            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()