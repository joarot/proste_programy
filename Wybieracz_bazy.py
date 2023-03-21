import mysql.connector


# wyświetlenie dostępnych baz
baza= mysql.connector.connect(host="localhost", user="root", passwd="", database="")
kursor= baza.cursor()
kwerenda="SHOW DATABASES"
kursor.execute(kwerenda)
print("Uruchomiłem kwerendę:\n"+kursor.statement)
print("Dostępne bazy danych:")
i=0
tab= []
for rekord in kursor.fetchall():
    s = str(i)
    sl= slice(2,-3)
    text = str(rekord)
    text=text[sl]
    if (i<10):
        print(' '+s,'-',text)
    else:  print(s,'-',text)
    tab += [text]
    i += 1


#wybór bazy danych
print()
wyb = int(input("Wybierz bazę (wpisz numer i zatwierdź przyciskiem enter):"))
while (wyb>len(tab) and wyb<0):
    print("Wystąpił błąd")
    print()
    wyb = int(input("Wybierz bazę (wpisz numer i zatwierdź przyciskiem enter):"))
ba=tab[wyb]


#wczytanie bazy danych i wyświetlenie dostępnych tabel
baza= mysql.connector.connect(host="localhost", user="root", passwd="", database=""+ba)
kursor= baza.cursor()
kwerenda="SHOW TABLES"
kursor.execute(kwerenda)
print("Uruchomiłem kwerendę:\n"+kursor.statement)
print("Dostępne tabele w bazie "+tab[wyb]+":")
i=0
tab= []
for rekord in kursor.fetchall():
    s = str(i)
    sl = slice(2, -3)
    text = str(rekord)
    text = text[sl]
    if (i < 10):
        print(' ' + s, '-', text)
    else:
        print(s, '-', text)
    tab += [text]
    i += 1


#wybór tabeli
print()
wyb = int(input("Wybierz tabelę (wpisz numer i zatwierdź przyciskiem enter):"))
while (wyb>len(tab) & wyb<0):
    print("Wystąpił błąd")
    print()
    wyb = int(input("Wybierz tabelę (wpisz numer i zatwierdź przyciskiem enter):"))

kwerenda="Select * from "+tab[wyb]
kursor.execute(kwerenda)
print("Uruchomiłem kwerendę:\n"+kursor.statement+"\nby uzyskać nazwy pól")
print("Dostępne pola w tabeli "+tab[wyb]+":")
tabela=tab[wyb]
i=0
tab= []
for rekord in kursor.column_names:
    s = str(i)
    if (i < 10):
        print(' ' + s, '-', rekord)
    else:
        print(s, '-', rekord)
    i += 1
    tab += [rekord]
kolumny=tab


#wybór pól do kwerend
print()
wyb = input("Wybierz pola, które mają zostać wyświetlone (wpisz numer, lub *, lub numery oddzielone przecinkiem :")
"nie mam pomysłu jak zrobić by ten while działał"
while ((wyb>len(tab) and wyb<0) or wyb.split(",")>len(tab) or wyb!="*"):
    print("Wystąpił błąd")
    print()
    wyb = input("Wybierz pola, które mają zostać wyświetlone (wpisz numer, lub *, lub numery oddzielone przecinkiem :")

if(wyb=="*"):
    kwerenda="Select * from "+tabela
else:
    i=0
    tab=wyb.split(",")
    for x in tab:
        y=int(x)
        tab[i]=kolumny[y]
        i+=1
    sl = slice(1, -1)
    text = str(tab)
    text = text[sl]
    text = text.replace("'","")
    kwerenda = "Select "+text+" from "+tabela


#wybranie pola porównującego
print()
wyb = (input("Wybierz pole, które będzie kryterium wyszukiwania (wpisz numer i zatwierdź przyciskiem enter, lub jeśli określenie kryterium jest zbędne nic nie wpisuj i wciśnij enter):"))
''' nie mam pomysłu jak zrobić by ten while działał
while (wyb!=None or int(wyb)>len(kolumny) and int(wyb)<0 ):
    print("Wystąpił błąd")
    print()
    wyb = input("Wybierz pole, które będzie kryterium wyszukiwania (wpisz numer i zatwierdź przyciskiem enter, lub jeśli określenie kryterium jest zbędne nic nie wpisuj i wciśnij enter):")'''
baza = mysql.connector.connect(host="localhost", user="root", passwd="", database="" + ba)
kursor = baza.cursor()


#jeśli nie ma pola porównującego następuje wypisanie kwerendy
if(wyb==""):
    kursor.execute(kwerenda)
    print("Uruchomiłem kwerendę:\n" + kursor.statement)
    print("Wyniki kwerendy "+kwerenda)
    print(tab)
    for rekord in kursor:
        print(rekord)
    exit(0)
else:
    kwerenda += " where "+kolumny[int(wyb)]


#wybór operatora porównania
print()
wyb = str(input("Wybierz operator porównania (czyli >, <, <>, >=, <=, LIKE) i zatwierdź enterem:"))
while (wyb!=">" and wyb !="<" and wyb !="<>" and wyb !=">=" and wyb !="<=" and wyb !="LIKE"):
    print("Wystąpił błąd")
    print()
    wyb = str(input("Wybierz operator porównania (czyli >, <, <>, >=, <=, LIKE) i zatwierdź enterem:"))
kwerenda += " "+wyb
oper=wyb


#wybór wartości operatora porównania
wyb = input("Wybierz wartość operatora porównania i zatwierdź enterem:")
if(oper=="LIKE"):
    kwerenda += " '"+wyb+"'"
    kursor.execute(kwerenda)
    print("Uruchomiłem kwerendę:\n" + kursor.statement)
    print("Wyniki kwerendy " + kwerenda)
    print(tab)
    for rekord in kursor:
        print(rekord)
    exit(0)
else:
    kwerenda += wyb
    kursor.execute(kwerenda)
    print("Uruchomiłem kwerendę:\n" + kursor.statement)
    print("Wyniki kwerendy " + kwerenda)
    print(tab)
    for rekord in kursor:
        print(rekord)