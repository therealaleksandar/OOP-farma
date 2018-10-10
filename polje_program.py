import random
from paradajiz_klasa import *
from zito_klasa import *
from ovca_klasa import *
from krava_klasa import *

class Polje():
    def __init__(self,max_zivotinja,max_useva):
        self._usevi=[]
        self._zivotinje=[]
        self._max_zivotinja=max_zivotinja
        self._max_useva=max_useva
    def dodaj_usev(self,usev):
        if len(self._usevi)<self._max_useva:
            self._usevi.append(usev)
            return True
        else:
            return False
    def dodaj_zivotinju(self,zivotinja):
        if len(self._zivotinje)<self._max_zivotinja:
            self._zivotinje.append(zivotinja)
            return True
        else:
            return False

    def pozanji_usev(self,pozicija):
        self._usevi.pop(pozicija)

    def zakolji_zivotinju(self,pozicija):
        self._zivotinje.pop(pozicija)
    
    def izvesti_sadrzaj(self):
        usev_izvestaj=[]
        zivotinja_izvestaj=[]
        for usev in self._usevi:
            usev_izvestaj.append(usev.izvestaj())
        for zivotinja in self._zivotinje:
            zivotinja_izvestaj.append(zivotinja.izvestaj())
        return {"Usevi":usev_izvestaj,"Zivotinje":zivotinja_izvestaj}
    
    def izvesti_potrebe(self):
        hrana=0
        svetlost=0
        voda=0
        for usev in self._usevi:
            potrebe=usev.potrebe()
            if potrebe["potrebna svetlost"]>svetlost:
                svetlost=potrebe["potrebna svetlost"]
            if potrebe["potrebna voda"]>voda:
                voda=potrebe["potrebna voda"]
        for zivotinja in self._zivotinje:
            potrebe=zivotinja.potrebe()
            hrana+=potrebe["Potrebna hrana"]
        return {"hrana":hrana,"svetlost":svetlost,"voda":voda}

    def uzgajaj(self, svetlost, hrana, voda):
        if len(self._usevi)>0:
            for usev in self._usevi:
                usev.rasti(svetlost,voda)
        if len(self._zivotinje)>0:
            hrana_potrebna=0
            for zivotinja in self._zivotinje:
                potrebe=zivotinja.potrebe()
                hrana_potrebna+=potrebe["Potrebna hrana"]
            if hrana>hrana_potrebna:
                dodatna_hrana=hrana-hrana_potrebna
                hrana=hrana_potrebna
            else:
                dodatna_hrana=0
        for zivotinja in self._zivotinje:
            potrebe=zivotinja.potrebe()
            if hrana>=potrebe["Potrebna hrana"]:
                hrana-=potrebe["Potrebna hrana"]
                hrani=potrebe["Potrebna hrana"]
                if dodatna_hrana>0:
                    dodatna_hrana-=1
                    hrani+=1
                zivotinja.raste(hrani,voda)

def auto_uzgajanje(polje,dani):
    for dan in range(dani):
        svetlost=random.randint(1,10)
        voda=random.randint(1,10)
        hrana=random.randint(1,100)
        polje.uzgajaj(svetlost,hrana,voda)

def rucno_uzgajanje(polje):
    validno=False
    while not validno:
        try:
            svetlost=int(input("Unesite svetlost (1-10): "))
            if 1<=svetlost<=10:
                validno=True
            else:
                print("Unesite validnu vrednost od 1 do 10: ")
        except ValueError:
            print("Unesite validnu vrednost od 1 do 10: ")
    validno=False
    while not validno:
        try:
            voda=int(input("Unesite vodu (1-10): "))
            if 1<=voda<=10:
                validno=True
            else:
                print("Unesite validnu vrednost od 1 do 10: ")
        except ValueError:
            print("Unesite validnu vrednost od 1 do 10: ")
    validno=False
    while not validno:
        try:
            hrana=int(input("Unesite hranu (1-100): "))
            if 1<=hrana<=100:
                validno=True
            else:
                print("Unesite validnu vrednost od 1 do 10: ")
        except ValueError:
            print("Unesite validnu vrednost od 1 do 10: ")
    polje.uzgajaj(svetlost,hrana,voda)
