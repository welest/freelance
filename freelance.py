#!/usr/bin/python3
import parse_freelance
import mysql_freelance
#from multiprocessing import Process, Queue
import multiprocessing as mp
import time

def main():
	i=0
	freelance = parse_freelance.freelance_ru
#	spisok = freelance.parse(freelance())
#	mp.set_start_method("spawn")
	q = mp.Queue()
	p = mp.Process(name = 'parse', target = freelance.parse, args=(freelance(), q))
	p.daemon = True
	p.start()
	time.sleep(1)
	print(q.get())
	p.join()

#	for ni in spisok:
#		print(ni)
#	mysql = mysql_freelance.mysql_db
#	parse = mysql.insert(mysql())

#	while i <= (len(spisok)-7):
#		mysql.insert(mysql(), *spisok[i:i+7])
#		i+=7

if __name__ == '__main__':
	main()