from usev_klasa import *

class Paradajiz(Usev):
    def __init__(self):
        super().__init__(1,3,5)
        self._tip="Paradajiz"

    def rasti(self,svetlost,voda):
        if svetlost>=self._potrebna_svetlost and voda>=self._potrebna_voda:
            if self._status=="Izrasta" and voda>self._potrebna_voda:
                self._rast+=self._brzina_rasta*1.5
            elif self._status=="Mlado" and voda>self._potrebna_voda:
                self._rast+=self._brzina_rasta*1.25
            else:
                self._rast+=self._brzina_rasta
        self._dani_rasta+=1
        self._azuriraj_status()

def main():
    paradajiz1=Paradajiz()
    print(paradajiz1.izvestaj())
    rucni_rast(paradajiz1)
    print(paradajiz1.izvestaj())
    rucni_rast(paradajiz1)
    print(paradajiz1.izvestaj())

if __name__=='__main__':
    main()