def prikazi_useve(lista_useva):
    print()
    print ("Sledeci usevi su u listi useva")
    pos=1
    for usev1 in lista_useva:
        print("{0:>2}.{1}".format(pos,usev1.izvestaj()))
        pos+=1
def prikazi_zivotinje(lista_zivotinja):
    print()
    print("Sledece zivotinje su u listi")
    pos=1
    for zivotinja in lista_zivotinja:
        print("{0:>2}.{1}".format(pos,zivotinja.izvestaj()))
        pos+=1

def izaberi_usev(duzina_useva):
    validno=False
    while not validno:
        izabrano=int(input("Izaberite usev: "))
        if izabrano in range(1,duzina_useva+1):
            validno=True
        else:
            print("Odaberite validnu opciju")
    return izabrano-1

def izaberi_zivotinju(duzina_zivotinja):
    validno=False
    while not validno:
        izabrano=int(input("Izaberite zivotinju: "))
        if izabrano in range(1,duzina_zivotinja+1):
            validno=True
        else:
            print("Odaberite validnu opciju")
    return izabrano-1
def pozanji_usev_sa_polja(polje):
    if len(polje._usevi)>0:
        prikazi_useve(polje._usevi)
        izabrani_usev_broj=izaberi_usev(len(polje._usevi))
        izabrani_usev=polje._usevi[izabrani_usev_broj]
        polje.pozanji_usev(izabrani_usev_broj)
        return izabrani_usev._tip

def zakolji_zivotinju_sa_polja(polje):
    if len(polje._zivotinje)>0:
        prikazi_zivotinje(polje._zivotinje)
        izabrana_zivotinja_broj=izaberi_zivotinju(len(polje._zivotinje))
        izabrana_zivotinja=polje._zivotinje[izabrana_zivotinja_broj]
        polje.zakolji_zivotinju(izabrana_zivotinja_broj)
        return izabrana_zivotinja._ime


def prikazi_usev_meni():
    print()
    print("Odaberite koju vrstu useva zelite da uzgajate:")
    print()
    print("1. Paradajiz")
    print("2. Zito")
    print()
    print("0. Ne zelim da uzgajam usev - vrati me u prethodni meni")
    print()
    print("Molimo vas da odaberete jednu od ponudjenih opcija")

def prikazi_zivotinje_meni():
    print()
    print("Odaberite koju vrstu zivotinje zelite da uzgajate:")
    print()
    print("1. Ovca")
    print("2. Krava")
    print()
    print("0. Ne zelim da uzgajam zivotinje - vrati me u prethodni meni")
    print()
    print("Molimo vas da odaberete jednu od ponudjenih opcija")

def prikazi_glavni_meni():
    print('---------------------------------------------------')
    print("1. Dodaj usev")
    print("2. Ukloni usev")
    print()
    print("3. Dodaj zivotinju")
    print("4. Ukloni zivotinju")
    print()
    print("5. Uzgajaj polje rucno 1 dan")
    print("6. Uzgajaj polje automatski 30 dana")
    print()
    print("7. Prikazi status polja")
    print()
    print("0. Nazad")
    print()
    print("Molimo vas da odaberete jednu od ponudjenih opcija")

def dobij_izbor_menija(manje,vece):
    validno=False
    while not validno:
        try:
            izbor=int(input("Vas izbor je: "))
            if manje<=izbor<=vece:
                validno=True
            else:
                print("Izbor nije validan - probajte ponovo")
        except ValueError:
            print("Izbor nije validan - probajte ponovo")
    return izbor

