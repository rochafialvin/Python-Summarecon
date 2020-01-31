# LOOP

# WHILE LOOP
# number = 24

# Akan terus berjalan selama
# kondisi pada while bernilai true
# while number <= 10:
#     print(f'Genap : {number}')
#     number += 2

# FOR LOOP

# [0, 1, 2, 3, 4, 5]
# for i in range(6) :
#     print(f'Angka : {i}')

# [0, 2, 4, 6, 8]
# for i in range(0, 9, 2):
#     print(f'G E N A P : {i}')

# [1, 3, 5, 7, 9]
# for i in range(1, 10, 2):
#     print(f'G A N J I L : {i}')

# [0, 1, 2, 3, 4]
# range(0, 5)
# range(5)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range(1, 11)

# [1, 3, 5, 7, 9]
# range(1, 11, 2)

# DRAWING

# Horizontal Stars
# * * * * * 
# stars = ''

# for val in range(5):
#     stars += ' * '

# print(stars)

# Vertical Stars
# *
# *
# *
# *
# *

# stars = ''

# for i in range(5):
#     stars += ' * '
#     stars += '\n'

# print(stars)



# Square Stars
#  *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  * \n *  *  *  *  *

# stars = ''
# row = 7

# # Menentukan banyaknya baris
# for i in range(row):
#     # Menentukan banyak bintang per baris
#     for j in range(row):
#         stars += ' * '
    
#     stars +='\n'

# print(stars)


# Triangle Stars (increment)
#  * 
#  *  * 
#  *  *  * 
#  *  *  *  * 
#  *  *  *  *  * 

# stars = ''
# row = 5

# # Banyaknya baris
# for i in range(row):
#     # Banyaknya bintang per baris
#     for j in range(i + 1):
#         stars += ' * '

#     stars += '\n'

# print(stars)

# # [5, 4, 3, 2, 1]
# print(list(range(5, 0, -1)))
# # [5, 4, 3, 2]
# print(list(range(5, 1, -1)))
# # [5, 4, 3]
# print(list(range(5, 2, -1)))
# # [5, 4]
# print(list(range(5, 3, -1)))
# # [5]
# print(list(range(5, 4, -1)))


# stars = ''
# row = 5

# # Banyaknya baris
# # [0, 1, 2, 3, 4]
# for i in range(5):
#     # Banyaknya bintang per baris
#     # [5]
#     for j in range(5, i, -1):
#         stars += ' * '

#     stars += '\n'

# print(stars)

# i = 0 -> 1 -> 2 -> 3 -> 4
# j = 5 -> 4 -> 3 -> 2

# stars
#  *  *  *  *  * \n
#  *  *  *  * \n
#  *  *  * \n
#  *  * \n
#  * \n


stars = ''
row = 5

# Banyaknya baris
for i in range(row):

    # Banyaknya bintang per baris
    for j in range(5, i, -1):
        stars += ' * '

    stars += '\n'

# Banyaknya baris
for i in range(1, row, 1):
    # Banyaknya bintang per baris
    for j in range(i + 1):
        stars += ' * '

    stars += '\n'

print(stars)



















