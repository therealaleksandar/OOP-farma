import random
class Zivotinje():
    def __init__(self,brzina_rasta,potrebna_hrana,potrebna_voda):
        self._tezina=0
        self._dani_rasta=0
        self._brzina_rasta=brzina_rasta
        self._potrebna_hrana=potrebna_hrana
        self._potrebna_voda=potrebna_voda
        self._status="Mladunce"
        self._tip="Genericko"
        self._ime="Zivotinja"
    def potrebe(self):
        return {'Potrebna hrana':self._potrebna_hrana,'Potrebna voda':self._potrebna_voda}
    def izvestaj(self):
        return {'Ime':self._ime,'Tezina':self._tezina,'Status':self._status,'Tip':self._tip,'Dani rasta':self._dani_rasta}
    def _azuriraj_status(self):
        if self._tezina>110:
            self._status="Staro"
        elif self._tezina>80:
            self._status="Zrelo"
        elif self._tezina>30:
            self._status="Mlado"
        elif self._tezina>0:
            self._status="Izrasta"
        else:
            self._status="Mladunce"
    
    def raste(self,hrana,voda):
        if hrana>=self._potrebna_hrana and voda>=self._potrebna_voda:
            self._tezina+=self._brzina_rasta
        self._dani_rasta+=1
        self._azuriraj_status()

def auto_rast(zivotinja,dani):
    for dan in range(dani):
        hrana=random.randint(2,20)
        voda=random.randint(1,10)
        zivotinja.raste(hrana,voda)

def rucni_rast(zivotinja):
    validno=False
    while not validno:
        try:
            hrana=int(input("Unesite kolicinu hrane u kilogramima: "))
            if 2<=hrana<=20:
                validno=True
            else:
                print("Uneli ste pogresnu kolicinu hrane. Probajte ponovo")
        except ValueError:
            print("Uneli ste pogresnu kolicinu hrane. Probajte ponovo")
    validno=False
    while not validno:
        try:
            voda=int(input("Unesite potrebnu vodu: "))
            if 1<=voda<=10:
                validno=True
            else:
                print("Uneli ste pogresnu kolicinu hrane. Probajte ponovo")
        except ValueError:
            print("Uneli ste pogresnu kolicinu hrane. Probajte ponovo")
    
    zivotinja.raste(hrana,voda)

def prikazi_meni():
    print("1. Uzgajaj rucno 1 dan")
    print("2. Uzgajaj automatski 30 dana")
    print("3. Prikazi izvestaj")
    print("0. Zatvori program")
    print ()
    print ("Molimo vas izaberite opciju")

def selektovana_opcija():
    validno=False
    while not validno:
        try:
            izbor=int(input("Unesite vasu opciju: "))
            if izbor in(0,1,2,3):
                validno=True
            else:
                print("Izbor nije validan. Pokusajte ponovo")
        except ValueError:
            print("Izbor nije validan. Pokusajte ponovo")
        return izbor

def upravljaj_zivotinjama(zivotinja):
    print ("Ovo je program za uzgoj zivotinja")
    print ()
    izlaz=False
    while not izlaz:
        prikazi_meni()
        izbor=selektovana_opcija()
        print()
        if izbor==1:
            rucni_rast(zivotinja)   
            print()
        elif izbor==2:
            auto_rast(zivotinja,30)
            print()
        elif izbor==3:
            print(zivotinja.izvestaj())
            print()
        elif izbor==0:
            izlaz=True
            print()
    print("Hvala sto ste koristili program.")
   
def main():
    zivotinja1=Zivotinje(2,4,4)
    #upravljaj_zivotinjama(zivotinja1)
    # print(zivotinja1.potrebe())
    # print(zivotinja1.izvestaj())
    # auto_rast(zivotinja1,30)
    # rucni_rast(zivotinja1)
    print(zivotinja1.potrebe["Potrebna hrana"])

if __name__=='__main__':
    main()    
