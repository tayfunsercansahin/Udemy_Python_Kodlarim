with open("bilgiler.txt","r") as file:
    for i in file:
        print(i, end = "")

print("\n")

with open("bilgiler.txt","r") as file:
    file.seek(4)
    içerik = file.read(10)
    print(içerik)