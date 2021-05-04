import math
dir(math)
help(math)

print(math.factorial(5))
print(math.factorial(6))

print(math.floor(5.6))
print(math.floor(11.9))

print(math.ceil(5.6))
print(math.ceil(11.9))

import math as matematik

print(matematik.factorial(5))
print(matematik.factorial(3))

print(matematik.floor(5.6))
print(matematik.floor(11.9))

print(matematik.ceil(5.6))
print(matematik.ceil(11.9))

from math import*

print(factorial(5))
print(factorial(6))

print(floor(6.4))
print(floor(9.3))

print(ceil(13.3))
print(ceil(7.7))


def factorial(sayı):
    print("Benim fonksiyonum")
    faktoriyel = 1
    if(sayı == 0 or sayı ==1):
        return 1
    else:
        while(sayı >= 1):
            faktoriyel = faktoriyel * sayı
            sayı = sayı - 1
        return faktoriyel

print(factorial(5))