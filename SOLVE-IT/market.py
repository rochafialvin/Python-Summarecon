fruits = ['Apel', 'Anggur', 'Jeruk']
stock = [5, 7, 8]
price = [1000, 15000, 20000]
qty = [0 , 0, 0]

# input dari user diubah ke integer
mainOpt = int(input(
    'Menu Utama \n' +
    '1. Menampilkan list\n' +
    '2. Menambahkan buah\n' +
    '3. Belanja\n' +
    'Menu pilihan :' 
))

if mainOpt == 1:
    print('CreateList')
elif mainOpt == 2 :
    print('Add Fruit')
elif mainOpt == 3 :
    print('Shopping')

    # Akan loop sebanyak data buah
    for i in range(len(fruits)):
        askAgain = True
        while askAgain:
            # User akan menginput jumlah qty buah yg diinginkan
            qty[i] =  int(input(f'\nMasukkan jumlah {fruits[i]} : '))
            # Jika permintaan user melebihi stock
            if qty[i] > stock[i]:
                print(f'Kesalahan input, stock Apel : {stock[i]}')
            else :
                askAgain = False






    # # Hitung total harga setiap buah
    totalApple = qtyApple * priceApple
    totalGrape = qtyGrape * priceGrape
    totalOrange = qtyOrange * priceOrange

    # # Hitung total belanja keseluruhan
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

    # moneyAgain = True

    # while moneyAgain:
    #     # User akan input uang
    #     userMoney = int(input('\nMasukkan jumlah uang : '))
    #     # Cari selisih uang user dengan total belanja
    #     margin = userMoney - totalPrice
    #     # Jika uang yang user masukkan kurang
    #     if userMoney < totalPrice:
    #         print(f'Uang yang Anda masukkan kurang Rp.{margin}')
    #     else :
    #         print(f'Terimakasih, uang kembalian Anda Rp. {margin}')
    #         moneyAgain = False


# Upgrade :
#      Memiliki menu utama :
#       1. Melihat list buah (name | stock | price)
#       2. Menambahkan list buah
#       3. Belanja buah
#
#     - Hanya boleh ada satu while dalam input qty semua buah
#     - Setiap selesai menambahkan buah, tampilkan list buah terbaru