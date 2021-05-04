print("""*****************
Kullanıcı Girişi
*****************""")

sys_kullanıcı_adı = "murat"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı adını girin:")
parola = input("Parolayı girin:")

if (sys_kullanıcı_adı == kullanıcı_adı) and (sys_parola != parola):
    print("Kullanıcı adı doğru, parola yanlış")
elif (sys_kullanıcı_adı != kullanıcı_adı) and (sys_parola == parola):
    print("Kullanıcı adı yanlış, parola doğru")
elif (sys_kullanıcı_adı != kullanıcı_adı) and (sys_parola != parola):
    print("Kullanıcı adı ve parola yanlış")
else:
    print("Sisteme başarıyla giriş yapıldı...")
