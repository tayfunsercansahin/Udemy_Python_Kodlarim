def selamla(isim):
    print("Selam",isim)
selamla("Tayfun")

def selamla(isim = "İsimsiz"):
    print("Selam",isim)
selamla()

def bilgileriGoster(ad,soyad,numara):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgileriGoster("Tayfun Sercan","Şahin","160251044")

def bilgileriGoster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara = "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgileriGoster()
bilgileriGoster("Tayfun Sercan","Şahin")
bilgileriGoster(numara = "160251044")

print("Tayfun","Sercan","Şahin",sep = "/")

def toplama(*a):
    print(a)
toplama(1,2,3)

def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)
toplama(1,2,3)
toplama(3,4,5,6,7,8,9,10,11)
