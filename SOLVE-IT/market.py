stockApple = 5
stockGrape = 7
stockOrange = 8

priceApple = 10000
priceGrape = 15000
priceOrange = 20000

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
#     1. Jika user memasukkan qty lebih dari stock :
#         minta user untuk input ulang, sampai tidak melebihi stock

#     2. Minta user input sejumlah uang:
#         Jika uangnya kurang, munculkan pesan kurangnya berapa
#         kemudian minta beliau input lagi

#         Jika uangnya pas atau lebih, 'Terimakasih, kembalian Anda (sekian)'