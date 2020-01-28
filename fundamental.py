# Untuk menampilkan teks (komentar)
# print('My first code')

# Variable
# Untuk menyimpan sebuah data
# Tidak bisa diawali dengan angka
# string, tipe data yg menyimpan teks = 'Vinales'
# number , float : desimal (0.25, 3.14), integer : bulat (3, 5, 6)
# camelCase
firstName = 'Vinales'
lastName = 'John'
age = 32

# Function type digunakan untuk mengethaui tipe data
# dari sebuah variable
# result = type(age)
# print(result)

# print(type(age))

# function input digunakan untuk menerima inputan user
# name = input("Siapa Nama Anda : ")
# day = input("Hari apakah saat ini : ")

# print('Nama saya adalah  ' + name)
# print('Hari ini adalah hari ' + day)

# Aritmatika


# numThree = "7"

# # function int akan mengubah string menjadi integer
# # hasil = numOne + int(numThree)
# # print(hasil)
# numOne = 10
# numTwo = 5
# result = numOne + numTwo # 15

# # numOne = 10 , numOneString = "10"
# numOneString = str(numOne)
# # numTwo = 5  , numTwoString = "5"
# numTwoString = str(numTwo)
# # result = 15 , resultString = "15"
# resultString = str(result)

# # 10 + 5 = 15
# result = numOne + numTwo
# print(numOneString + " + " + numTwoString + " = " + str(result))

# # 10 - 5 = 5
# result = numOne - numTwo
# print(numOneString + " - " + numTwoString + " = " + str(result))

# # 10 * 5 = 50
# result = numOne * numTwo
# print(numOneString + " * " + numTwoString + " = " + str(result))

# # 10 / 5 = 2
# result = numOne / numTwo
# print(numOneString + " / " + numTwoString + " = " + str(result))

# # 10 % 5 = 0
# result = numOne % numTwo
# print(numOneString + " % " + numTwoString + " = " + str(result))

# # 10 ** 5 = 100000
# result = numOne ** numTwo
# print(numOneString + " ** " + numTwoString + " = " + str(result))


ageJohn = 47
ageKobe = 41

# ageJohn = ageJohn + 3
ageJohn += 3

# ageKobe = ageKobe - 1
ageKobe -= 1

# print(ageJohn)
# print(ageKobe)

# module math
import math

# Mengabsolute sebuah nilai
# print(abs(-13))

# Mengabsolute sebuah nilai kemudian diubah menjadi float
# print(math.fabs(-4))

# Pangkat
# print(math.pow(8, 2))
# print(math.pow(8, 3))

# Akar dua
# print(math.sqrt(64))

# Membulatkan
# print(round(4.7))
# print(round(4.4))

# Floor (dibulatkan ke bawah)
# print(math.floor(4.7))

# Ceil (dibulatkan ke atas)
# print(math.ceil(4.4))


# STRING



# print(len(x)) # Banyak karakter pada string
# index dimulai dari nol
# print(x.index('Dunia')) # Mengetahui letak suatu kata

# Memotong kalimat bedasarkan karakter tertentu, default = spasi " "
# print(x.split())
# print(x.split(" "))

x = 'halo Dunia ku yang cerah'

# Mengubah menjadi huruf kecil
# print(x.lower())

# Mengubah menjadi huruf besar
# print(x.upper())

# Mengubah huruf besar untuk huruf pertama kalimat
# print(x.capitalize())

# print("hello, i'am ironman")
# print('hello, i\'am ironman')
# print('You are "crazy"')
# print("You are \"crazy\" ")

# \n untuk membuat baris baru, enter, new line
print("Hello, i'am ironman" + "\n" +"and i'am \"crazy\"")
print(
    "Hello, i'am ironman" + "\n" + 
    "and i'am \"crazy\""
)


# Duplicate code : SHIFT + ALT + DOWN ARROW
# Untuk membersihkan terminal : CTRL + L
# Membuat komentar : CTRL + /
# Membuka / Menutup terminal : CTRL + J