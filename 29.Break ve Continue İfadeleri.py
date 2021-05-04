i = 0
while(i < 10):
    print("i =",i)
    i += 1

i = 0
while(i < 10):
    if(i == 5):
        break
    print("i =",i)
    i += 1

liste = [1,2,3,4,5]
for i in liste:
    if i == 3:
        break
    print("i :",i)

"""while True:
    isim = input("İsim girin(Çıkmak için 'q'ya basın):")
    if(isim == "q"):
        print("Programdan çıkılıyor...")
        break
    print("İsminiz: ",isim)"""

liste = list(range(11))
print(liste)

liste = list(range(11))
for i in liste:
    print("i: ",i)

liste = list(range(11))
for i in liste:
    if(i == 3 or i == 5):
        continue
    print("i: ",i)

i = 0
while(i < 10):
    if(i == 2):
        i += 1
        continue
    print(i)
    i += 1

