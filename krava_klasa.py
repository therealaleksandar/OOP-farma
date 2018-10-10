from zivotinje_klasa import *
class Krava(Zivotinje):
    def __init__(self,ime):
        super().__init__(3,6,5)
        self._tip="Krava"
        self._ime=ime
    def raste(self,hrana,voda):
        if hrana>=self._potrebna_hrana and voda>=self._potrebna_voda:
            if self._status=="Mladunce" and hrana>self._potrebna_hrana:
                self._tezina+=self._brzina_rasta*2
            elif self._status=="Izrasta" and hrana>self._potrebna_hrana:
                self._tezina+=self._brzina_rasta*1.5
            elif self._status=="Mlado" and hrana>self._potrebna_hrana:
                self._tezina+=self._brzina_rasta*1.25
            else:
                self._tezina+=self._brzina_rasta
        self._dani_rasta+=1
        self._azuriraj_status()

def main():
    krava1=Krava("Milka")
    print(krava1.izvestaj())
    print(krava1.potrebe())
    krava1.raste(7,5)
    print(krava1.izvestaj())
    auto_rast(krava1,30)
    print(krava1.izvestaj())
    rucni_rast(krava1)
    print(krava1.izvestaj())
if __name__=="__main__":
    main()