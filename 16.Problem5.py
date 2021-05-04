ilkSayi = int(input("İlk sayıyı girin:"))
ikinciSayi = int(input("İkinci sayıyı girin:"))

print("İlk sayı: {} , İkinci sayı: {}\n".format(ilkSayi,ikinciSayi))

(ilkSayi,ikinciSayi) = (ikinciSayi,ilkSayi)
print("Sayılar arasında değiştiriliyor...")

print("İlk sayı: {} , İkinci sayı: {}\n".format(ilkSayi,ikinciSayi))
