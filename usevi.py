from zito_klasa import *
from paradajiz_klasa import *

def prikazi_meni2():
    print()
    print("Molimo Vas da izaberete koji usev zelite da uzgajate")
    print()
    print("1. Paradajiz")
    print("2. Zito")
    print()
    print('Molimo vas da izaberete opciju iz menija')

def izabrana_opcija():
    Validno=False
    while not Validno:
        try:
            izbor=int(input("Ukucajte vas odabir: "))
            if izbor in(1,2):
                Validno=True
            else:
                print("Molimo da unesete validnu opciju.")
        except ValueError:
            print("Molimo da unesete validnu opciju")
    return izbor

def kreirajte_usev():
    prikazi_meni2()
    izbor=izabrana_opcija()
    if izbor==1:
        novi_usev=Paradajiz()
    elif izbor==2:
        novi_usev=Zito()
    return novi_usev

def main():
    novi_usev=kreirajte_usev()
    upravljaj_usevom(novi_usev)

if __name__=="__main__":
    main()