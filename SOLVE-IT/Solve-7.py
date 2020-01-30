# Ganjil Genap

# Genap , menghasilkan nol jika di modulus dua
# Ganjil , menghasilkan satu jika di modulus dua

number = int(input('Masukkan Angka : '))

if number % 2 == 0:
    status = 'Genap'
else:
    status = 'Ganjil'

print(f'Angka {number} tergolong bilangan {status}')