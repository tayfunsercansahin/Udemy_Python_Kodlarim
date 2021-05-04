x = float(input("Birinci sayıyı girin:"))
y = float(input("İkinci sayıyı girin:"))
z = float(input("Üçüncü sayıyı girin:"))

if (x > y):
    if (x > z):
        print("En büyük sayı birinci sayıdır.")
    elif (x == z):
        print("En büyük sayılar birinci ve üçüncü sayılardır.")
    else:
        print("En büyük sayı üçüncü sayıdır.")
elif (y > x):
    if (y > z):
        print("En büyük sayı ikinci sayıdır.")
    elif (y == z):
        print("En büyük sayılar ikinci ve üçüncü sayılardır.")
    else:
        print("En büyük sayı üçüncü sayıdır.")





