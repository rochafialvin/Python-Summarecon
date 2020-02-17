# R A N G E
# Sebuah function yang akan me return list of integer
# range menerima 1 parameter wajib, 2 parameter tidak wajib

# Menerima 1 parameter
# Parameter tersebut digunakan sebagai batas akhir angka
# Angka pertama dimulai dari nol
resRange = list(range(5))
print(f'range(5) : {resRange}') # [0, 1, 2, 3, 4]

en = 6
resRange = list(range(en))
print(f'range(en) : {resRange}') # [0, 1, 2, 3, 4, 5]

# Menerima 2 parameter
# Parameter 1 : nilai awal
# Parameter 2 : nilai akhir (tidak termasuk)
resRange = list(range(2, 7))
print(f'range(2, 7) : {resRange}') # [2, 3, 4, 5, 6]

# Menerima 3 parameter
# Parameter 1 : nilai awal
# Parameter 2 : nilai akhir (tidak termasuk)
# Parameter 3 : step, loncatan setiap nilai (default : 1)
resRange = list(range(2, 15, 2))
print(f'range(2, 15, 2) : {resRange}') # [2, 4, 6, 8, 10, 12, 14]  

resRange = list(range(10, 1, -1))
print(f'range(10, 1, -1) : {resRange}') # [10, 9, 8, 7, 6, 5, 4, 3, 2]

resRange = list(range(10, 1, -2))
print(f'range(10, 1, -2) : {resRange}') # [10, 8, 6, 4, 2]


days = ['Sunday', 'Monday', 'Tuesday']

# looping sebanyak data yang ada di days : 3
# [0, 1, 2]
for i in range(len(days)):
    print(f'Loop i : {i}')