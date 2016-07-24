import requests
from lxml import etree
import lxml.html
import time
import re

class freelance_ru:

	def __init__(self):
		self.main_url = 'https://freelance.ru/projects/filter/'
		self.main_spisok = []

	def unic(self, ident_word):
		word_list = ['php']
		for words in word_list:
			if words in ident_word.lower():
				return True

	def create_spisok(self, list_work, web_page):
		on = 0
		while on < len(list_work):
#			if self.unic(list_work[on]):
			privileg = web_page.xpath('//*[@class="proj-inf status pull-left"]/text()')
			price = web_page.xpath('//*[@class="cost"]/b/text()')
			link = web_page.xpath('//*[@class="ptitle"]/@href')
			text = web_page.xpath('//*[@class="descr"]/p/span[2]/text()')
			date = web_page.xpath('//*[@class="proj-inf pdata pull-left"]/text()')
			time = web_page.xpath('//*[@class="proj-inf pdata pull-left"]/@title')
#			self.main_spisok.append({'work' : list_work[on],
#								   'dostup' : privileg[on],
#						 		    'money' : price[on],
#								     'link' : 'https://freelance.ru' + link[on],
#					 		     'opisanie' : text[on].replace('\n', ''),
#					 		  	  	 'data' : time[on]})
			self.main_spisok.append(re.sub(r'[\"\'\n\r\t\."]', '', list_work[on]))
			self.main_spisok.append(re.sub(r'[\"\'\n\r\t]', '', text[on]))
			self.main_spisok.append(privileg[on])
			self.main_spisok.append('https://freelance.ru' + link[on])
			self.main_spisok.append(re.sub(r'[\s]', '', price[on]))
			self.main_spisok.append(date[on][-8:])
			self.main_spisok.append(time[on][-5:])
			on += 1

	def parse(self, q):
		i = 1
		try:
			zapros = requests.get(self.main_url)
			tree = lxml.html.document_fromstring(zapros.text)
		except:
			print('connection timeout')
		page = tree.xpath('//*[@class="pagination pagination-sm"]/li/a/text()')
		a = int(page[-2])
		while i <= 3:
			time.sleep(2)
			parse_url = self.main_url + '?page=' + str(i)
			zapros_parse = requests.get(parse_url)
			tree_parse = lxml.html.document_fromstring(zapros_parse.text)
			name_work = tree_parse.xpath('//*[@class="ptitle"]/span/text()')
			self.create_spisok(name_work, tree_parse)
#			print('page '+str(i))
			i += 1
		return self.main_spisok
#	for i in (tree.xpath('//*[@class="avatr"]/img')):
#		print('https://freelance.ru' + i.attrib['src'])