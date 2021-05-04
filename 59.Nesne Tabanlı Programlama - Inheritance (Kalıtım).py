class çalışan():
    def __init__(self,isim,maaş,departman):
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgileriGöster(self):
        print("İsim: {} \nMaaş: {} \nDepartman: {} \n".format(self.isim,self.maaş,self.departman))
    def departmanDeğiştir(self,yeniDepartman):
        self.departman = yeniDepartman

class yönetici(çalışan):
    pass

yönetici1 = yönetici("Mustafa Murat Coşkun",3500,"Bilişim")
yönetici1.bilgileriGöster()

yönetici1.departmanDeğiştir("İnsan kaynakları")
yönetici1.bilgileriGöster()

class yönetici(çalışan):
    def zamYap(self,zamMiktarı):
        self.maaş += zamMiktarı

yönetici2 = yönetici("Serhat Say",3800,"Pazarlama")
yönetici2.bilgileriGöster()

yönetici2.zamYap(500)
yönetici2.bilgileriGöster()
