kilo=int(input("kilo giriniz:"))
boy=float(input("boy giriniz:"))
vki=kilo/(boy*boy)
if 18<=vki<=25:
    print("normal",str(vki))
elif 26<vki<=55:
    print("normal üstü",str(vki))
elif 56<=vki<=70:
     print("obez",str(vki))
else:
    print("hatalı deger girildi..")
    #boy: metre cinsinden olmalı,
            
