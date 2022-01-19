#havaalanı bagaj tutar hesabı
bagac=int(input("bagaj:"))
if  (bagac>20):
    bagacTutarı=(bagac-20)*10
    print("ödenecek bagaj tutarı:",str(bagacTutarı),"tl'dir.")
elif (bagac<=20):
    print("ödeme yapılması gereksiz.")
        
