import math
print("""
**********
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Faktoriyel
**********""")
işlem = int(input("İşlemi seçiniz(1,2,3,4,5):"))
x = int(input("İlk sayıyı giriniz:"))
y = int(input("İkinci sayıyı giriniz:"))

if(işlem == 1):
    print("{} + {} = {}".format(x,y,x+y))
elif(işlem == 2):
    print("{} - {} = {}".format(x,y,x-y))
elif(işlem == 3):
    print("{} * {} = {}".format(x,y,x*y))
elif(işlem == 4):
    print("{} / {} = {}".format(x,y,x/y))
elif(işlem == 5):
    print("{}! = {}".format(x,math.factorial(x)))
else:
    print("Geçersiz işlem girdiniz!, Lütfen 1-2-3-4-5 giriniz.")

