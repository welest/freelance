import urllib
from multiprocessing import Pool
import requests

spisok = ['http://google.com', 'http://yandex.ru', 'https://mail.ru']
spisok1 = ['http://google.com', 'http://yandex.ru', 'https://mail.ru']
spisok2 = ['http://google.com', 'http://yandex.ru', 'https://mail.ru']
spisok3 = ['http://google.com', 'http://yandex.ru', 'https://mail.ru']
spisok4 = ['http://google.com', 'http://yandex.ru', 'https://mail.ru']
#spisok = [1,2,3,4,5]
spisokall = []

def dobav(*args):
	spisokall.append(args)
	spisokall.append(args)
	spisokall.append(args)
	spisokall.append(args)asd
	spisokall.append(args)
	return spisokall
#	return x*x
def main():

#	pool = Pool(1)
	result = map(dobav, (spisok, spisok1, spisok2, spisok3, spisok4 ))
#	result = pool.map(requests.get, spisok)
#	result = map(dobav, spisok)
#	for i in result: print(i)
#	pool.close()
#	pool.join()
	for i in result:
		print(i)
#	for i in spisok:
#		spisok1.append(urllib.urlopen(i))

if __name__ == "__main__":
	main()