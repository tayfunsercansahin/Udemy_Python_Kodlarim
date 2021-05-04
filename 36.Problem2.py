sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while(gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam = toplam + (basamak ** basamak_sayisi)
    gecici_sayı = gecici_sayı // 10

if(toplam == sayı):
    print(sayı,"Bir armstrong sayısıdır.")
else:
    print(sayı,"Bir armstrong sayısı değildir.")