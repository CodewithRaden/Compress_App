def kompresi_rle(teks):
    hasil = ""
    i = 0
    while i < len(teks):
        count = 1
        while i + 1 < len(teks) and teks[i] == teks[i + 1]:
            count += 1
            i += 1
        hasil += teks[i] + str(count)
        i += 1
    return hasil


def dekompresi_rle(teks):
    hasil = ""
    i = 0
    while i < len(teks):
        karakter = teks[i]
        i += 1
        angka = ""
        while i < len(teks) and teks[i].isdigit():
            angka += teks[i]
            i += 1
        hasil += karakter * int(angka)
    return hasil


teks_asli = input("Masukkan teks untuk dikompresi: ")
teks_terkompresi = kompresi_rle(teks_asli)
print("Teks Terkompresi:", teks_terkompresi)

teks_dekompresi = dekompresi_rle(teks_terkompresi)
print("Teks Dekompresi:", teks_dekompresi)
