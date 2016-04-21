'''
·打开一个网页、读出网页代码（模块urllib.request）
·查找需要的信息（正则表达式）
·打印出查找的信息
'''
import urllib.request       #网络相关
import re                   #正则表达式
import urllib.parse         #网址解析器=拆解、合并

def get_html(url):
	data=urllib.request.urlopen(url).read().decode('UTF-8')
	print('运行函数')
	return data

def get_need(guize,ku,url):	
	need=[]
	ZZ_href=re.compile(guize)
	WD_href=ZZ_href.findall(ku)
	url_o=urllib.parse.urlparse(url)
	for i in range(len(WD_href)):
		o=urllib.parse.urlparse(WD_href[i][6:-1])#解析网址
		if o[1]==url_o[1]:
			need.append(WD_href[i][6:-1])
		elif o[1]=='':
			to=urllib.parse.urljoin(url,o[2])
			need.append(to)
	print('运行函数get_need')		
	return need

def __main__():
	url="http://www.16sucai.com/"
	guize="href=\".+?\""
	print('-------------------start get html-------------')
	html_data=get_html(url)
	print('-------------------findall-------------')
	need_data=get_need(guize,html_data,url)
	for need1 in need_data:
		print(need1)

if __name__ == '__main__':
	__main__()



'''
#image=re.compile(r"http.+?\.jpg|http.+?\.npg")
'''

