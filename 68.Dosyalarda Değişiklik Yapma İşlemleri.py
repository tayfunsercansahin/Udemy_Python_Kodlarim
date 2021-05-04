with open("bilgiler.txt","r+") as file:
    print(file.read())

with open("bilgiler.txt","r+") as file:
    file.seek(10)
    file.write("Deneme")
with open("bilgiler.txt","r+") as file:
    print(file.read())

with open("bilgiler.txt","a") as file:
    file.write("Mustafa Günay\n")
with open("bilgiler.txt","r+") as file:
    print(file.read())

with open("bilgiler.txt","r+") as file:
    içerik = file.read()
    içerik = "Mehmet Keper\n" + içerik
    file.seek(0)
    file.write(içerik)
with open("bilgiler.txt","r+") as file:
    print(file.read())

with open("bilgiler.txt","r+") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    for i in liste:
        file.write(i)
with open("bilgiler.txt","r+") as file:
    print(file.read())