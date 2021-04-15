import math


def trunc(liczba, dokladkosc):  # funkcja wycinająca niedokładność max do 15 cyfr po przecinku
	odwrotnosc_dokladnosci = 1 / dokladkosc
	liczba = math.trunc(liczba * odwrotnosc_dokladnosci)/odwrotnosc_dokladnosci
	return round(liczba, 15)


def algorytm(liczba, dokladnosc):  # właściwy algorytm
	a = liczba
	b = 1

	while math.fabs(a-b) >= dokladnosc:
		a = (a + b) / 2
		b = liczba / a

	# return trunc(a, dokladnosc)  # wynik z wycintą niedokładnością
	return a  # wynik niezmodyfikowany


print(algorytm(3, 0.0000001))
