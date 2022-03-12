def bilgileriGoster(ad, soyad, no="yok", sinif="yok"):
    print("Adınız: ", ad)
    print("Soyadınız: ", soyad)
    print("Numaranız: ", no)
    print("Sınıfınız: ", sinif)
ad = input("Adınız:")
soyad = input("Soyadınız:")
no = input("Numaranız:")
sinif = input("Sınıfınız:")

bilgileriGoster(ad, soyad, no, sinif)
bilgileriGoster("Gökhan","Küçükdemirkol","171824")
#eğer 3 tane parametre ile de fonksiyonu çalıştırmak istiyorsak default değerler tanımlamalıyız