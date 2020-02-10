########
# LIST #
########

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

########
# SORT #
########

# Mengurutkan data ASCENDING / ASC / kecil - besar

# listStr = ['Can', 'Angry', 'Evil', 'Forgive']
# listInt = [7, 5, 9, 1, 3]
# listBool = [False, True, True, False]

# ['Angry', 'Can', 'Evil', 'Forgive']
# listStr.sort()
# print(
#     listStr
# )

# [1, 3, 5, 7, 9]
# listInt.sort()
# print(
#     listInt
# )

# [False, False, True, True]
# listBool.sort()
# print(
#     listBool
# )

# Mengurutkan data DESCENDING / DESC / besar - kecil

# listStr = ['Can', 'Angry', 'Evil', 'Forgive']
# listInt = [7, 5, 9, 1, 3]
# listBool = [False, True, True, False]

# ['Forgive', 'Evil', 'Can', 'Angry']
# listStr.sort(reverse = True)
# [9, 7, 5, 3, 1]
# listInt.sort(reverse = True)
# [True, True, False, False]
# listBool.sort(reverse = True)

# print(listStr)
# print(listInt)
# print(listBool)

# Ambil 3 gaji terendah dan 3 gaji tertinggi

# listSalary =[
#     7500000,
#     9000000,
#     300000,
#     200000,
#     1700000
# ]

# # Terendah
# listSalary.sort()
# print(
#     listSalary[0:3]
# )

# # Tertinggi
# listSalary.sort(reverse=True)
# print(
#     listSalary[0:3]
# )

# x = [40, 100, 1, 5, 25, 10]
# y = [ 5, 25, 10]

# def minMax(listNum):
#     startList = listNum
    
#     # rendah - tinggi
#     # [1, 5, 10, 25, 40, 100]
#     listNum.sort()
    
#     #Nilai Awal 
#     print(startList)

#     # Nilai Terendah
#     print(listNum[0])

#     # Nilai Tertinggi
#     print(listNum[-1])

# minMax(x)
# minMax(y)


# x = [40, 100, 1, 5, 25, 10]
# y = [ 5, 25, 10]

# def maxMin(listNum):
#     startList = listNum
    
#     # [1, 5, 10, 25, 40, 100]
#     listNum.sort()

#     min = listNum[0]
#     max = listNum[-1]
    

#     return [startList, min, max]

# tmp = maxMin(y)
# print(tmp)

# Min max
# x = [40, 100, 1, 5, 25, 10]
# y = [ 5, 25, 10]

# def minMax(x):
#     min = max = x[0]

#     for i in range(len(x)):
#         if x[i] < min :
#             min = x[i]
#         if x[i] > max :
#             max = x[i]

#     return [x, min, max]


# tmp = minMax(x)
# print(f'List : {tmp[0]}')
# print(f'Min : {tmp[1]}')
# print(f'Max : {tmp[2]}')



