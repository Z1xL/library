import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
 
sifre_uzunluğu = int(input("Şifre kaç karakterden oluşturulsun: "))
sifre_adeti = int(input("Kaç adet şifre oluşturulsun: "))
for y in range(0, sifre_adeti):
        sifre = ""
        for y in range(0, sifre_uzunluğu):
            sifre2 = random.choice(x)
            sifre      = sifre + sifre2
        print("Random sifreniz: " , sifre)
