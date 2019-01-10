from __future__ import print_function
import sys

import Pyro4.utils.flame



if sys.version_info < (3, 0):
    input = raw_input

Pyro4.config.SERIALIZER = "pickle"  # flame requires pickle serializer

print("Start a Pyro Flame server somewhere.")
location = input("what is the location of the flame server, hostname:portnumber? ")
print()

# connect!
flame = Pyro4.utils.flame.connect(location)

# basic stuff
socketmodule = flame.module("socket")
osmodule = flame.module("os")
print("remote host name=", socketmodule.gethostname())
print("remote server current directory=", osmodule.getcwd())



class Rmi():
	#pola

	src_file = None
	dest_name = None

	#funkcje

	def numberoflines(self):
		number = 0
		filename = input('podaj nazwe pliku zrodklowego:')
		with open(filename, 'r') as f:
			for line in f:
				number += 1
		return number

	def zmienne(self):
		self.src_file = input("Wprowadz nazwe pliku zrodlowego: ")
		self.dest_name = input("Wprowadz nazwe pliku docelowego: ")


	def wysylanie(self):
		self.zmienne()
		filesource = open(self.src_file, 'rb').read()
		#wylacznie zaladowanie kodu na serwer
		flame.sendfile(self.dest_name, filesource)


	def moduly(self):
		self.zmienne()
		modulesource = open(self.src_file).read() 
		#wyslanie kodu JAKO MODUL (import):
		flame.sendmodule(self.dest_name, modulesource)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = flame.module(self.dest_name).doSomething("Marcin", 42)
		print("\nresult from uploaded module:", result)

	def poprawnosc(self):
		self.zmienne()    #czekaj wrzuc tutaj tylko zmiernna self.src_ zrodlowego...									##czekaj.... wez w tym file source daj plik 4funkcja,py
		filesource = open(self.src_file, 'rb').read()
		root = flame.evaluate(filesource)
		print("result=", root)
		flame.sendfile(self.dest_name, filesource)
		print('Zawartosc pliku z serwera:',flame.getfile(self.dest_name))

	def funkcja(self):
		modulesource = open ('function.py').read()
		#wyslanie kodu JAKO MODUL (import):
		flame.sendmodule('flameexample.function', modulesource)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = flame.module('flameexample.function').numberoflines(input("podaj nazwe pliku znajdującego się na serwerze"))
		print("\nWybrany program ma:", result, "lini kodu")
		r = self.numberoflines()
		print ('kod żródłowy zawiera:',r,'linii')
		if r==result:
			print ("Ilość linii kodu programu przesłanego na serwer jest równa ilości linii kodu źródłowego programu,", result,'=',r)


file = Rmi()
# Informacje na serwerze gdy polaczy sie z klientem
flame.builtin("print")("Serwer polaczyl sie z klientem")



def main():
	wybor = 0
	print ("Witaj programie klienta")
	while wybor != 1 and wybor !=2 and wybor !=3 and wybor != 4 and wybor != 5:
		print ("Aby uruchomic funkcje klienta wybierz jedna z wybranych opcji: ")
		
		print ("1 - Wysylanie pliku do serwera")
		print ("2 - Sprawdzenie poprawnosci kodu i kompilacja  ")
		print ("3 - Wykonanie programu")
		print ("4 - 4 funkcja")
		print ("5 - Wyjscie z programu")

		wybor = int(input("Podaj numer: "))
		if wybor != 1 and wybor !=2 and wybor !=3 and wybor != 5 and wybor != 4:
			print("Niewłaściwy wybór. Spróbuj jeszcze raz")
	#wyslanie pliku na serwer
	if wybor == 1:
		file.wysylanie()

	# wysylanie kodu jako modul na serwer	
	if wybor == 2:
		file.moduly()

	#sprawdzenie poprawnosci 
	if wybor == 3:	
		file.poprawnosc()
	# sprawdzenie poprawnosci
	if wybor == 4:
		file.funkcja()
	#wyjscie z menu
	if wybor == 5:
		print ("Dziękujemy za skorzystanie z naszych usług. Do zoboczenia!")
		sys.exit(0)

def koniec():
	print("Dziękujemy za skorzystanie z naszych usług. Do widzenia! ")
	return False

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
