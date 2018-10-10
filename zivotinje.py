from krava_klasa import *
from ovca_klasa import *

def prikazi_meni():
    print()
    print("Molimo da izaberete zivotinju koju zelite uzgajati")
    print()
    print("1. Ovca")
    print("2. Krava")
    print()
    print("Molimo izaberite ponudjenu opciju")

def izabrana_opcija():
    validno=False
    while not validno:
        try:
            izbor=int(input("Selektovana opcija: "))
            if izbor in(1,2):
                validno=True
            else:
                print("Opcija nije validna. Probajte ponovo: ")
        except ValueError:
            print("Opcija nije validna. Probajte ponovo: ")
    return izbor

def kreirajte_zivotinju():
    prikazi_meni()
    izbor=izabrana_opcija()
    if izbor==1:
        ime=input('Unesite ime ovce: ')
        nova_zivotinja=Ovca(ime)
    elif izbor==2:
        ime=input('Unesite ime krave: ')
        nova_zivotinja=Krava(ime)
    return nova_zivotinja


def main():
    nova_zivotinja=kreirajte_zivotinju()
    upravljaj_zivotinjama(nova_zivotinja)

if __name__=="__main__":
    main()
