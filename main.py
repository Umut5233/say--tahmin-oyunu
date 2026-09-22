import random

tahmin_edilecek_sayı = random.randint(1,100)
print (tahmin_edilecek_sayı)

print ("Sayı tahmin oyununa hoş geldiniz!")
print ("Lütfen 1 ile 100 arası bir sayı tutunuz.")

kullanıcı_tahmini = input ("-->")

if int(kullanıcı_tahmini) == tahmin_edilecek_sayı:
    print ("Tahmininiz Doğru Tebrikler!")

elif int(kullanıcı_tahmini) != tahmin_edilecek_sayı:
    print ("Tahmininiz Yanlış.")
