# SOLVE IT - 1
import math
# Buat variable dengan nilai
x = 4
y = 3
z = 2

# Melakukan penghitungan
# Hasilnya disimpan di variable result
# (4 + 3 * 2) / (4 * 3)
# 10 / 12
# result = 0.83 
result = (x + y * z) / (x * y)

# Variable result di pangkat z (2)
finalResult = math.pow(result, z) # 0.83 pangkat 2

print(finalResult)

