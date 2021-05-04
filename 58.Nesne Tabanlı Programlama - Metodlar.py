class yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgileriGöster(self):
        print("""
        Yazılımcının özellikleri
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def zamYap(self,zamMiktarı):
        print("Zam yapılıyor...")
        self.maaş += zamMiktarı

    def dilEkle(self,yeniDil):
        print("Dil ekleniyor...")
        self.diller.append(yeniDil)

yazılımcı1 = yazılımcı("Mustafa","Coşkun",12345,3000,["Python","Java","C"])
yazılımcı2 = yazılımcı("Tayfun","Şahin",6789,3800,["Matlab","C++"])
yazılımcı1.bilgileriGöster()
yazılımcı2.bilgileriGöster()

yazılımcı1.dilEkle("Golang")
yazılımcı1.bilgileriGöster()
yazılımcı2.zamYap(500)
yazılımcı2.bilgileriGöster()
