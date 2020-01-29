# SOLVE IT - 3

# 1 tahun = 360 hari
# 1 bulan = 30 hari
# 1 minggu = 7 hari

# Tentukan banyaknya hari
days = 485

# Tentukan jumlah tahun
year = int(days / 360)
# Sisa hari setelah diambil sekian tahun
days = days % 360

# Tentukan jumlah bulan
month = int(days / 30)
# Sisa hari setelah diambil sekian bulan
days = days % 30

# Tentukan jumlah minggu
week = int(days / 7)
# Sisa hari setelah diambil sekian minggu
days = days % 7

print(f"{year} tahun")
print(f"{month} bulan")
print(f"{week} minggu")
print(f"{days} hari")