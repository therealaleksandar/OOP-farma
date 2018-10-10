from polje_program import Polje,upravljaj_poljem
from pojedinacno import upravljaj_farmom

def prikazi_meni():
    print("\nDOBRODOSLI U PROGRAM ZA UPRAVLJANJE FARMOM\n")
    print("Izaberite sekciju: ")
    print()
    print("1. Pojedinacno uzgajanje")
    print("2. Grupno uzgajanje celog polja")
    print()
    print("0. Izlaz")
    print()
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

def glavni():
    izlaz=False
    while not izlaz:
        print("\n"*100)
        prikazi_meni()
        izbor=izabrana_sekcija()
        izlaz=False
        if izbor==1:
            upravljaj_farmom()
        elif izbor==2:
            novo_polje=Polje(5,5)
            upravljaj_poljem(novo_polje)
        elif izbor==0:
            izlaz=True
            print("Drago nam je sto ste koristili nas program.")

def main():
    glavni()
if __name__=="__main__":
    main()
