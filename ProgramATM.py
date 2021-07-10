print("\t\t\tBAYNIAGA")
print(" ")
print("\nselamat datang di program ATM, Bank BAYNIAGA")
pin = 1234
i = 1
saldo = 50000000
mengulang = 'Y'
while i>0:
    pin_benar = float(input("\nsilahkan masukkan 4 digit pin anda : "))
    if pin_benar==(1234):
        print("\nanda memasukkan pin anda benar")
        break
    else :
        print("\pin yang anda masukkan salah, silahkan ulangi kembali")
        i = i - 1

pilihan = " "
while(pilihan != "N"):
    print("\n1. silahkan tekan 1 untuk informasi saldo\n"
          "2. silahkan tekan 2 untuk penarikan uang \n"
          "3. silahkan tekan 3 untuk menabung\n"
          "4. silahkan tekan 4 untuk keluar")
    menu = int(input("\nsilahkan pilih menu yang anda lakukan => "))
    print("=" * 50)
    if menu==1:
        print("isi saldo anda : ", saldo)
        mengulang = input("apakah anda ingin mengulang y/t : ")
        if mengulang == "t":
            print("TERIMA KASIH")
            break
    elif menu==2:
        print("jumlah penarikan nominal sebesar : 50000, 100000, 250000, 500000, 1000000")
        jumlah_tarik = int(input("berapa jumlah penarikan anda : "))
        saldo = saldo - jumlah_tarik
        print("\nsisa saldo rekening anda : ", saldo)
        mengulang = input("apakah anda ingin mengulang y/t : ")
        if mengulang == "t":
            print("TERIMA KASIH")
            break
    elif menu==3:
        tabung = float(input("masukan nominal yang ingin ditabung :"))
        hasil = saldo + tabung
        print("sisa saldo anda adalah :", int(hasil))
        mengulang = input("apakah anda ingin mengulang y/t : ")
        if mengulang == "t":
            print("TERIMA KASIH")
            break
    else:
        print("kartu akan keluar dari mesin ATM...")
        print("\nterima kasih sudah menggunakan Bank BAYNIAGA")
        break