# Skripta koja prolazi kroz halooglasi, sekciju nekretnine i izabrane podatke pakuje u json
from bs4 import BeautifulSoup
import requests

#Broj stranica koje hocemo da skrejpujemo
pages = input('Enter number of pages: \t')

#Naziv json fajla u koji pakujemo dobijene podatke
naziv_fajla = input("Enter the file name: \t")

#Naziv grada koji zelimo da obradimo
naziv_grada = input("Enter name of the city: \t")

# Formiramo fajl u koji smestamo podatke
f = open(naziv_fajla + ".txt", "a")
# Upisujemo pocetne znakove json objekta
f.write("{" + '"' + "objekat" + '"' + ": [")

# key_number nam je redni broj objekta u jsonu, tj. stan koji upisujemo
key_number = 0

# Unosom promenljive pages smo odredili koliko stranica zelimo da skrepujemo
for num_page in range(1, int(pages)):
	# Saljemo request za grad koji smo prethodno uneli inputom
	r = requests.get("https://www.halooglasi.com/nekretnine/izdavanje-stanova/" + naziv_grada + "?page=" + str(num_page))
	# Supa sablon, uvek isto
	soup = BeautifulSoup(r.text, features='html.parser')
	# Pronalazimo div u kojem se nalaze nasi podaci i prolazimo kroz njega prikupljajuci podatke koji nas zanimaju
	results = soup.find_all('div', {'class': 'my-product-placeholder'})
	for result in results:
		# Uzimamo cenu
		cena = result.find('div', {'class': 'central-feature'}).text
		evro = cena.rstrip('.\xa0€')     								# Trimujemo spejs i skidamo znak evro
		tacka = evro.replace('.', '') 									# Popunjavamo listu i uklanjamo decimal point
		print(cena)
		naslov_find = result.find("h3", {"class":"product-title"}).text # Uzimamo naslov
		naslov = naslov_find.replace('"', '')							# Iz naslova uklanjamo navodnike, jer nam sjebe json objekat
		print(naslov)
		mesto = result.find("ul", {"class" : "subtitle-places"}).text   # Uzimamo mesto
		print(mesto)
		povrsina = result.find("ul", {"class" : "product-features"}).text # Uzimamo povrsinu
		print(povrsina)
		# Ovde zna da pukne ponekad, pa sam stavio try except
		try:
			about_find = result.find("p", {"class" : "product-description"}).text
			about = about_find.replace('"', '')

		except:
			print("none")
		print(about)
		# Ovde isto zna da zvekete pa sam ubacio try except
		try:
			f = open(naziv_fajla + ".txt", "a")
		except:
			print("JBG nesto puklo na appendu")
		# Ovo je najkonfuznija magija, koja je zapravo najprostija. Tu dodajem navodnike i zareze koji formiraju json objekat
		try:
			f.write("{\n" + '"' + "key_number" + '"' + ":" +  str(key_number)  + ",\n"
			+ '"' + "cena" + '"' + ":" + tacka + ",\n" 
			+ '"' + "naslov" + '"' + ":" + '"' + naslov + '"' + ",\n" 
			+ '"' + "mesto" + '"' + ":" + '"' + mesto + '"' + ",\n"
			+ '"' + "povrsina" + '"' + ":" + '"' + povrsina + '"' + ",\n" 
			+ '"' + "about" + '"' + ":" + '"' + about + '"' + "\n},")
		except:
			print("jbg nesto puklo na upisu")
		# Uvecavamo key_number predstavlja ID za svaki oglas
		key_number += 1
# Unos poslednjih zagrada koje uokviruju json objekat
f = open(naziv_fajla + ".txt", "a")
f.write("]}")

# TASK: Na kraju poslednjeg objekta skinuti zarez