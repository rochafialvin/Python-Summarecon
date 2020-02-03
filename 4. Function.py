# Function
# Sekumpulan / block kode yang dapat diberikan nama
# dan digunakan secara berulang
# Dapat memiliki input, output, atau keduanya

# def hello():
#     print(f'Hello ...')

# # # Menerima satu input
# def greet(name):
#     print(f'Hello, {name}')

# greet('Budi')

# # # Menerima dua input
# def plus(x, y):
#     res = x + y
#     # Memiliki satu ouput
#     # Kode setelah return tidak akan di proses
#     return res
    
# # result = plus(2, 3)
# # print(f'Nilai result : {result}')

# # Default parameter
# def multiple(x, y = 3):
#     res = x * y
#     return res

# resMultiple = multiple(5, 2)
# print(resMultiple)

# resMultiple = multiple(5)
# print(resMultiple)


# # Function dapat menerima function
# def oneFun():
#     print('Hello, i\'am oneFun')

# def twoFun(fun):
#     fun()

# twoFun(oneFun)

# # LIST

# day1 = 'Sunday'
# day2 = 'Monday'
# day3 = 'Tuesday'

# # index , dimulai dari nol
# days = ['Sunday', 'Monday', 'Tuesday']

# def renderDays(data):
#     for i in data:
#         print(f'Today is {i}')

# renderDays(days)

##############################
# RETURN MORE THAN ONE VALUE #
##############################

# def calculate(x, y):
#     sum = x + y
#     mult = x * y
#     mod = x % y

#     return [sum, mult, mod]

# final = calculate(10, 5)

# print(f'Hasil penjumlahan : {final[0]}')
# print(f'Hasil perkalian : {final[1]}')
# print(f'Hasil modulus : {final[2]}')

################
# Append & pop #
################

# # Append untuk menambahkan data ke list
# fruits = ['Apple', 'Banana', 'Cherry']
# fruits.append('Durian')

# # print(fruits)
# # ['Apple', 'Banana', 'Cherry', 'Durian']

# # Pop akan mengeluarkan data dari list
# # Kita bisa menentukan data yang ingin di pop dengan index
# fruits.pop() # Durian

# # 0 adalah index dar 'Apple'
# fruits.pop(0) # Apple

# # print(fruits)

# fruits[0] = 'Pisang'
# fruits[1] = 'Grape'

# print(fruits)

##########
# INSERT #
##########

# Untuk memasukkan data di index tertentu
# letter = ['A', 'B', 'D', 'E']

# Masukkan huruf C ke index - 2, sisanya akan bergeser
# letter.insert(2, 'C')

# print(letter)
# ['A', 'B', 'C','D', 'E']


# listList = [1, "String", True,['Satu', 'Dua', 'Tiga']]

# number = listList[3]
# print(number[1])

# listList[3][1]

# PERTAMA
# Buat sebuah function yang menerima list
# Akan me return hasil kali dua dari semua angka di dalam list

# nilaiAWal = [1, 3, 5, 7]
# hasilakhir = [2, 6, 10, 14]

# CARA PERTAMA
# listOne = [1, 3, 5, 7]

# def multiTwo(data):
#     listFinal = []

#     for i in data:
#         res = i * 2
#         listFinal.append(res)

#     return listFinal

# finalResult = multiTwo(listOne)

# CARA KEDUA
# listOne = [1, 3, 5, 7]

# def multiTwo(data):
#     listFinal = [ i * 2 for i in data]

#     return listFinal

# finalResult = multiTwo(listOne)

# print(finalResult)


# KEDUA
# Sebuah function yang dapat memisahkan nilai genap dan ganjil
# [11, 22, 34, 41, 52, 63, 71, 86,]
# [[22, 34, 52, 86], [11, 41, 63 ,71]]

startList = [11, 22, 34, 41, 52, 63, 71, 86,]

def oddEven(listNumber):
    oddList = []
    evenList = []
    finalList = []

    for i in listNumber:
        if i % 2 == 0:
            # input ke array genap
            evenList.append(i)
        else:
            # input ke array ganjil
            oddList.append(i)
    # Memasukkan list genap ke dalam list penampung (index 0)
    finalList.append(evenList)
    # Memasukkan list ganjil ke dalam list penampung (index 1)
    finalList.append(oddList)

    return finalList

result = oddEven( startList )
print(result)