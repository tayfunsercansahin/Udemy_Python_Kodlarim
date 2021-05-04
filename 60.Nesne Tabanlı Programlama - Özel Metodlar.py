class kitap():
    def __init__(self,isim,yazar,sayfaSayısı,tür):
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayısı = sayfaSayısı
        self.tür = tür
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}\n".format(self.isim,self.yazar,self.sayfaSayısı,self.tür)
    def __len__(self):
        return self.sayfaSayısı
    def __del__(self):
        print("kitap1 objesi siliniyor...")

kitap1 = kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap1)
print(len(kitap1))
del kitap1