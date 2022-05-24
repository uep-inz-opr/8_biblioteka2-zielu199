class Biblioteka:
	lista_egzemplarzy = []
	lista_ksiazek = []
	ostateczna = []
	lista_czytelnikow = []
	czy_w_liscie = False

	def __init__(self, limit_wypozyczen):
		self.limit_wypozyczen = limit_wypozyczen

	def dodaj_egzemplarz_ksiazki(self, ksiazka):
		self.lista_ksiazek.append(ksiazka)
		return True

	def wypozycz(self, czytelnik, tytul):
		if len(czytelnik.lista_czytelnika) < 3:
			for ksiazka_wyp in self.lista_ksiazek:
				if ksiazka_wyp.tytul == tytul:
					for ksiazki_czytelnika in czytelnik.lista_czytelnika:
						if ksiazki_czytelnika.tytul == tytul:
							return False
					czytelnik.lista_czytelnika.append(ksiazka_wyp)
					self.lista_ksiazek.remove(ksiazka_wyp)
					return True
		return False

	def oddaj(self, nazwisko, tytul):
		for czytelnik in self.lista_czytelnikow:
			if czytelnik.nazwisko == nazwisko:
				for ksiazki_czytelnika in czytelnik.lista_czytelnika:
					if ksiazki_czytelnika.tytul == tytul:
						self.lista_ksiazek.append(ksiazki_czytelnika)
						czytelnik.lista_czytelnika.remove(ksiazki_czytelnika)
						return True
		return False

class Ksiazka:
	def __init__(self, tytul, autor, rok):
		self.tytul = tytul
		self.autor = autor
		self.rok = rok

class Egzemplarz:
	def __init__(self, rok_wydania, wypozyczony):
		self.rok_wydania = rok_wydania
		self.wypozyczony = wypozyczony

class Czytelnik:
	def __init__(self, nazwisko, lista_czytelnika):
		self.nazwisko = nazwisko
		self.lista_czytelnika = lista_czytelnika


n = int(input())
lista_akcji = [input().strip(' ') for akcja in range(n)]
akcje = []
biblioteka = Biblioteka(20)



for x in lista_akcji:
	nawias1 = x.replace("(", "")
	nawias2 = nawias1.replace(")", "")
	cudzyslow = nawias2.replace("\"", "")
	akcje = cudzyslow.split(", ")
	if akcje[0].strip() == "dodaj":
		ksiazka = Ksiazka(tytul=akcje[1].strip(), autor=akcje[2].strip(), rok=akcje[3].strip())
		print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
	if akcje[0].strip() == "wypozycz":
		jest_czytelnik = False
		tytul = akcje[2].strip()
		for czytelnik in biblioteka.lista_czytelnikow:
			if czytelnik.nazwisko == akcje[1].strip():
				jest_czytelnik = True
				print(biblioteka.wypozycz(czytelnik, tytul))
				break
		if not jest_czytelnik:
			nowy = Czytelnik(akcje[1].strip(), [])
			biblioteka.lista_czytelnikow.append(nowy)
			print(biblioteka.wypozycz(nowy, tytul))
	if akcje[0].strip() == "oddaj":
		nazwisko = akcje[1].strip()
		tytul = akcje[2].strip()
		print(biblioteka.oddaj(nazwisko, tytul))
