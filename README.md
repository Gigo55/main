adi=input("adınızı giriniz:")
maas=float(input("net maaşınızı giriniz:"))
yıl=float(input("kaç yıl çalıştınız:"))
if 0<yıl<=5:
    maastoplami=(maas*0.1)+maas
    print("maastoplamı:",maastoplami)
if 6<yıl<=10:
    maastoplami=(maas*0.15)+maas
    print("maastoplamı:",maastoplami)
if yıl>=11:
    maastoplami=(maas*0.25)+maas
    print("maastoplamı:",maastoplami)
print("Sayın",adi,"zamlı maaşınız",maastoplami,"TL'dir.")

