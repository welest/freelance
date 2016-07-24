import MySQLdb as mysql


class mysql_db:

	def __init__(self):
		self.ip = '192.168.0.233'
		self.user = 'root'
		self.passwd = 'dSm3445229'
		self.db = 'freelance'

	def connect(self):
		try:
			conn = mysql.connect( self.ip, self.user, self.passwd, self.db )		
		except mysql.Error:
			print ("connection false")
		cursor = conn.cursor()
		cursor.execute('SET NAMES `utf8`')
		try:
			cursor.execute('SELECT * FROM site')
		except mysql.Error:
			print ('net takoi bazi')
		result = cursor.fetchall()
		return result
#	cur.execute('insert into sites_inform values ("glav", "opisanie", "dostup", "link", "time", (select id from site where name_site="freelance") )')
#	print(result)

		conn.close()

#def main():
#	connect = mysql_db
#	vibor = connect().connect
#	for i in vibor():
#		print(i)
#
#if __name__ == '__main__':
#	main()