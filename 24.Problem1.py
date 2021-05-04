kilo = int(input("Kilonuzu girin(kg):"))
boy = float(input("Boyunuzu girin(m):"))

bki = kilo / (boy ** 2)

if bki < 18.5:
    print("Zayıf")
elif (bki < 25) and (bki > 18.5):
    print("Normal")
elif (bki < 30) and (bki > 25):
    print("Fazla kilolu")
elif (bki > 30):
    print("Obez")
else:
    print("Geçersiz boy ve kilo girdiniz!")

