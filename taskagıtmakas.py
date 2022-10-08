import random
secenek = ["Taş", "Kağıt", "Makas"]
tas = secenek[0]
kagıt = secenek[1]
makas = secenek[2]

print("Taş Kağıt Makas Oyununa Hoş Geldiniz .. \n Oyunu Bitirmek İçin q Tuşuna Basabilirsiniz")

while True:
    secim = input("Taş mı Kağıt mı Makas mı?")
    bil_secim = random.choice(secenek)

    if secim == tas:

        if bil_secim == tas:
            print("Bilgisayar Seçimi : Taş  \n Oyun Sonucu: Berabere")

        elif bil_secim == kagıt:
            print("Bilgisayar Seçimi : Kağıt  \n Oyun Sonucu: Kaybettiniz.. :(")

        else:
            print("Bilgisayar Seçimi : Makas  \n Oyun Sonucu: Kazandınız.. :)")

    if secim == kagıt:

        if bil_secim == tas:
            print("Bilgisayar Seçimi : Taş  \n Oyun Sonucu: Kazandınız.. :)")

        elif bil_secim == kagıt:
            print("Bilgisayar Seçimi : Kağıt  \n Oyun Sonucu: Berabere")

        else:
            print("Bilgisayar Seçimi : Makas  \n Oyun Sonucu: Kaybettiniz.. :(")

    if secim == makas:

        if bil_secim == tas:
            print("Bilgisayar Seçimi : Taş  \n Oyun Sonucu: Kaybettiniz.. :(")

        elif bil_secim == kagıt:
            print("Bilgisayar Seçimi : Kağıt  \n Oyun Sonucu: Kazandınız.. :)")

        else:
            print("Bilgisayar Seçimi : Makas  \n Oyun Sonucu: Berabere..")

    if secim == "q":
        print("Çıkış Yapılıyor..")
        break
