from zivotinje import *
from usevi import *

def prikazi_meni():
    print("\nIzaberite sekciju: ")
    print()
    print("1. Zivotinje")
    print("2. Usevi")
    print()
    print("0. Nazad\n")
    print("Izaberite nesto od navedenog.")

def izabrana_sekcija():
    validno=False
    while not validno:
        try:
            izbor=int(input("Selektovali ste: "))
            if izbor in(0,1,2):
                validno=True
            else:
                print("Izabrali ste nepostojecu sekciju. Probajte ponovo: ")
        except ValueError:
            print("Izabrali ste nepostojecu sekciju. Probajte ponovo: ")
    return izbor

def upravljaj_farmom():
    while True:
        print("\n"*100)
        prikazi_meni()
        izbor=izabrana_sekcija()
        if izbor==1:
            nova_zivotinja=kreirajte_zivotinju()
            upravljaj_zivotinjama(nova_zivotinja)
        elif izbor==2:
            novi_usev=kreirajte_usev()
            upravljaj_usevom(novi_usev)
        else:
            break

def main():
    upravljaj_farmom()
if __name__=="__main__":
    main()
