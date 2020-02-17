# FUNCTION
# Block kode yang memiliki nama dan dapat di running secara berulang
# Sebuah function dapat memiliki input, output, atau keduanya
# Sebuah function dapat 'menghasilkan' nilai

##################################
# function tanpa input dan output
#################################
# Deklarasi / pembuatan function
def pure():
    resSum = 4 + 7
    print(f'Hasil penjumlahan : {resSum}')

# running function, nama function diikuti dg kurung ()
# pure()

########################
# function dengan input
######################
# Banyaknya jumlah input tidak terbatas
def whatday(day, feel):
    # Mengubah huruf pertama menjadi kapital
    day = day.capitalize()
    print(f'Today is {day}, and i\'m {feel} ')

# whatday('monday', 'Happy')
# whatday('tUesday', 'Unhappy')
# whatday('WEDNESDAY', 'Sick')

################################
# function yang memiliki output
###############################
def summ(x, y):
    res = x + y
    return res
    # Setelah me-return sesuatu
    # Tidak akan membaca kode berikutnya
    # print('Not running')

# di sediakan variable penampung, karena 'summ' memiliki output
resultSumm = summ(4, 5)
# resultSumm adalah : 9
print(f'resultSumm adalah : {resultSumm}')