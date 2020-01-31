# Function
# Sekumpulan / block kode yang dapat diberikan nama
# dan digunakan secara berulang
# Dapat memiliki input, output, atau keduanya

# def hello():
#     print(f'Hello ...')

# # Menerima satu input
# def greet(name):
#     print(f'Hello, {name}')

# # Menerima dua input
# def plus(x, y):
#     res = x + y
#     # Memiliki satu ouput
#     # Kode setelah return tidak akan di proses
#     return res
    
# result = plus(2, 3)
# print(f'Nilai result : {result}')

# Default parameter
# def multiple(x, y = 3):
#     res = x * y
#     return res

# resMultiple = multiple(5, 2)
# print(resMultiple)

# resMultiple = multiple(5)
# print(resMultiple)


# Function dapat menerima function
# def oneFun():
#     print('Hello, i\'am oneFun')

# def twoFun(fun):
#     fun()

# twoFun(oneFun)

# LIST

day1 = 'Sunday'
day2 = 'Monday'
day3 = 'Tuesday'

# index , dimulai dari nol
# days = ['Sunday', 'Monday', 'Tuesday']

# def renderDays(data):
#     for i in data:
#         print(f'Today is {i}')

# renderDays(days)

# Append & pop

# Append untuk menambahkan data ke list
# fruits = ['Apple', 'Banana', 'Cherry']
# fruits.append('Durian')

# print(fruits)

# Pop akan mengeluarkan data dari list
# Kita bisa menentukan data yang ingin di pop dengan index
# fruits.pop() # Durian
# fruits.pop(0) # Apple

# print(fruits)

# fruits[0] = 'Pisang'
# fruits[1] = 'Grape'

# print(fruits)


listList = [1, "String", True,['Satu', 'Dua', 'Tiga']]
number = listList[3]
print(number[1])

# listList[3][1]

# PERTAMA
# Buat sebuah function yang menerima list
# Akan me return hasil kali dua dari semua angka di dalam list

# nilaiAWal = [1, 3, 5, 7]
# hasilakhir = [2, 6, 10, 14]

# KEDUA
# Sebuah function yang dapat memisahkan nilai genap dan ganjil
# [11, 22, 34, 41, 52, 63, 71, 86,]
# [[22, 34, 52, 86], [11, 41, 63 ,71]]