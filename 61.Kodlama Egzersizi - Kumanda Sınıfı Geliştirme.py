import random
import time
class kumanda():
    def __init__(self,tvDurum = "Kapalı",tvSes = 0,kanalListesi = ["Trt"],kanal = "Trt"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal
    def tvAc(self):
        if(self.tvDurum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tvDurum = "Açık"
    def tvKapat(self):
        if(self.tvDurum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tvDurum = "Kapalı"
    def sesAyarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi artır: '>'\nÇıkış: çıkış")
            if(cevap == "<"):
                if(self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses:",self.tvSes)
            elif(cevap == ">"):
                if(self.tvSes != 32):
                    self.tvSes += 1
                    print("Ses:",self.tvSes)
            else:
                print("Ses güncellendi:",self.tvSes)
                break
    def kanalEkle(self,kanalIsmi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanalListesi.append(kanalIsmi)
        print("Kanal eklendi.")
    def rastgeleKanal(self,):
        rastgele = random.randint(0,len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)

kumanda1 = kumanda()

print("""
Televizyon uygulaması
1.Tv aç
2.Tv kapat
3.Ses ayarları
4.Kanal ekle
5.Kanal sayısını öğrenme
6.Rastgele kanala geçme
7.Televizyon bilgileri
Çıkmak için 'q'ya basın.
""")

while True:
    işlem = input("İşlemi seçin:")
    if(işlem == "q"):
        print("Program sonlandırılıyor...")
        break
    elif(işlem == "1"):
        kumanda1.tvAc()
    elif(işlem == "2"):
        kumanda1.tvKapat()
    elif(işlem == "3"):
        kumanda1.sesAyarları()
    elif(işlem == "4"):
        kanalIsimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanalListesi = kanalIsimleri.split(",")
        for eklenecekler in kanalListesi:
            kumanda1.kanalEkle(eklenecekler)
    elif(işlem == "5"):
        print("Kanal sayısı:",len(kumanda1))
    elif(işlem == "6"):
        kumanda1.rastgeleKanal()
    elif(işlem == "7"):
        print(kumanda1)
    else:
        print("Geçersiz işlem...")


