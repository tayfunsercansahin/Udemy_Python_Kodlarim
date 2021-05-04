işlem = input("İşlemi girin:")

if işlem == "1":
    print("İşlem 1 seçildi.")
elif işlem == "2":
    print("İşlem 2 seçildi.")
elif işlem == "3":
    print("İşlem 3 seçildi.")
elif işlem == "4":
    print("İşlem 4 seçildi.")
else:
    print("Geçersiz işlem!")

note = float(input("Notu girin:"))

if (note >= 90):
    print("AA")
elif (note >= 70):
    print("BB")
elif (note >= 50):
    print("CC")
else:
    print("Kaldın!")
