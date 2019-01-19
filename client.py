from __future__ import print_function
import sys

import Pyro4.utils.flame



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



class Rmi():
	#pola

	src_file = None
	dest_name = None



	def zmienne(self):
		self.src_file = input("Wprowadz nazwe pliku zrodlowego z rozszerzeniem: ")
		self.dest_name = input("Wprowadz nazwe pliku docelowego: ")

	def checkname(self):
		while True:
			try:
				filesource = open(self.src_file, 'rb').read()
				return filesource
			except:
				print("Niepoprawna nazwa pliku zrodlowego, sprobuj jeszcze raz!")
				self.zmienne()
	def wysylanie(self):
		self.zmienne()
		c = self.checkname()
		# while True:
		# 	try:
		# 		filesource = open(self.src_file, 'rb').read()
		# 		return filesource
		# 	except:
		# 		print("do dupy")
		# 		self.zmienne()
		#wylacznie zaladowanie kodu na serwer
		flame.sendfile(self.dest_name, c)


	def moduly(self):
		self.zmienne()
		c = self.checkname()
		#modulesource = open(self.src_file).read()
		#wyslanie kodu JAKO MODUL (import):
		flame.sendmodule(self.dest_name, c)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = flame.module(self.dest_name).doSomething("Marcin", 42)
		print("\nresult from uploaded module:", result)

	def poprawnosc(self):
		self.zmienne()    #czekaj wrzuc tutaj tylko zmiernna self.src_ zrodlowego...									##czekaj.... wez w tym file source daj plik 4funkcja,py
		c = self.checkname()
		root = flame.evaluate(c)
		print("result=", root)
		

	def funkcja(self):
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

file = Rmi()
# Informacje na serwerze gdy polaczy sie z klientem
flame.builtin("print")("Serwer polaczyl sie z klientem")



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
		file.wysylanie()

	# wysylanie kodu jako modul na serwer	
	if wybor == "2":
		file.moduly()

	#sprawdzenie poprawnosci 
	if wybor == "3":
		file.poprawnosc()
	# sprawdzenie poprawnosci
	if wybor == "4":
		file.funkcja()
	#wyjscie z menu
	if wybor == "5":
		print ("Dziękujemy za skorzystanie z naszych usług. Do zoboczenia!")
		sys.exit(0)

def koniec():
	print("Dziękujemy za skorzystanie z naszych usług. Do widzenia! ")
	return False

while True:
	main()
	while True:
		a = input("Czy chciałbyś jeszcze skorzystać z któreś usługi? (y/n)")
		if a =='y':
			main()
		elif a != 'y' and a != 'n':
			print ("Wybrano niewłaściwy klawisz")
			a = input("Czy chciałbyś jeszcze skorzystać z któreś usługi? (y/n)")

		if a == "n":
			print("Dziękujemy za skorzystanie z naszych usług. Do zoboczenia!")
			sys.exit(0)


	






