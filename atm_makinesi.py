print("""
*****************
Hoşgeldiniz...

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Çıkış yapmak için lütfen "q" ya basın. 

*****************
"""
)

bakiye = 10000


while True:
    islem = input("Yapmak istediğiniz işlemi giriniz:")

    if (islem == "q"):
        print("Yine bekleriz...")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye += miktar

    elif (islem == "3"):
        miktar = int(input("Çekmek istediğiniz miktarı giriniz:"))
        if (bakiye - miktar < 0):
            print("Yetersiz Bakiye")
            continue
        bakiye -= miktar

    else:
        print("Geçersiz işlem girişi.")

