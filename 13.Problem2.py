kilo = int(input("Kilonuzu girin(kg):"))
boy = float(input("Boyunuzu girin(m):"))

print("Kilonuz = {} kg , Boyunuz = {} m\n".format(kilo,boy))

bedenKitleIndeksi = kilo / (boy ** 2)

print("Beden kitle indeksiniz: {}\n".format(bedenKitleIndeksi))