def dodaj_usev_u_polje(polje):
    prikazi_usev_meni()
    izbor=dobij_izbor_menija(0,2)
    if izbor==1:
        if polje.dodaj_usev(Paradajiz()):
            print()
            print("Usev zasadjen")
            print()
        else:
            print()
            print("Polje je puno - usev nije dodat")
            print()
    elif izbor==2:
        if polje.dodaj_usev(Zito()):
            print()
            print("Usev zasadjen")
            print()
        else:
            print()
            print("Polje je puno - usev nije dodat")
            print()
def dodaj_zivotinju_u_polje(polje):
    prikazi_zivotinje_meni()
    izbor=dobij_izbor_menija(0,2)
    if izbor in (1,2):
        ime=input("Molimo vas da upisete ime zivotinje: ")
        if izbor==1:
            if polje.dodaj_zivotinju(Ovca(ime)):
                print()
                print("Zivotinja dodata")
                print()
            else:
                print()
                print("Polje je puno - zivotinja nije dodata")
                print()
        elif izbor==2:
            if polje.dodaj_zivotinju(Krava(ime)):
                print()
                print("Zivotinja dodata")
                print()
            else:
                print()
                print("Polje je puno - zivotinja nije dodata")
                print()   

def upravljaj_poljem(polje):
    print()
    print("Ovo je program za upravljenje poljem")
    print()
    exit=False
    while not exit:
        prikazi_glavni_meni()
        izbor=dobij_izbor_menija(0,7)
        print()
        print("\n"*100)
        if izbor==1:
            dodaj_usev_u_polje(polje)
        elif izbor==2:
            uklonjen_usev=pozanji_usev_sa_polja(polje)
            print("Uklonili ste usev: {0}".format(uklonjen_usev))
        elif izbor==3:
            dodaj_zivotinju_u_polje(polje)
        elif izbor==4:
            zaklana_zivotinja=zakolji_zivotinju_sa_polja(polje)
            print("Uklonili ste zivotinju: {0}".format(zaklana_zivotinja))
        elif izbor==5:
            rucno_uzgajanje(polje)
        elif izbor==6:
            auto_uzgajanje(polje,30)
        elif izbor==7:
            for k,v in polje.izvesti_sadrzaj().items():
                print(k,v)
                print()
            #print(polje.izvesti_sadrzaj())
            print()
        elif izbor==0:
            exit=True
    
def main():
    novo_polje=Polje(5,2)
    upravljaj_poljem(novo_polje)
    # print(novo_polje._usevi)
    # print(novo_polje._zivotinje)
    # print(novo_polje._max_useva)
    # print(novo_polje._max_zivotinja)
    # novo_polje.dodaj_usev(Zito())
    # novo_polje.dodaj_usev(Paradajiz())
    # novo_polje.dodaj_zivotinju(Krava("Milka"))
    # novo_polje.dodaj_zivotinju(Ovca("Simka"))
    #rucno_uzgajanje(novo_polje)
    #izvestaj=novo_polje.izvesti_sadrzaj()
    #print(izvestaj["usevi"])
    #print(izvestaj["zivotinje"])
    #potrebe = novo_polje.izvesti_potrebe()
    #print(potrebe)
    #print()
    # print(novo_polje.izvesti_sadrzaj())
    # auto_uzgajanje(novo_polje,30)
    # print(novo_polje.izvesti_sadrzaj())
    #novo_polje.uzgajaj(9,19,7)
    #print()
    #print(novo_polje.izvesti_sadrzaj())
    # prikazi_useve(novo_polje._usevi)
    # prikazi_zivotinje(novo_polje._zivotinje)
    # pozanji_usev_sa_polja(novo_polje)
    # prikazi_useve(novo_polje._usevi)
    # zakolji_zivotinju_sa_polja(novo_polje)
    # prikazi_zivotinje(novo_polje._zivotinje)
    # print(novo_polje._usevi)
    # print(novo_polje._zivotinje)
    # novo_polje.pozanji_usev(0)
    # novo_polje.zakolji_zivotinju(0)
    # print(novo_polje._usevi)
    # print(novo_polje._zivotinje)
if __name__=="__main__":
    main()
