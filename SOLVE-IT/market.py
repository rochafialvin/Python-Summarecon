fruits = ['Apel', 'Anggur', 'Jeruk']
stock = [5, 7, 8]
price = [1000, 15000, 20000]

askAgain = True
while askAgain:
    # User akan menginput jumlah qty buah yg diinginkan
    qtyApple =  int(input('\nMasukkan jumlah Apel : '))
    # Jika permintaan user melebihi stock
    if qtyApple > stockApple:
        print(f'Kesalahan input, stock Apel : {stockApple}')
    else :
        askAgain = False


askAgain = True
while askAgain :
    # User akan menginput jumlah qty buah yg diinginkan
    qtyGrape =  int(input('\nMasukkan jumlah Anggur : '))
    # Jika permintaan user melebihi stock
    if qtyGrape > stockGrape:
        print(f'Kesalahan input, stock Anggur : {stockGrape}')
    else :
        askAgain = False



askAgain = True
while askAgain :
    # User akan menginput jumlah qty buah yg diinginkan
    qtyOrange =  int(input('\nMasukkan jumlah Jeruk : '))
    # Jika permintaan user melebihi stock
    if qtyOrange > stockOrange:
        print(f'Kesalahan input, stock Jeruk : {stockOrange}')
    else :
        askAgain = False

# Hitung total harga setiap buah
totalApple = qtyApple * priceApple
totalGrape = qtyGrape * priceGrape
totalOrange = qtyOrange * priceOrange

# Hitung total belanja keseluruhan
totalPrice = totalApple + totalGrape + totalOrange

print(
    '\n# # # # # # # # # # # # # # # # # #\n' +
    'Detail Belanja \n\n' +
    f'Apel : {qtyApple} x {priceApple} = {totalApple}\n' +
    f'Anggur : {qtyGrape} x {priceGrape} = {totalGrape}\n' +
    f'Jeruk : {qtyOrange} x {priceOrange} = {totalOrange}\n\n' +
    f'Total : {totalPrice}' +
    '\n# # # # # # # # # # # # # # # # # # '
)

moneyAgain = True

while moneyAgain:
    # User akan input uang
    userMoney = int(input('\nMasukkan jumlah uang : '))
    # Cari selisih uang user dengan total belanja
    margin = userMoney - totalPrice
    # Jika uang yang user masukkan kurang
    if userMoney < totalPrice:
        print(f'Uang yang Anda masukkan kurang Rp.{margin}')
    else :
        print(f'Terimakasih, uang kembalian Anda Rp. {margin}')
        moneyAgain = False


# Upgrade :
#      Memiliki menu utama :
#       1. Melihat list buah (name | stock | price)
#       2. Menambahkan list buah
#       3. Belanja buah
#
#     - Hanya boleh ada satu while dalam input qty semua buah
#     - Setiap selesai menambahkan buah, tampilkan list buah terbaru