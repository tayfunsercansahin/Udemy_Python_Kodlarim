a = int(input("a değerini girin:"))
b = int(input("b değerini girin:"))
c = int(input("c değerini girin:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci kök: {}\nİkinci Kök: {}\n".format(x1,x2))