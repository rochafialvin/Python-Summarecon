stockApple = 5
stockGrape = 7
stockOrange = 8

priceApple = 10000
priceGrape = 15000
priceOrange = 20000

# User akan menginput jumlah qty buah yg diinginkan
qtyApple =  int(input('Masukkan jumlah Apel : '))
# Jika permintaan user melebihi stock
if qtyApple > stockApple:
    print(f'Kesalahan input, stock Apel : {stockApple}')
    qtyApple = 0

# User akan menginput jumlah qty buah yg diinginkan
qtyGrape =  int(input('Masukkan jumlah Anggur : '))
# Jika permintaan user melebihi stock
if qtyGrape > stockGrape:
    print(f'Kesalahan input, stock Anggur : {stockGrape}')
    qtyGrape = 0

# User akan menginput jumlah qty buah yg diinginkan
qtyOrange =  int(input('Masukkan jumlah Jeruk : '))
# Jika permintaan user melebihi stock
if qtyOrange > stockOrange:
    print(f'Kesalahan input, stock Jeruk : {stockOrange}')
    qtyOrange = 0

# Hitung total harga setiap buah
totalApple = qtyApple * priceApple
totalGrape = qtyGrape * priceGrape
totalOrange = qtyOrange * priceOrange

# Hitung total belanja keseluruhan
totalPrice = totalApple + totalGrape + totalOrange

print(
    'Detail Belanja \n\n' +
    f'Apel : {qtyApple} x {priceApple} = {totalApple}\n' +
    f'Anggur : {qtyGrape} x {priceGrape} = {totalGrape}\n' +
    f'Jeruk : {qtyOrange} x {priceOrange} = {totalOrange}\n\n' +
    f'Total : {totalPrice}'
)