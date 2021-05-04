print(5 in [1,2,3,4])
print(3 in [1,2,3,4])

print("P" in "Python")
print("S" in "Python")

print(4 in (1,2,3))
print(2 in (1,2,3))

liste = [1,2,3,4,5,6,7]
for eleman in liste:
    print(eleman)

liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam = toplam + eleman
    print("Eleman = {} , Toplam = {}".format(eleman,toplam))
print("Genel toplam = {}".format(toplam))

liste = [1,2,3,4,34,54,63,78]
for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)

s = "Python"
for i in s:
    print(i * 2)

demet = (1,2,3,4,5)
for a in demet:
    print(a)

liste = [(1,2),(3,4),(5,6),(7,8)]
for eleman in liste:
    print(eleman)

liste = [(1,2),(3,4),(5,6),(7,8)]
for (i,j) in liste:
    print("i = {} , j = {}".format(i,j))

liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print("{} * {} * {} = {}".format(i,j,k,i*j*k))

sözlük = {"Bir":1,"İki":2,"Üç":3,"Dört":4}
for eleman in sözlük:
    print(eleman)
for eleman in sözlük.values():
    print(eleman)
for i,j in sözlük.items():
    print("Anahtar = {} , Değer = {}".format(i,j))