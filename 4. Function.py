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

# startList = [11, 22, 34, 41, 52, 63, 71, 86,]

# def oddEven(listNumber):
#     oddList = []
#     evenList = []
#     finalList = []

#     for i in listNumber:
#         if i % 2 == 0:
#             # input ke array genap
#             evenList.append(i)
#         else:
#             # input ke array ganjil
#             oddList.append(i)
#     # Memasukkan list genap ke dalam list penampung (index 0)
#     finalList.append(evenList)
#     # Memasukkan list ganjil ke dalam list penampung (index 1)
#     finalList.append(oddList)

#     return finalList

# result = oddEven( startList )
# print(result)

# if else:

# Jika sebuah kata diawali dengan huruf vokal 'a i u e o', tambahkan huruf 'yay' di akhir
# Jika tidak, taruh huruf pertama di paling belakang kemudian tambahkan 'ay'

# apple --> appleyay
# word --> ordway

def changeWord(word):
    if word[0] in 'aiueo':
        word = word + 'yay'
    else :
        word = word[1:] + word[0] +'ay'

    print(word)

# changeWord("apple")
# changeWord("word")


# Reversed Sentence
# Hello  my friend --> friend my hello
# This is friday --> friday is This
# split()
# reverse() 
# join()

def sentRev(word):
    res = word.split() # ['Hello', 'my', 'friend']
    res.reverse() # ['friend', 'my', 'Hello']
    res = " ".join(res) # friend my Hello
    print(res)

# sentRev('Hello my friend')

# Has 99
def has99(lis):
    idx = lis.index(9)
    if lis[idx + 1] == 9:
        return True
    else:
        return False


print(has99([1, 9, 9]))
print(has99([5, 9, 2, 9]))
print(has99([9, 3, 9]))
print(has99([7, 9, 9, 6]))
# [1, 9, 9] --> True
# [5, 9, 2, 9] --> False
# [9, 3, 9] --> False
# [7, 9, 9, 6] --> False


# word = "Friday"

# word[2] # i
# word[-1] # y
# word[1:5] # rida
# word[1:] # riday
# word[:5] # Frida