from __future__ import print_function
import sys

import Pyro4.utils.flame


class Rmi():
	#pola

	src_file = None
	dest_name = None

	#funkcje

	def __init__(self):
		self.src_file = ''
		self.dest_name = ''


	def zmienne(self, source_file=None,dest_name=None):
		if source_file is None:
			self.src_file = input("Wprowadz nazwe pliku zrodlowego z rozszerzeniem: ")
		else:
			self.src_file = source_file

		if dest_name is None:
			self.dest_name = input("Wprowadz nazwe pliku docelowego z rozszerzeniem: ")
		else:
			self.dest_name = dest_name

	def checkname(self):
			while True:
				try:
					filesource = open(self.src_file, 'rb').read()
					return filesource
				except:
					print("Blad , wprowadz ponownie nazwy plikow z rozszerzeniami!")
					self.zmienne()
	def wysylanie(self,server):
		self.zmienne()
		c = self.checkname()
		server.sendfile(self.dest_name, c)
		return 1


	def moduly(self,server):
		self.zmienne()
		c = self.checkname()
		#modulesource = open(self.src_file).read()
		#wyslanie kodu JAKO MODUL (import):
		server.sendmodule(self.dest_name, c)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = server.module(self.dest_name).doSomething("Marcin", 42)
		print("\nresult from uploaded module:", result)

	def poprawnosc(self,server):
		self.zmienne()    #czekaj wrzuc tutaj tylko zmiernna self.src_ zrodlowego...									##czekaj.... wez w tym file source daj plik 4funkcja,py
		c = self.checkname()
		root = server.evaluate(c)
		print("result=", root)
		

	def funkcja(self,server):
		number = 0
		x = input("podaj nazwe pliku zrodlowego znajdujacego sie na serwerze ")
		modulesource = open ('function.py').read()
		#wyslanie kodu JAKO MODUL (import):
		flame.sendmodule('flameexample.function', modulesource)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = flame.module('flameexample.function').numberoflines(x)
		print("\nWybrany kod pliku przeslanego na serwer ma:", result, "linii kodu")
		with open(x, 'r') as f:
			for line in f:
				number += 1
		r = number
		print ('kod żródłowy pliku zawiera:',r,'linii')
		if r == result:
			print ("Ilość linii kodu programu przesłanego na serwer jest równa ilości linii kodu źródłowego programu,", result,'=',r)
		else: print("Ilosc linii kodu miedzy plikami na serwerze i kliencie rozni sie!")



def main():
	wybor = None
	print ("Witaj w programie klienta")
	while wybor != "1" and wybor != "2" and wybor !="3" and wybor != "4" and wybor != "5":
		print ("Aby uruchomic funkcje klienta wybierz jedna z wybranych opcji: ")
		
		print ("1 - Wysylanie pliku do serwera")
		print ("2 - Sprawdzenie poprawnosci kodu i kompilacja  ")
		print ("3 - Wykonanie programu")
		print ("4 - Raport")
		print ("5 - Wyjscie z programu")

		wybor = str(input("Podaj numer: "))
		if wybor != "1" and wybor != "2" and wybor != "3" and wybor != "4" and wybor != "5":
			print("Niewłaściwy wybór. Spróbuj jeszcze raz")
	#wyslanie pliku na serwer
	if wybor == "1":
		file.wysylanie(flame)


	# wysylanie kodu jako modul na serwer	
	if wybor == "2":
		file.moduly(flame)

	#sprawdzenie poprawnosci 
	if wybor == "3":	
		file.poprawnosc(flame)
	# sprawdzenie poprawnosci
	if wybor == "4":
		file.funkcja(flame)
	#wyjscie z menu
	if wybor == "5":
		print ("Dziękujemy za skorzystanie z naszych usług. Do zoboczenia!")
		sys.exit(0)

def koniec():
	print("Dziękujemy za skorzystanie z naszych usług. Do widzenia! ")
	return False


if __name__ == '__main__':
	if sys.version_info < (3, 0):
		input = raw_input

	Pyro4.config.SERIALIZER = "pickle"  # flame requires pickle serializer

	print("Start a Pyro Flame server somewhere.")
	def connection():
		location = input("what is the location of the flame server, hostname:portnumber? ")
		while True:
			try:
				flame = Pyro4.utils.flame.connect(location)
				print()
				return flame
			except:
				print('sproboj ponownie')
				location = input("what is the location of the flame server, hostname:portnumber? ")


flame = connection()


# basic stuff
socketmodule = flame.module("socket")
osmodule = flame.module("os")
print("remote host name=", socketmodule.gethostname())
print("remote server current directory=", osmodule.getcwd())

file = Rmi()
# Informacje na serwerze gdy polaczy sie z klientem
flame.builtin("print")("Serwer polaczyl sie z klientem")


while True:
	main()
	a= input("Czy chciałbyś jeszcze skorzystać z któreś usługi? (y/n)")
	if a =='y':
		main()
	elif a != 'y' and a != 'n':
		print ("Wybrano niewłaściwy klawisz")
		a = input("Czy chciałbyś jeszcze skorzystać z któreś usługi? (y/n)")

	if a == "n":
		print("Dziękujemy za skorzystanie z naszych usług. Do zoboczenia!")
		sys.exit(0)
