# def times2(num):
#     return num * 2

# result = times2(4) # 2

# Lambda
# Biasa digunakan sebagai callback function

# lambda num: num * 2

# MAP
# Digunakan untuk merubah bentuk data
# Menerima dua parameter , function dan list
# function yang memiliki istilah 'callback function'
# function ini harus menerima satu buah parameter
# function tersebut harus me return sesuatu
# return mapobject, untuk mendapatkan listnya harus
# di masukkan ke dalam function list()

# witch function
# def times2(num):
#     return num * 2

# numList = [1, 2, 3 ,4 , 5]

# mapObj = map(times2, numList)
# result = list(mapObj)

# print(result)

# with lambda

# mapObj = map(lambda num: num * 2, numList)
# result = list(mapObj)

# print(result)


# FILTER
# Digunakan untuk menyaring data
# Menerima dua parameter , function dan list
# function yang memiliki istilah 'callback function'
# function ini harus menerima satu buah parameter
# function tersebut harus me return bool (True , False)
# return filterobject, untuk mendapatkan listnya harus
# di masukkan ke dalam function list()

# with function
def even(num):
    return num % 2 == 0

numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]

evenList = list(myFilter(even, numList))

print(evenList)

# # With Lambda
# evenList = list(filter(lambda x: x % 2 == 0, numList))

# print(evenList)


# SEARCH 

# word = ['Sands', 'Peace', 'Sandals', 'Birds', 'Dear']

numList = [1, 2, 3, 4, 5]
resInt = 2 in numList # True
resInt = 6 in numList # False

numString = 'You can jump'
resStr = 'You' in numString # True
resStr = 'you' in numString # False

print(resStr)


# HOMEWORK
# Buat duplicate function untuk map dan filter

def myMap(fun, lis):
    # do something

def myFilter(fun, lis):
    # do something

