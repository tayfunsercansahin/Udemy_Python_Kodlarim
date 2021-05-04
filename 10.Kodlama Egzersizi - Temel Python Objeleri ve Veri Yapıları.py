print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad, soyad, takım]
print("Bilgiler kaydediliyor...")

print("Oyuncu Adı: {}\nOyuncu Soyadı: {}\nOyuncu Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi...")