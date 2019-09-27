class ayam(object):
	def __init__(self, m, k, s):
		self.mata = m
		self.kaki = k
		self.sayap = s

	def hitungVolume(self):
		return self.mata * self.kaki * self.sayap

	def cetakData (self):
			print("mata\t: ", self.mata)
			print("kaki\t: ", self.kaki)
			print("sayap\t: ", self.sayap)

	def cetakVolume(self):
			print("volume\t= ", self.hitungVolume())

	# mendefenisian kelas turunan(subclass)
class warna_ayam (ayam):
	def __init__ (self, m, k, s, w):

	# memanggil ayam.__init__()
		super(warna_ayam, self).__init__(m, k, s)
	# menambah atribut baru
		self.warna = w
	def cetakData (self):
	# membuat objek warna_ayam
		super (warna_ayam, self).cetakData()
		print("warna\t: ", self.warna)
		

def main ():
	# membuat objek warna_ayam
	warna_ayam1 = warna_ayam(2, 2, 2, "hitam")

	# menggunakan objek 
	warna_ayam1.cetakData()
	warna_ayam1.cetakVolume()

if __name__ == "__main__":
	main()
	