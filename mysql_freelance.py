import pymysql

class mysql_db:

	def __init__(self):
		self.ip = 'mysql78.1gb.ru'
		self.user = 'gb_freelans'
		self.passwd = '3f4c548z234'
		self.db = 'gb_freelans'
		self.freelance = '(select id from sites where site_name="freelance")'
		self.repeat_title = '(select id from site_inform where title=%s)'
		self.repeat_text = '(select id from site_inform where title=%s, text= %s)'

#	проверка, есть ли такие данные уже в базе
	def double_title(self, title):
		conn = pymysql.connect( self.ip, self.user, self.passwd, self.db, use_unicode=True, charset='utf8')
		try:
			cursor = conn.cursor()
		except pymysql.Error:
			print("connection false")
		title_id = (self.repeat_title % '"{}"'.format(title))
		conn.close()
	#	if title_id > 0: return True
		return title_id

	def double_text(self, title, text):
		conn = pymysql.connect( self.ip, self.user, self.passwd, self.db, use_unicode=True, charset='utf8')
		try:
			cursor = conn.cursor()
		except pymysql.Error:
			print("connection false")
		text_id = (self.repeat_text % '"{}" "{}"'.format(title, text))
		conn.close()
#		if title_id > 0: return True
		return text_id

#	вставка строки в базу
	def insert(self, *args):
		conn = pymysql.connect( self.ip, self.user, self.passwd, self.db, use_unicode=True, charset='utf8')
		try:
			cursor = conn.cursor()
		except pymysql.Error:
			print("connection false")		
		site_id = cursor.execute("""%s""" % self.freelance)
		try:
			cursor.execute('SET NAMES utf8')
		except pymysql.Error:
			print('cant change unicode')
#		print(cursor.execute(self.repeat % args))
#		if result:
#			print('ok')
#		else:
#			print('no')
		try:
			print ('insert into site_inform values (%s, %s);' % (','.join('"{}"'.format(a) for a in args), site_id))
#			cursor.execute("""insert into site_inform (title, text, privileg, link, price, date, time, site_id) values (%s, %s);""" % (','.join('"{}"'.format(a) for a in args), site_id))
		except pymysql.Error:
			print ('insert into site_inform values (%s, %s);' % (','.join(args), site_id))
		conn.close()

def main():
	connect = mysql_db
	vibor = connect.insert(connect(), 'Change your life banner', 'pap', 'papa', 'mama', 'asd', 'asd')
	print(connect.double_text(connect(), 'papa', 'mama'))
	print (connect.double_title(connect(), 'papa'))

if __name__ == '__main__':
	main()