# FILTER (function)
# Function yang digunakan untuk menyaring data
# Menerima function (callback function) dan iterable data
# iterable data : string, list, tuple
# callback function harus menerima satu parameter
# callback function harus me return boolean (True / False)

# for val in 'hello':
#     print(f'Huruf {val}')

# for val in [1, 2, 3]:
#     print(f'{val} * 2 = {val*2}')

numbers = [1, 7, 34, 12, 6, 9, 16]

def even(x):
    resModulus = x % 2
    # Jika hasil modulus adalah  nol, yang berarti x adalah angka genap
    if resModulus == 0:
        return True
    else :
        return False

# filter nilai genap
resFilter = list(filter(even, numbers))
print(resFilter) # [34, 12, 6, 16]


