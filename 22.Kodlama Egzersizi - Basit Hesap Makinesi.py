print("""****************************
Hesap makinesi programı
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
****************************""")

a = int(input("Birinci sayıyı girin:"))
b = int(input("İkinci sayıyı girin:"))

işlem = input("İşlemi girin(1,2,3,4):")

if işlem == "1":
    print("{} + {} = {}".format(a,b,a+b))
elif işlem == "2":
    print("{} - {} = {}".format(a,b,a-b))
elif işlem == "3":
    print("{} * {} = {}".format(a,b,a*b))
elif işlem == "4":
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Geçersiz işlem girdiniz. Lütfen 1,2,3,4'den birini giriniz.")


