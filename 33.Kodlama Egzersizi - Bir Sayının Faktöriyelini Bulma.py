print("""
****************
Faktöriyel Bulma
****************""")
while True:
    sayı = input("Sayı: ")
    if(sayı == "q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i
        print("{}! = {}".format(sayı,faktoriyel))