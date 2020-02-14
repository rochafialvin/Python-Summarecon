# TUPLE
# Menggunakan kurung ()
# Akses value menggunakan index

days = ('Sunday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# Access one value
days[0] # Sunday
days[1] # Monday
days[-1] # Friday

# More than one value
days[1:4] # ('Monday', 'Tuesday', 'Wednesday')

# Count
# Menghitung jumlah value tertentu pada tuple
days.count('Sunday') # 2

# index
# Mencari index dari suatu value pada tuple
days.index('Tuesday') # 3

# ... in ...
# Cek apakah suatu value ada didalam tuple, return True / False
'Saturday' in days # False

# for ... in ...
# loop terhadap semua data yang ada di list
# ('Sunday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
for day in days:
    print(f'Today is {day}')