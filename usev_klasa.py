import random

class Usev:
        """Genericki usev za jelo"""
        #constructor
        def __init__(self,brzina_rasta,potrebna_svetlost,potrebna_voda):
            #postavljanje atributa
            self._rast=0
            self._dani_rasta=0
            self._brzina_rasta=brzina_rasta
            self._potrebna_svetlost=potrebna_svetlost
            self._potrebna_voda=potrebna_voda
            self._status= "Seme"
            self._tip="Genericko"
        #unserscore _ znaci da su atributi privatni i moze im se pristupiti samo u klasi

        def potrebe (self):
            return {'potrebna svetlost':self._potrebna_svetlost,'potrebna voda':self._potrebna_voda}
        def izvestaj (self):
            return {'tip':self._tip,'status':self._status,'rast':self._rast,'dani rasta':self._dani_rasta}
        def _azuriraj_status (self):
            if self._rast>15:
                self._status="Staro"
            elif self._rast>10:
                self._status="Zrelo"
            elif self._rast>5:
                self._status='Mlado'
            elif self._rast>0:
                self._status="Izrasta"
            else:
                self._status="Seme"
        def rasti (self,svetlost,voda):
            if svetlost>=self._potrebna_svetlost and voda>=self._potrebna_voda:
                self._rast+=self._brzina_rasta
            self._dani_rasta+=1
            self._azuriraj_status()
def auto_rast(usev,dani):
    for dan in range (dani):
        svetlost=random.randint(1,10)
        voda=random.randint(1,10)
        usev.rasti(svetlost,voda)

def rucni_rast(usev):
    valid =False
    while not valid:
        try:
            svetlost=int(input("Unesite vrednost svetlosti (1-10): "))
            if 1<=svetlost<=10:
                valid=True
            else:
                print("Uneli ste pogresnu vredno. Molimo Vas da unesete vrednost izmedju 1-10:")
        except ValueError:
            print("Uneli ste pogresnu vredno. Molimo Vas da unesete vrednost izmedju 1-10:")
    valid=False
    while not valid:
        try:
            voda=int(input("Unesite vrednost vode (1-10):"))
            if 1<=voda<=10:
                valid=True
            else:
                print("Uneli ste pogresnu vredno. Molimo Vas da unesete vrednost izmedju 1-10:")
        except ValueError:
            print("Uneli ste pogresnu vredno. Molimo Vas da unesete vrednost izmedju 1-10:")
    usev.rasti(svetlost,voda)

def prikazi_meni():
    print("1. Uzgajaj rucno 1 dan")
    print("2. Uzgajaj automatski 30 dana")
    print("3. Prikazi izvestaj")
    print("0. Zatvori program")
    print ()
    print ("Molimo vas izaberite opciju")

def dobij_izbor_menija():
    valid =False
    while not valid:
        try:
            izbor=int(input("Selektovana opcija: "))
            if 0<=izbor<4:
                valid=True
            else:
                print("Molimo unesite ponudjenu opciju")
        except ValueError:
            print("Molimo unesite ponudjenu opciju")
        return izbor

def upravljaj_usevom (usev):
    print ("Ovo je program za obradu useva")
    print ()
    nijeizlaz=True
    while nijeizlaz:
        prikazi_meni()
        opcija=dobij_izbor_menija()
        print()
        if opcija==1:
            rucni_rast(usev)
            print()
        elif opcija==2:
            auto_rast(usev,30)
            print()
        elif opcija==3:
            print(usev.izvestaj())
            print()
        elif opcija==0:
            nijeizlaz=False
            print()
    print("Hvala Vam sto ste koristili program.")

def main():
    #definisan je objekat novi usev
    novi_usev=Usev(1,4,3)
    upravljaj_usevom(novi_usev)
    # print(novi_usev.potrebe())
    # print(novi_usev.izvestaj())
    # novi_usev.rasti(5,4)
    # rucni_rast(novi_usev)
    # print(novi_usev.izvestaj())

if __name__=='__main__':
    main()
