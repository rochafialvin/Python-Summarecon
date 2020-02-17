# LIST
# Menyimpan data lebih dari satu
# Mengakses data tertentu pada list menggunakan index
# index dimulai dari nol
# Gunakan kurung siku untuk menulis index dari list

animals = ['Tiger', 'Eagle', 'Bear', 'Koala', 'Dolphin', 'Shark']

# Akses satu nilai tertentu
animals[0] # Tiger
animals[2] # Bear
animals[-1] # Shark

# Akses lebih dari satu nilai
# dari index 1 sampai 3
animals[1:4] # Eagle, Bear, Koala

# dari index 0 sampai 3
animals[:4] # Tiger Eagle Bear Koala

# dari index 2 sampai habis
animals[2:] # Bear Koala Dolphin Shark

# SORT #
# Mengurutkan secara ascending
# animals.sort()
# print(animals)

# Mengurutkan secara descending
# animals.sort(reverse=True)
# print(animals)

# APPEND #
# Menambahkan data ke urutan paling akhir
# print(animals)
# animals.append('Bird')
# animals.append('Cat')
# print(animals)

# REMOVE #
# Menghapus data pada list
print(animals)
animals.remove('Shark')
animals.remove('Tiger')
print(animals)

# Method list lainnya
# http://www.yourownlinux.com/2016/10/python-list-methods-append-sort-remove-reverse.html