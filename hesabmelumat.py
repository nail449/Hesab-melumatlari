class account:
    def __init__(self,ad,soyad,telefonnomresi,balans):
        self.ad = ad
        self.soyad = soyad
        self.telefonnomresi = telefonnomresi
        self.balans = balans
    def hesabMelumatlari(self):
        print("Ad:", self.ad)
        print("Soyad:",self.soyad)
        print("Telefon nomresi:",self.telefonnomresi)
        print("Kartin balansi:",self.balans)

    def kartdanpulcek(self,miqdar):
        if (self.balans - miqdar < 0):
            print("Balansda kifayet qeder pul yoxdur...")
        else:
            self.balans -= miqdar
            print("yeni balans:",self.balans)
    def pulkocurt(self,miqdar):
        self.balans += miqdar
        print("Yeni balans:",self.balans)


nail = account("Nail", "Rzayev", "+994553412890","1000")

nail.hesabMelumatlari()