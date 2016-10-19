# encoding: utf-8

'''
Created on 2016年7月24日

@author: Miao1
'''

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w')
        fout.write('<meta http-equiv="content-type" content="text/html;charset=utf-8">')  

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
#             print data['url']
#             print data['title']
#             print data['summary']
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title']) #python3 去掉encode('utf-8')
            fout.write("<td>%s</td>" % data['summary'])
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    



