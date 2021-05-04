liste = ["Elma",35,"Merhaba",3.14,5]
x = type(liste)
print(x)

liste = []
print(liste)

liste = list()
print(liste)

liste2 = [1,2,3,4,5,6,7,8,9]
y = len(liste2)
print("Kaç Elemanlı? =",y)

liste = list("Merhaba")
print(liste)
print(len(liste))

liste = [3,4,5,6,7,8,9,10]
print(liste[2],liste[7],liste[-2],sep = ",")
print(liste[len(liste)-1])
print(liste[4:])
print(liste[:5])
print(liste[::2])
print(liste[::-1])

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + liste2
print(liste3)
print(liste2 * 3)
liste1 = liste1 * 3
print(liste1)

print(liste2)
liste2[1] = 10
print(liste2)
print(liste2 * 2)

liste = [1,2,3,4,5]
print(liste[:2])
liste[:2] = [10,11]
print(liste)

liste = [10,11,3,4,5,6]
print(liste)
liste.append("Python")
print(liste)
liste.append(12)
print(liste)
liste.pop(0)
print(liste)

liste = [34,2,1,5,6,32,100]
print(liste)
liste.sort()
print(liste)
liste.sort(reverse = True)
print(liste)

liste = ["Php","Python","Java","C"]
print(liste)
liste.sort()
print(liste)
liste.sort(reverse = True)
print(liste)

liste = [[1,2],[3,4],[5,6]]
print(liste)
print(liste[1][0])

liste = [1,2,3,4,5]
a = liste * 3
print(liste)







