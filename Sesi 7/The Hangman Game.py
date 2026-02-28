import random

def pilih_kata():
    daftar_kata = ["indonesia", "jerman", "belanda", "inggris", "turki", "australia", "china"]
    return random.choice(daftar_kata)


def tampilkan_kata(kata, huruf_ditebak):
    tampilan = ""
    for huruf in kata:
        if huruf in huruf_ditebak:
            tampilan += huruf + " "
        else:
            tampilan += "_ "
    print("\nKata: ", tampilan.strip())


def cek_menang(kata, huruf_ditebak):
    for huruf in kata:
        if huruf not in huruf_ditebak:
            return False
    return True


def game_loop():
    kata_rahasia = pilih_kata()
    huruf_ditebak = []
    nyawa = 6

    print("\n===== SELAMAT DATANG DI HANGMAN GAME =====")
    print("Tebak hurufnya sebelum kesempatannya habis!")
    print("Cluenya adalah tebak nama negara")

    while nyawa > 0:
        tampilkan_kata(kata_rahasia, huruf_ditebak)
        print("Huruf yang sudah ditebak: ", huruf_ditebak)
        print("Nyawa: ", nyawa)

        tebakan = input("\nTebak satu huruf: ").lower()

        #Validasi input
        if len(tebakan) != 1 or not tebakan.isalpha():
            print("Masukkan hanya satu huruf saja !!!")
            continue

        if tebakan in huruf_ditebak:
            print("Huruf sudah ditebak sebelumnya")
            continue

        if tebakan in kata_rahasia:
            print("Benar ")
            huruf_ditebak.append(tebakan)

        else:
            print("Salah ")
            huruf_ditebak.append(tebakan)
            nyawa -= 1

        if cek_menang(kata_rahasia, huruf_ditebak):
            print("\nSELAMAT! KAMU MENANG !!! ")
            print("Kata yang benar adalah:", kata_rahasia)
            return

    print("\nGAME OVER")
    print("Kata yang benar adalah:", kata_rahasia)

game_loop()
