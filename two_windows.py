import subprocess

def okna():
	file = open('/home/welest/1.txt', 'a')
	file2 = open('/home/welest/2.txt', 'a')

	odin = subprocess.Popen( 'xterm', shell=True, stdout=file, stderr=file)
	odin1 = subprocess.Popen( 'xterm & ls -l', shell=True, stdout=subprocess.PIPE, stderr=file2).communicate()
	print(odin1)

def spisok(*args):
	print(",".join('"{}"'.format(a) for a in args))

spisok_full = ['papa', 'mama', 'papa', 'sister', 'sist', 'mother']
spisok_part = ['papa', 'sist', 'papa']
spisok_id = []


def oriverka_list(args):
	pass

def main():
	okna()

#	i = 0
#	while i < len(spisok_part):
#	for ni in spisok_part:
#		while i < len(spisok_full):
#			if ni == spisok_full[i]:
#				spisok_id.append(spisok_full.index(spisok_full[i]))
#			i+=1
#	print(spisok_id)



if __name__ == "__main__":
	main()