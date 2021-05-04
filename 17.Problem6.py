a = float(input("Dik üçgenin ilk kenarını girin:"))
b = float(input("Dik üçgenin ikinci kenarını girin:"))

hipotenüsünKaresi = (a ** 2) + (b ** 2)

hipotenüs = hipotenüsünKaresi ** 0.5

print("İlk kenar: {} , İkinci kenar: {} , Hipotenüs: {}\n".format(a,b,hipotenüs))