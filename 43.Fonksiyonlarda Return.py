def toplama(a,b,c):
    return a+b+c
def ikiyleçarp(d):
    return d*2
toplam = toplama(3,4,5)
print(toplam)
print(ikiyleçarp(toplam))

def üçleçarp(a):
    print("1.fonksiyon çalıştı...")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı...")
    return a+2
def dördeböl(a):
    print("3.fonksiyon çalıştı...")
    return a/4
print(dördeböl(ikiyletopla(üçleçarp(5))))




