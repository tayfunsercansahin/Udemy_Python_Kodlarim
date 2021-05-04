def selamla():
    print("Merhaba...")
    print("Nasılsınız?")
print(type(selamla))
selamla()

def selamla(isim):
    print("İsminiz:",isim)
print(type(selamla))
selamla("Tayfun ")
selamla("Ayşe")

def toplama(a,b,c):
    print("{} + {} + {} = {}".format(a,b,c,a+b+c))
print(type(toplama))
toplama(3,5,7)

def faktoriyel(sayı):
    faktoriyel = 1
    if(sayı == 0 or sayı == 1):
        print("Faktoriyel:",faktoriyel)
    else:
        while(sayı >= 1):
            faktoriyel *= sayı
            sayı -= 1
        print("Faktoriyel:",faktoriyel)

faktoriyel(0)
faktoriyel(1)
faktoriyel(5)
faktoriyel(6)