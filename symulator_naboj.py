pocisk_typ = ["ćwiczebny", "zwykły", "smugowy", "przeciwpancerny", "z zubożonym uranem"]
luska_material = ["mosiądzu","stopu aluminium lub stali","plastiku"]
splonka_typ=["Berdan", "Boxer"]
kaliber_mm=[5.45, 5.56, 6, 7, 7.62, 7.7, 7.92]

class naboj():
    def __init__(self, pocisk, luska, splonka, kaliber):
        self.__proch = "bezdymnym"
        self.pocisk = pocisk
        self.luska = luska
        self.splonka = splonka
        self.__kaliber = kaliber
    def __str__(self):
        return "Nabój {0}, kalibru {1} o łusce wykonanej z {2}, elaborowany prochem {3} ze spłonką typu {4} ".format(self.pocisk, self.__kaliber, self.luska, self.__proch, self.splonka)

class symulacja(naboj):
    """Przykład dla 7,62x39 mm:
          a) masa pocisku dla typu:
             - ćwiczebnego 7g?
             - zwykłego 7.91g
             - smugowego 7.45g
             - ppanc 7.77g
          b) długość pocisku 27mm
          c) masa prochu: 1.6-1.8g
        Długość lufy wpływa na prędkość np. dla standarowego naboju 7.62x39 mm prędkość początkowa dla lufy długości 415mm wynosi 715 m/s a dla lufy 520mm 735 m/s
        """
    def __init__(self, pocisk, luska, splonka, kaliber, pocisk_masa, dlugosc_pocisku, dlugosc_luski, masa_prochu, dlugosc_lufy):
        naboj.__init__(self, pocisk, luska,  splonka, kaliber)
        self.__pocisk_masa = pocisk_masa
        self.__dlugosc_pocisku=dlugosc_pocisku
        self.__dlugosc_luski=dlugosc_luski
        self.__masa_prochu=  masa_prochu
        self.__dlugosc_lufy=dlugosc_lufy

    def predkosc_wylotowa(self):
        if(self.pocisk==pocisk_typ[0]):
            typ=0.4
        elif(self.pocisk==pocisk_typ[1]):
            typ=0.5
        elif (self.pocisk == pocisk_typ[2]):
            typ=0.35
        elif (self.pocisk == pocisk_typ[3]):
            typ=0.75
        else:
            typ=1
        prd= self.__masa_prochu*self.__dlugosc_lufy
        prd=prd/((typ*self.__pocisk_masa)/4.01)
        print("Prędkość wylotowa tego pocisku wynosi: "+str(prd)+" m/s")
        print("UWAGA: Wzór został zmyślony i pewność wyniku zbliżonego do rzezczywistego istnieje tylko w przypadku gdy użyje się wartości odpowiednich dla\nzwykłego naboju kalibru 7.62x39mm i lufy o długości 415mm. (dla lufy długości 520mm wzór jest już nie prawidłowy, myli się o około 100m/s)\nJego parametry są zawarte w komentarzu wewnątrz klasy symulacja.")
    def niezawodnosc(self):
        niezawodnosc=1

        if(self.splonka==splonka_typ[0]): niezawodnosc-=0.15

        if(self.luska==luska_material[0] or self.luska==luska_material[1]): niezawodnosc-=0
        else: niezawodnosc-=0.1

        if(self.pocisk==pocisk_typ[0]): niezawodnosc-=0
        elif(self.pocisk==pocisk_typ[1]): niezawodnosc-=0.05
        elif(self.pocisk==pocisk_typ[2]): niezawodnosc-=0.10
        elif(self.pocisk==pocisk_typ[3]): niezawodnosc-=0.15
        else: niezawodnosc-=0.20

        if(self.__masa_prochu<(0.2*self.__pocisk_masa) or self.__masa_prochu>(0.33*self.__pocisk_masa)):
            pom=self.__pocisk_masa/(self.__masa_prochu*30)
            pom=round(pom, 2)
            niezawodnosc-=pom
            if(niezawodnosc<0):
                print("Nabój jest tak zły, że aż przelicznik wszedł na ujemne.")
        print("Niezawodność takiego naboju to: "+str(niezawodnosc)+" na 1")
        print("UWAGA: Oczywiście ten wzór na niezawodność może być błędny, nie posiadam żadnych dowodów na jego poprawność.")

    def dlugosc_naboju(self):
        g=float(input("\nPodaj ile procent pocisku ma wystawać z łuski (wartość min: 0, wartość maksymalna 0.9): "))
        while (g<0 or g>0.9):
            g = float(input("\nPodaj ile procent pocisku ma wystawać z łuski (wartość min: 0, wartość maksymalna 0.9): "))
        dl_naboju=self.__dlugosc_luski+(self.__dlugosc_pocisku*(0+g))
        print("\nDługość naboju to: "+str(round(dl_naboju,2))+" mm")
        "Sprawdzenie poprawności wzoru na naboju 7.62x39mm (0.6481) pokazało poprawny wynik"
    def __str__(self):
        return super().__str__()+"o masie pocisku {0}g, długości pocisku {1}mm, długości łuski {2}mm i prochem o masie {3}g zostaje wystrzelony z lufy o długości {4}mm".format(self.__pocisk_masa, self.__dlugosc_pocisku, self.__dlugosc_luski, self.__masa_prochu, self.__dlugosc_lufy)

