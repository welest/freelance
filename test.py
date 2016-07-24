import time

spisok = []
chart = ['mama', 'pap']

def unic(word_list, ident_word):
	for words in word_list:
		if words == ident_word:
			return True

def perebor(list_num, list_chislo):
	on = 0
	while on < len(list_num):
		if unic(chart, list_num[on]):
				#one = list_num.index(move)
				spisok.append({'number' : list_num[on], 'chislo' : list_chislo[on]})
		on += 1

number = ['mama', 'papa', 'masha', 'mama']
chislo = ['a', 'b', 'v', 'n']


def main():
	i = 1
	on = 0

	while i <= 5:
#		time.sleep(2)
		perebor(number, chislo)
		i += 1
	for me in spisok:
		print(me)

if __name__ == '__main__':
	main()