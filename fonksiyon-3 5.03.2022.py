def bilgileriGoster(ad, soyad, no, sinif):
    print("Adınız: ", ad)
    print("Soyadınız: ", soyad)
    print("Numaranız: ", no)
    print("Sınıfınız: ", sinif)
ad = input("Adınız:")
soyad = input("Soyadınız:")
no = input("Numaranız:")
sinif = input("Sınıfınız:")

bilgileriGoster(ad, soyad, no, sinif)
bilgileriGoster("Gökhan","Küçükdemirkol","05396957654")
#eğer 3 tane parametre ile de fonksiyonu çalıştırmak istiyorsak default değerler tanımlamalıyız
