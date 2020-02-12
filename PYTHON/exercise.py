# Number One
# def wordRev
# Buatlah sebuah function yang menerima sebuah kata
# Reverse huruf setiap kata

# Contoh:
#   Hello my friend --> olleH ym dneirf
#   abc de efg --> cba ed gfe


# Number Two
# def sum01
# Buat function yang menerima list of number
# Jumlahkan semua angka, kecuali angka yang ada diantara angka 0 - 1

def sum01(lis):
    # Temukan index angka 0 dan 1
    # Untuk index angka 1 dijumlahkan dengan angka 1
    zero = lis.index(0)
    one = lis.index(1) + 1

    # Delete data dari index angka 0 hingga index angka 1
    del lis[zero:one]

    # Sisa angka pada list, dijumlahkan
    result = sum(lis)

    # Print hasil jumlah dari data lis
    print(result)

sum01([5, 0, 3, 1, 2, 1])

# [2, 4, 0, 1, 11] -- > 17 (0, 1 tidak masuk hitungan)
# [7, 0, 3, 1, 7, 9] --> 23 (0, 3, 1 tidak masuk hitungan)
# [5, 0, 3, 2, 1] --> 5 (0, 3, 2, 1 tidak masuk hitungan)