"wybór typu pocisku"

for i in range(len(pocisk_typ)):
    print(i,") ",pocisk_typ[i])
a=int(input("Wybierz typ pocisku (wpisz numer porządkowy i zatwierdź eneterem): "))
while (a>len(pocisk_typ)-1 or a<0 ):
    a = int(input("Wybierz typ pocisku (wpisz numer porządkowy i zatwierdź eneterem): "))



"wybór materiału z którego wykonana jest łuska"

for i in range(len(luska_material)):
    print(i,") ",luska_material[i])
b=int(input("\nWybierz materiał łuski (wpisz numer porządkowy i zatwierdź eneterem): "))
while (b>len(luska_material)-1 or b<0 ):
    b = int(input("Wybierz materiał łuski (wpisz numer porządkowy i zatwierdź eneterem): "))



"wybór typu spłonki"

for i in range(len(splonka_typ)):
    print(i,") ",splonka_typ[i])
c=int(input("Wybierz typ spłonki (wpisz numer porządkowy i zatwierdź eneterem): "))
while (c>len(splonka_typ)-1 or c<0 ):
    c = int(input("Wybierz typ spłonki (wpisz numer porządkowy i zatwierdź eneterem): "))



"wybór kalibru"

for i in range(len(kaliber_mm)):
    print(i,") ",kaliber_mm[i])
d=int(input("\nWybierz kaliber (wpisz numer porządkowy i zatwierdź eneterem): "))
while (d>len(kaliber_mm)-1 or d<0 ):
    d = int(input("Wybierz kaliber (wpisz numer porządkowy i zatwierdź eneterem): "))



"masa pocisku"

pocisk_masa=float(input("\nPodaj masę pocisku (liczba w gramach): "))
while (pocisk_masa<=0 ):
    pocisk_masa = float(input("Podaj masę pocisku (liczba w gramach): "))



"długość pocisku"

dlugosc_pocisku = float(input("\nPodaj długość pocisku (liczba w milimetrach): "))
while (dlugosc_pocisku <= 0):
    dlugosc_pocisku = float(input("Podaj długość pocisku (liczba w milimetrach): "))

"długość łuski"

dlugosc_luski = float(input("\nPodaj długość łuski (liczba w milimetrach, 75% jej długości musi być większa od długości pocisku): "))
while (dlugosc_luski <= 0 or (0.75*dlugosc_luski)<dlugosc_pocisku):
    dlugosc_luski = float(input("Podaj długość łuski (liczba w milimetrach, 75% jej długości musi być większa od długości pocisku): "))

"masa prochu"

masa_prochu=float(input("\nPodaj masę prochu (liczba w gramach najlepiej pomiędzy 1/5 a 1/3 masy pocisku, inaczej nabój może być zawodny): "))
while (masa_prochu<=0 ):
    masa_prochu = float(input("Podaj masę prochu (liczba w gramach): "))



"długość lufy"

dlugosc_lufy=int(input("\nPodaj długość lufy (musi być conajmniej pięciokrotnie większa od długości pocisku: "))
while (dlugosc_lufy<dlugosc_pocisku*5 ):
    dlugosc_lufy = int(input("Podaj długość lufy (musi być conajmniej pięciokrotnie większa od długości pocisku: "))

sym=symulacja(pocisk_typ[a], luska_material[b], splonka_typ[c], kaliber_mm[d], pocisk_masa, dlugosc_pocisku, dlugosc_luski,  masa_prochu, dlugosc_lufy)
sym.dlugosc_naboju()
print(sym)
sym.predkosc_wylotowa()
sym.niezawodnosc()
