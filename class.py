
class url:
	def __init__(self):
		self.a = 1
		self.b = 2

	def pas(self):
		return self.a + self.b

	def mnog(self, x):
		a = self.pas()
		print(a)
		print (self.b)

	def nam(self, x):
		self.mnog(x)

def main():
	rul = url
#	rul.nam(rul, rul().b)
#	rul.mnog(rul, rul().b)
	rul.nam(rul(), 2)


if __name__ == '__main__':
	main()