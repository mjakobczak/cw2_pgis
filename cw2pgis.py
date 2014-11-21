##Zadanie1

from collections import defaultdict
import string
import itertools
from math import sqrt
f=open("text.txt","r")
##print(f.read())

d = defaultdict(int)
licznik=0
slownik={}

slowa=f.read().split()
for word in slowa:
    licznik=licznik+1
    d[word] += 1
    ##print word
    if word in slownik.keys():
        slownik[word] = slownik[word]+1
    else:
        slownik[word]=1

##print slownik
print "Zadanie 1"
print"----------"
items= sorted(slownik.items(), key=lambda krotka: krotka[1], reverse = True) 
licznik=0
f=open("text2.txt","r+")
for item in items:
    licznik=licznik+1
    if licznik<=10:
        print item
        f.write(str(item)+"\n")

##Zadanie2
print""
print "Zadanie 2"
print"----------"
menu={}
with open("menu.txt") as menu_f:
    content = menu_f.readlines()
##print content
for linia in content:
    nazwa=linia.split(":")[0]
    cena=float(linia.split(":")[1])
##  print nazwa
##  print cena
    menu[nazwa]= cena
##print menu

def zamowienie(zamowienie):
    cena=0
    for i in zamowienie:
        if i in menu:
            cena+=menu[i]
    return cena*1.1
print zamowienie(["Zupa pomidorowa", "Pierogi ruskie", "Kompot"]) 

##Zadanie3
print""
print "Zadanie 3"
print"----------"
 
class LiczbaZespolona:
    r=0
    u=0
    def __init__(self,r,u):
        self.r = r
        self.u = u
       
    def getR(self):
        return self.r
 
    def setR(self, r):
        self.r = r
       
    def getU(self):
        return self.u
 
    def setU(self, u):
        self.u = u
 
    def dodaj(self,liczba2):
        r = self.r + liczba2.r
        u = self.u + liczba2.u
        wynik = LiczbaZespolona(r,u)
        return wynik
    
    def odejmij (self,liczba2):
        r = self.r - liczba2.r
        u = self.u - liczba2.u
        wynik = LiczbaZespolona(r,u)
        return wynik
    
    def modulo (self):
        r = self.r 
        u = self.u 
        wynik= sqrt(r*r + u*u)
        print wynik
    
    def wyswietl(self):
        print str(self.r)+ "+" + str(self.u)+"i"
 
   
       
   
liczba1=LiczbaZespolona(6,3)
liczba2=LiczbaZespolona(5,2)
print "liczba1"
liczba1.wyswietl()
print "liczba2"
liczba2.wyswietl()
print "Wynik dodawania"
liczba1.dodaj(liczba2).wyswietl()
print "Wynik odejmowania"
liczba1.odejmij(liczba2).wyswietl()
print "Wartoœæ bezwzgledna liczby2"
liczba2.modulo()

##Zadanie4
print""
print "Zadanie 4"
print"----------"

class Maszyna:
    moc=0
    def __init__(self,moc):
        self.moc = moc
       
    def getMoc(self):
        return self.moc
 
    def setMoc(self, moc):
        self.moc = moc

    def wyswietl(self):
        print "Maszyna o mocy: " + str(self.moc)
        

class Pojazd:
    iloscKol=0

    def __init__(self, iloscKol):
        self.iloscKol = iloscKol
       
    def getIloscKol(self):
        return self.iloscKol
 
    def setIloscKol(self, iloscKol):
        self.iloscKol = iloscKol

    def wyswietl(self):
        print "Pojazd z iloscia kol: " + str(self.iloscKol)
         
class Komputer(Maszyna):
    pass
    
class Samochod(Maszyna, Pojazd):

    def __init__(self, moc, iloscKol):
        self.moc=moc
        self.iloscKol=iloscKol

    def wyswietl(self):
        print "Samochod o mocy: " +str(self.moc)
        print "Samochod z iloscia kol: " + str(self.iloscKol)
    
maszyna1= Maszyna(100)
maszyna1.wyswietl()

pojazd1=Pojazd(4)
pojazd1.wyswietl()

komputer1=Komputer(200)
komputer1.wyswietl()

samochod1=Samochod(300,4)
samochod1.wyswietl()
