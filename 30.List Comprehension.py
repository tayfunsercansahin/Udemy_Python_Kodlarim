liste1 = [1,2,3,4,5]
liste2 = list()
for i in liste1:
    liste2.append(i)
print("Liste1: ",liste1)
print("Liste2: ",liste2)

liste3 = [1,2,3,4,5]
liste4 = [i for i in liste3]
print("Liste4: ",liste4)

liste = [3,4,5]
liste1 = [i * 2 for i in liste]
print("Liste1: ",liste1)

liste = [(1,2),(3,4),(5,6)]
liste2 = [(i,j) for i,j in liste]
liste1 = [i * j for i,j in liste]
print("Liste2 =",liste2)
print("Liste1 =",liste1)

s = "Python"
liste1 = [i * 3 for i in s]
print(liste1)

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = list()
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print(liste1)
