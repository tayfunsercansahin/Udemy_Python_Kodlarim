liste1 = [1,2,3,4,5]
liste2 = [i * 2 for i in liste1]
print(liste2)

def ikiyleçarp(x):
    return x*2
print(ikiyleçarp(3))

ikiyleçarp = lambda x : x*2
print(ikiyleçarp(4))

karesinial = lambda y : y**2
print(karesinial(5))

def toplama(x,y,z):
    return x+y+z
print(toplama(10,11,12))

toplama = lambda x,y,z : x+y+z
print(toplama(5,6,7))

def terscevir(s):
    return s[::-1]
print(terscevir("Python Programlama"))

ters = lambda s : s[::-1]
print(ters("Tayfun Sercan"))

def çifttek(sayı):
    return sayı % 2 == 0
print(çifttek(14))
print(çifttek(15))