# SOLVE IT - 2

# Meminta input dari user, disimpan di variable
# Input dari user nanti akan berupa 'string'
# "3" ,  bukan 3
numUser = input("Silahkan masukkan sebuah angka : ")

# Ubah input dari user tadi menjadi integer
numUser = int(numUser)

# Hitung kuadrat dari input user
result = numUser ** 2

# Munculkan di terminal
print(f"Kuadrat dari {numUser} = {result}")