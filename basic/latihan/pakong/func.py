import time
import random

uang = 100000
space = "\n" * 10
binatang = ["kambing", "kuda", "anjing", "babi"]
binDecor = """
*****************  ***********
* K A M B I N G *  * K U D A *
*****************  ***********

***************  ***********
* A N J I N G *  * B A B I *
***************  ***********
""" + space

bangkrut = """
***********************************
* A N D A  >> B A N G K R U T ! ! *
***********************************
""" + space






while True:
    pakongOnline = f"""
    ******************************
    * P A K O N G >> O N L I N E *
    ******************************

        >> by raja serah <<

    Keuntungan ditangan anda..
    kami berikan Free Rp.100.000

    Yang menang untung...
    Yang kalah untung...

    But Carabut Cabuuuuuttttt...


         U A N G  - A N D A
    *****************************
               {uang}
    *****************************

    """

    print("\n" * 50)
    print(pakongOnline)
    print("uang anda : Rp.",uang)
    if uang <= 0:
        print("\n" * 50)
        print(bangkrut)
        time.sleep(5)
        exit()


    taruh = int(input("masukan taruhan anda : "))
    while taruh > uang:
        print("\n" * 50)
        print("Maaf uang anda tidak cukup \nSilakan masukan jumlah sesuai..\n")
        print("uang anda Rp.", uang)
        taruh = int(input("masukan taruhan anda : "))


    print("\n")
    print("\n" * 50)
    print(binDecor)
    x = input("pilih binatang anda: ")
    x = x.lower()
    if x in binatang:

        print("\n" * 50)
        print("semoga beruntung...")
        print("silakan tunggu...")
        time.sleep(3)
        print("but carabut cabutt...")
        time.sleep(1)

        print("\n" * 50)
        result = random.choice(binatang)
        result = result.lower()
        print("""
Binatangnya :
**********************
* >>>>> {} <<<<< *
**********************""".format(result))

        print("\n")
        if x == result:
            uang = uang + taruh
            print(f"""
*****************************
* >> SELAMAT ANDA MENANG << *
*          {taruh}          *
*****************************






""")
            time.sleep(5)
            print("\n" * 50)
        else:
            uang = uang - taruh
            print("""
***************************
* >> ANDA KALAH !!! << *  *
* >> SILAKAN COBA LAGI << *
***************************









""")
            time.sleep(5)
            print("\n" * 50)

    else:
        print("\nmaaf pilihan anda tidak ada..")
