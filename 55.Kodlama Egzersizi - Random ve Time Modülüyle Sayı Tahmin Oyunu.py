import random
import time
print("""
*************************************
1 ile 40 arasındaki sayıyı tahmin et
*************************************""")

rastgeleSayı = random.randint(1,40)
tahminHakkı = 7

while True:
    tahmin = int(input("Tahmininiz:"))
    if(tahmin < rastgeleSayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin.")
        tahminHakkı -= 1
        print("Tahmin hakkınız:",tahminHakkı)
    elif(tahmin > rastgeleSayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin.")
        tahminHakkı -= 1
        print("Tahmin hakkınız:", tahminHakkı)
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tahmin hakkınız:", tahminHakkı)
        print("Tebrikler, sayınız:",rastgeleSayı)
        break

    if(tahminHakkı == 0):
        print("Tahmin hakkınız bitti!")
        print("Sayınız:",rastgeleSayı)
        break