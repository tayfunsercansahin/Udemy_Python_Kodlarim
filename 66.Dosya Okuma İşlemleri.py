file = open("bilgiler.txt","r")
file.close()

try:
    file = open("olmayanDosya.txt","r")
except FileNotFoundError:
    print("Dosya bulunamadı.")

file = open("bilgiler.txt","r")
for i in file:
    print(i)
file.close()

file = open("bilgiler.txt","r")
for i in file:
    print(i, end = "")
file.close()

file = open("bilgiler.txt","r")
içerik = file.read()
print("\nDosyanın içeriği:")
print(içerik)

file = open("bilgiler.txt","r")
print(file.readline())
file.close()

file = open("bilgiler.txt","r")
liste = file.readlines()
print(liste)
file.close()