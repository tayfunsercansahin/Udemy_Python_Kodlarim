import random
print('Sayı tahmin oyununa hoşgeldiniz..')
hak=int(input('Kaç tahmin hakkınız olsun :'))
puan=100/hak
g=random.random()
sayi=int(g*100)

print("1-100 arasında bir değer giriniz.")
tpuan=0
for a in range(hak) :
    tahmin=int(input(f'{a+1}. tahmininizi giriniz: '))
    if tahmin < sayi:
        tpuan += puan
        if (100-tpuan) != 0:
            print('Yukarı çıkın ')
    elif tahmin> sayi:
        tpuan += puan
        if (100-tpuan) != 0:
            print('Aşağı inin ')
    elif tahmin == sayi :
        print(f'Bildiniz toplam puanınız : {100-tpuan}')
        break
    #if a+1 == hak:
    #    print('hakkınız bitti.')    !! bunu puan olayı olmazsa hakkım bitince yazdırmak için kullanabilirim.

if (100-tpuan) == 0 :
    print (f'Bilemediniz tutulan sayı buydu: {sayi}')