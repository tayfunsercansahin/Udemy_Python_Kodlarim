try:
    a = int("12315125")
    print("Program burada!")
except:
    print("Bir hata oluştu!")
print("Bloklar sona erdi.")

try:
    a = int("sadsada12315125")
    print("Program burada")
except:
    print("Bir hata oluştu!")
print("Bloklar sona erdi.")

try:
    a = int("sadsada12315125")
    print("Program burada")
except ValueError:
    print("Bir hata oluştu!")
print("Bloklar son erdi.")

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a/b)
except ValueError:
    print("Lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
print("Bloklar sona erdi.")

def tersçevir(s):
    if(type(s) != str):
        raise ValueError("Lütfen string bir değer gönderin.")
    else:
        return s[::-1]

print(tersçevir("Python"))
#print(tersçevir(12))

try:
    print(tersçevir(12))
except ValueError:
    print("Fonksiyon hata verdi, string girin!")