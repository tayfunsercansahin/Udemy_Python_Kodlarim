def tamBolenleriBulma(sayı):
    tamBolenler = []
    for i in range(1,sayı+1):
        if(sayı % i == 0):
            tamBolenler.append(i)
    return tamBolenler

while True:
    sayı = input("Sayı:")
    if(sayı == "q"):
        print("Programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)
        print("Tam bölenler:",tamBolenleriBulma(sayı))
