"""
**************
Asal Sayı mı?
**************"""
def asalMi(sayı):
    if(sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
        return True

while True:
    sayı = input("Sayı:")
    if(sayı == "q"):
        print("Programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)

        if(asalMi(sayı)):
            print(sayı,"asal bir sayıdır.")
        else:
            print(sayı,"asal bir sayı değildir.")

