sözlük1 = {"Bir":1,"İki":2,"Üç":3,"Dört":4}
print(type(sözlük1))
print(sözlük1)
print(sözlük1["Bir"])
print(sözlük1["Dört"])
sözlük1["Beş"] = 5
print(sözlük1)

sözlük2 = {}
print(sözlük2)
sözlük2 = dict()
print(sözlük2)

a = {"Bir":[1,2,3,4],"İki":[[1,2],[3,4],[5,6]],"Üç":15}
print(a["İki"])
print(a["Bir"])

print(sözlük1)
sözlük1["Beş"] = 10
print(sözlük1)
sözlük1["Beş"] += 1
print(sözlük1)

a = {"Sayılar":{"Bir":1,"İki":2,"Üç":3},"Meyveler":{"Kiraz":"Yaz","Portakal":"Kış","Erik":"Yaz"}}
print(a)
print(a["Sayılar"])
print(a["Meyveler"])
print(a["Sayılar"]["İki"])
print(a["Meyveler"]["Kiraz"])

print(sözlük1)
print(sözlük1.keys())
print(sözlük1.values())
print(sözlük1.items())

for k,v in sözlük1.items():
    print(k,v)