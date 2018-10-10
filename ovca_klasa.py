from zivotinje_klasa import *
class Ovca(Zivotinje):
    def __init__(self,ime):
        super().__init__(2,4,3)
        self._tip="Ovca"
        self._ime=ime

    def raste(self,hrana,voda):
        if hrana>=self._potrebna_hrana and voda>=self._potrebna_voda:
            if self._status=="Izrasta" and hrana>self._potrebna_hrana:
                self._tezina+=self._brzina_rasta*1.5
            elif self._status=="Mladunce" and hrana>self._potrebna_hrana:
                self._tezina+=self._brzina_rasta*1.25
            else:   
                self._tezina+=self._brzina_rasta
        self._dani_rasta+=1
        self._azuriraj_status()

def main():
    ovca1=Ovca("Lenka")
    print(ovca1.potrebe())
    ovca1.raste(3,3)
    print(ovca1.izvestaj())
if __name__=="__main__":
    main()